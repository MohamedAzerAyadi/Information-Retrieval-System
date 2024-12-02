import os 
from pathlib import Path
#Path détecte l'OS automatiquement pour convertir les chaines de chemins en chemins corrects 
#Exemple : sous windows '/' -> '\'


#redirection des logs vers un fichier
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

#création de l'arborescence du projet 
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files: 
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    #creation du dossier
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    #creation du fichier 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else: 
        logging.info(f"{filename} already exists")