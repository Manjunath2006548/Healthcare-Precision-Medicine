import random

DRUG_GENE_MAP = {
    "CODEINE": "CYP2D6",
    "WARFARIN": "CYP2C9",
    "CLOPIDOGREL": "CYP2C19",
    "SIMVASTATIN": "SLCO1B1",
    "AZATHIOPRINE": "TPMT",
    "FLUOROURACIL": "DPYD"
}

MECHANISM_TEXT = {
    "loss_of_function": "reduced or absent enzymatic activity",
    "gain_of_function": "increased enzymatic activity",
    "reduced_function": "partially decreased transporter function"
}

CLINICAL_IMPACT_TEXT = {
    "loss_of_function": "which may lead to drug accumulation and toxicity",
    "gain_of_function": "which may cause rapid drug metabolism and reduced therapeutic effect",
    "reduced_function": "which may increase systemic drug exposure"
}


def generate_clinical_explanation(drug, variants, risk):
    """
    Generates structured pharmacogenomic explanation.
    """

    target_gene = DRUG_GENE_MAP.get(drug, "unknown")

    intro_templates = [
        f"Pharmacogenomic analysis was performed in relation to {drug}.",
        f"Genetic evaluation of drug response to {drug} was conducted.",
        f"A precision medicine assessment was completed regarding {drug}."
    ]

    explanation = random.choice(intro_templates) + "\n\n"

    gene_variants = [
        v for v in variants
        if v.get("gene", "").upper() == target_gene
    ]

    if not gene_variants:
        explanation += (
            f"No clinically significant variants were identified in {target_gene}. "
            f"Standard dosing of {drug} is likely appropriate.\n\n"
        )
    else:
        for variant in gene_variants:

            gene = variant.get("gene", "")
            variant_id = variant.get("id", "unknown_variant")
            impact = variant.get("impact", "unknown")

            mechanism = MECHANISM_TEXT.get(
                impact,
                "an uncertain functional effect"
            )

            clinical_effect = CLINICAL_IMPACT_TEXT.get(
                impact,
                "which may influence therapeutic outcomes"
            )

            explanation += (
                f"Variant {variant_id} was detected in the {gene} gene. "
                f"This variant is associated with {mechanism}, "
                f"{clinical_effect}. "
                f"Since {drug} is metabolized via {gene}, "
                f"altered gene function may significantly modify drug response.\n\n"
            )

    explanation += f"Overall predicted clinical risk level: {risk}.\n\n"

    explanation += (
        "Genotype-guided prescribing and clinical monitoring are recommended "
        "to optimize therapeutic efficacy and minimize adverse events."
    )

    return explanation
