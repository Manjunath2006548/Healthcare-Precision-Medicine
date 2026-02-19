from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from parse_vcf_script import parse_vcf
from llm_model import generate_clinical_explanation

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests for frontend

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Drug → Gene Mapping
DRUG_GENE_MAP = {
    "CODEINE": "CYP2D6",
    "WARFARIN": "CYP2C9",
    "CLOPIDOGREL": "CYP2C19",
    "SIMVASTATIN": "SLCO1B1",
    "AZATHIOPRINE": "TPMT",
    "FLUOROURACIL": "DPYD"
}

# Variant Impact → Risk Logic
VARIANT_IMPACT_RULES = {
    "CYP2D6": {"loss_of_function": "Ineffective", "gain_of_function": "Toxic", "reduced_function": "Adjust Dosage"},
    "CYP2C19": {"loss_of_function": "Ineffective", "reduced_function": "Adjust Dosage"},
    "CYP2C9": {"loss_of_function": "Toxic", "reduced_function": "Adjust Dosage"},
    "SLCO1B1": {"reduced_function": "Toxic"},
    "TPMT": {"loss_of_function": "Toxic"},
    "DPYD": {"loss_of_function": "Toxic"}
}

def evaluate_risk(drug, variants):
    drug = drug.upper()
    if drug not in DRUG_GENE_MAP:
        return "Unknown"

    target_gene = DRUG_GENE_MAP[drug]
    gene_rules = VARIANT_IMPACT_RULES.get(target_gene, {})

    for variant in variants:
        if variant["gene"] == target_gene:
            impact = variant["impact"]
            if impact in gene_rules:
                return gene_rules[impact]
    return "Safe"

# Health Check
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "RIFT Precision Medicine API Running"})

# Main VCF Analysis Endpoint
@app.route("/parse_vcf", methods=["POST"])
def parse_vcf_route():
    if "vcf_file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["vcf_file"]
    drug = request.form.get("drug_name", "").upper()
    patient_name = request.form.get("patient_name", "")
    age = request.form.get("age", "")
    weight = request.form.get("weight", "")

    if not drug or not patient_name or not age or not weight:
        return jsonify({"error": "All patient fields are required"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    variants, primary_gene = parse_vcf(file_path)
    risk = evaluate_risk(drug, variants)
    explanation = generate_clinical_explanation(drug, variants, risk)

    return jsonify({
        "patient_info": {
            "name": patient_name,
            "age": age,
            "weight": weight
        },
        "patient_id": file.filename.replace(".vcf", ""),
        "drug": drug,
        "primary_gene": primary_gene,
        "risk_assessment": {"risk_label": risk},
        "variants_detected": variants,
        "clinical_explanation": explanation
    })

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)