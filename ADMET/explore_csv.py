import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

out_dir = Path("ADMET/results")
out_dir.mkdir(parents=True, exist_ok=True)
out_dir = Path("ADMET/plots")
out_dir.mkdir(parents=True, exist_ok=True)




def make_plots(myJobName):
    myJobName = myJobName
    csv_file_path = f"./ADMET/results/{myJobName}/pred.csv"

    df = pd.read_csv(csv_file_path)


    row = df.iloc[0]

    print("")
    print(row["ClinTox_drugbank_approved_percentile"])

    # Pick the 5 “dashboard” axes (use percentiles so everything is already 0–100)
    axes = {
        "Blood-Brain Barrier Safe": "BBB_Martins_drugbank_approved_percentile",
        "hERG Safe": "hERG_drugbank_approved_percentile",
        "Bioavailable": "Bioavailability_Ma_drugbank_approved_percentile",
        "Soluble": "Solubility_AqSolDB_drugbank_approved_percentile",
    }

    # A simple “Non-Toxic” score as the average of several toxicity-related percentiles
    tox_percentile_cols = [
        "ClinTox_drugbank_approved_percentile",
        "AMES_drugbank_approved_percentile",
        "DILI_drugbank_approved_percentile",
        "Carcinogens_Lagunin_drugbank_approved_percentile",
        "Skin_Reaction_drugbank_approved_percentile",
    ]
    non_toxic = float(np.mean([row[c] for c in tox_percentile_cols if c in df.columns]))

    labels = list(axes.keys()) + ["Non-Toxic"]
    values = [float(row[col]) for col in axes.values()] + [non_toxic]


    # # Optional: save
    # # plt.savefig("radar.png", dpi=200, bbox_inches="tight")

    # --- Radar plot (black background) ---
    N = len(labels)
    angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    values_plot = values + values[:1]
    angles_plot = angles + angles[:1]

    fig = plt.figure(figsize=(4, 4), facecolor="black")
    ax = plt.subplot(111, polar=True, facecolor="black")

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # White labels
    ax.set_thetagrids(np.degrees(angles), labels, fontsize=9, color="white")

    # White radial ticks
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels(["0", "25", "50", "75", "100"], fontsize=8, color="white")

    # Grid + spine colors (light gray/white)
    ax.grid(color="white", alpha=0.25)
    ax.spines["polar"].set_color("white")
    ax.spines["polar"].set_alpha(0.35)

    # Make tick marks white too
    ax.tick_params(colors="white")

    # Plot + fill (kept red like your example)
    ax.plot(angles_plot, values_plot, linewidth=2, color="red")
    ax.fill(angles_plot, values_plot, color="red", alpha=0.25)

    ax.set_title(f"ADMET {myJobName} Safety Summary", color="white", pad=12)

    plt.tight_layout()
    # plt.show()

    # Optional save with black background
    plt.savefig(f"ADMET/plots/radar_{myJobName}.png", dpi=200, facecolor="black", bbox_inches="tight")



    # EXTRA:

    # # Show first 10 rows nicely formatted
    # print(df["logP"].head(10))

    # Show all the columns
    # print(df.columns)

    # --- Smiles String ---
    smiles_col = ["smiles"]

    # --- Physicochemical (matches website Physicochemical) ---
    physicochemical_cols = [
        "molecular_weight",
        "logP",
        "hydrogen_bond_acceptors",
        "hydrogen_bond_donors",
        "Lipinski",
        "QED",
        "stereo_centers",
        "tpsa",
    ]

    # --- Absorption (matches website Absorption) ---
    # Website includes: HIA, Bioavailability, Aqueous Solubility, Lipophilicity, Hydration FE,
    # Cell Effective Permeability, PAMPA, P-gp inhibition
    absorption_cols = [
        "HIA_Hou",                      # Human Intestinal Absorption
        "Bioavailability_Ma",           # Oral Bioavailability
        "Solubility_AqSolDB",           # Aqueous Solubility
        "Lipophilicity_AstraZeneca",    # Lipophilicity
        "HydrationFreeEnergy_FreeSolv", # Hydration Free Energy
        "Caco2_Wang",                   # Cell Effective Permeability (proxy/label on site)
        "PAMPA_NCATS",                  # PAMPA Permeability
        "Pgp_Broccatelli",              # P-glycoprotein Inhibition
    ]

    # --- Distribution (matches website Distribution) ---
    distribution_cols = [
        "BBB_Martins",                  # Blood-Brain Barrier Penetration
        "PPBR_AZ",                      # Plasma Protein Binding Rate
        "VDss_Lombardo",                # Volume of Distribution at Steady State
    ]

    # --- Metabolism (matches website Metabolism) ---
    # Inhibition columns + substrate columns
    metabolism_cols = [
        "CYP1A2_Veith",
        "CYP2C19_Veith",
        "CYP2C9_Veith",
        "CYP2D6_Veith",
        "CYP3A4_Veith",
        "CYP2C9_Substrate_CarbonMangels",
        "CYP2D6_Substrate_CarbonMangels",
        "CYP3A4_Substrate_CarbonMangels",
    ]

    # --- Excretion (matches website Excretion) ---
    excretion_cols = [
        "Half_Life_Obach",              # Half Life
        "Clearance_Hepatocyte_AZ",      # Drug Clearance (Hepatocyte)
        "Clearance_Microsome_AZ",       # Drug Clearance (Microsome)
    ]

    # --- Toxicity (matches website Toxicity) ---
    # Core toxicity + Nuclear receptor + Stress response endpoints shown under Toxicity on site
    toxicity_core_cols = [
        "hERG",
        "ClinTox",
        "AMES",                         # Mutagenicity on website
        "DILI",
        "Carcinogens_Lagunin",
        "LD50_Zhu",
        "Skin_Reaction",
    ]

    toxicity_receptor_cols = [
        "NR-AR",
        "NR-AR-LBD",
        "NR-AhR",
        "NR-Aromatase",
        "NR-ER",
        "NR-ER-LBD",
        "NR-PPAR-gamma",
    ]

    toxicity_stress_response_cols = [
        "SR-ARE",
        "SR-ATAD5",
        "SR-HSE",
        "SR-MMP",
        "SR-p53",
    ]

    # If your CSV also has these two and you want them under Toxicity:
    toxicity_other_cols = [
        "Mitochondrial Membrane Potential",  # NOTE: your CSV column is "SR-MMP" (already above)
        "Tumor Protein p53",                 # NOTE: your CSV column is "SR-p53" (already above)
    ]

    # # ---- Printing (1-row dataframe slices) ----
    # print(df[smiles_col])
    # print(df[physicochemical_cols])

    # print(df[absorption_cols])
    # print(df[distribution_cols])
    # print(df[metabolism_cols])
    # print(df[excretion_cols])

    # print(df[toxicity_core_cols])
    # print(df[toxicity_receptor_cols])
    # print(df[toxicity_stress_response_cols])


# make the radar graph
smi_folder = Path("ADMET/test_samples_smiles")

for smi_file in smi_folder.glob("*.smi"):
    myJobName = smi_file.stem   # 👉 "samples_1"

    with open(smi_file, "r") as f:
        for line in f:
            smiles = line.strip().split()[0]   # first column is SMILES
            
            print("File:", myJobName)
            print("SMILES:", smiles)

            make_plots(myJobName)