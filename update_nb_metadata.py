import json
import os

notebooks = [
    "notebooks/01_Ingestion_Pipeline.ipynb",
    "notebooks/02_Compliance_Assistant.ipynb",
    "notebooks/03_Validation_Rules.ipynb"
]

for nb_path in notebooks:
    if os.path.exists(nb_path):
        with open(nb_path, "r", encoding="utf-8") as f:
            nb = json.load(f)
        
        nb["metadata"]["kernelspec"] = {
            "display_name": "Python 3 (AMD-Hackathon)",
            "language": "python",
            "name": "amd_hackathon_venv"
        }
        
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print(f"Updated metadata for {nb_path}")
