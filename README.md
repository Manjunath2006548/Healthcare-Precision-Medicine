# Healthcare Precision Medicine

Healthcare Precision Medicine is a platform that analyzes patient genomic data (VCF files) to identify pharmacogenomic variants in six critical genes (CYP2D6, CYP2C19, CYP2C9, SLCO1B1, TPMT, DPYD). It predicts drug-specific risks, generates clinical explanations, and provides CPIC-aligned dosing recommendations.

---

## 🔗 Live Demo

https://photos.app.goo.gl/DXmsh2XtykYegdEo9

## 📹 LinkedIn Video

https://www.linkedin.com/posts/manjunathbhaskar_pharmaguard-pharmacogenomics-aiinhealthcare-ugcPost-7430420696989777920-5Wkp?utm_source=share&utm_medium=member_android&rcm=ACoAAFSDX68BTLLdgGYcxLOZMel2H_a-c7okWiY

## PROJECT PRESENTATION

https://www.canva.com/design/DAHBwlae_Uc/uLTaJBBp5GVGkJ4H9WgJXA/edit?utm_content=DAHBwlae_Uc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

---

## 🏗 Architecture Overview

The system has two main components:

**Backend (Python + Flask)**  
- Parses VCF files  
- Identifies pharmacogenomic variants  
- Evaluates drug-specific risk  
- Generates clinical explanations  

**Frontend (HTML, CSS, JavaScript)**  
- User-friendly dashboard  
- Upload VCF, select drug, input patient info  
- Displays risk prediction and clinical explanation  

---

## 🛠 Tech Stack
- Python 3.14, Flask, Flask-CORS  
- HTML, CSS, JavaScript  
- Dependencies listed in `requirements.txt`  
- Sample VCF files included  

---

## ⚡ Installation Instructions

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/RIFT-Healthcare-Precision-Medicine.git
cd RIFT-Healthcare-Precision-Medicine/backend

Install dependencies:
Bash
pip install -r requirements.txt
Run the Flask server:
Bash
python server.py
Open index.html in your browser to access the frontend dashboard.

🧬 API Documentation
POST /analyze
Description: Upload a VCF and drug info to get pharmacogenomic risk assessment.
Request Body (multipart/form-data):
file: VCF file
drug: Drug name
patient_name, age, weight

Sample Response:
Json

{
  "drug": "CODEINE",
  "primary_gene": "CYP2D6",
  "risk_level": "Safe",
  "variants_detected": [
      {
          "id": "rs123",
          "gene": "CYP2D6",
          "impact": "reduced_function"
      }
  ],
  "clinical_explanation": "Genetic evaluation of drug response to CODEINE was conducted..."
}

💻 Usage Example

Open the frontend dashboard.
Enter patient info and select the drug.
Upload a VCF file.
Click Predict.
View predicted risk and detailed clinical explanation.

👥 Team Members
Manjunath Bhaskar Hebbar
VENKATA DHANUSH REDDY MALLELA
Ajay k
Bhaskar



📂 Repository Structure


Healthcare-Precision-Medicine/
│
├── backend/
│   ├── llm_model.py
│   ├── parse_vcf_script.py
│   ├── server.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── sample_vcfs/
│   ├── sample1.vcf
│   ├── sample2.vcf
│   ├── sample3.vcf
│   └── sample4.vcf
│
├── json_outputs/
│   ├── sample1.json
│   ├── sample2.json
│   ├── sample3.json
│   └── sample4.json
│
└── README.md

✅ Features

1.Parses authentic VCF files (industry-standard genomic data).
2.Identifies pharmacogenomic variants across 6 critical genes.
3.Predicts drug-specific risks: Safe, Adjust Dosage, Toxic, Ineffective, Unknown.
4.Generates clinical explanations with variant citations and biological mechanisms.
5.Provides CPIC-aligned dosing recommendations.





