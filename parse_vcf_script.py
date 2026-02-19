# parse_vcf_script.py

CRITICAL_GENES = {
    "CYP2D6",
    "CYP2C19",
    "CYP2C9",
    "SLCO1B1",
    "TPMT",
    "DPYD"
}


def normalize_impact(raw_impact):
    """
    Convert raw IMPACT field into standardized categories:
    loss_of_function
    gain_of_function
    reduced_function
    unknown
    """
    raw_impact = raw_impact.lower()

    if "high" in raw_impact or "loss" in raw_impact:
        return "loss_of_function"

    if "gain" in raw_impact:
        return "gain_of_function"

    if "moderate" in raw_impact or "reduced" in raw_impact:
        return "reduced_function"

    return "unknown"


def parse_vcf(file_path):
    """
    Parses VCF file and returns:
        variants: list of dicts [{id, gene, impact}]
        primary_gene: first critical gene detected
    """

    variants = []
    primary_gene = "Unknown"

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            # Skip header lines
            if line.startswith("#"):
                continue

            parts = line.split("\t")
            if len(parts) < 8:
                continue

            chrom, pos, rsid, ref, alt, qual, filt, info = parts[:8]

            # Parse INFO field
            info_dict = {}
            for item in info.split(";"):
                if "=" in item:
                    key, val = item.split("=", 1)
                    info_dict[key] = val

            gene = info_dict.get("GENE", "Unknown").upper()

            # 🔥 Filter only 6 pharmacogenomic genes
            if gene not in CRITICAL_GENES:
                continue

            raw_impact = info_dict.get("IMPACT", "unknown")
            impact = normalize_impact(raw_impact)

            if primary_gene == "Unknown":
                primary_gene = gene

            variants.append({
                "id": rsid if rsid != "." else f"{chrom}:{pos}",
                "gene": gene,
                "impact": impact
            })

    return variants, primary_gene