import os
import maya.cmds as cmds
import openpyxl

def aggiungi_sfera(file_path):
    # Apri il file
    cmds.file(new=True, force=True)
    cmds.file(file_path, open=True)
    
    # Aggiungi una sfera di raggio 3
    cmds.polySphere(radius=3)
    
    # Salva il file con il suffisso "_OK"
    file_name = os.path.basename(file_path)
    save_path = os.path.join(os.path.dirname(file_path), file_name.replace('.ma', '_OK.ma'))
    cmds.file(rename=save_path)
    cmds.file(force=True, options="v=0;", type="FBX export", pr=True, es=True)
    return save_path  # Restituisci il percorso del file FBX salvato

def cerca_file_ma(start_folder):
    converted_files = []  # Lista per memorizzare i nomi dei file convertiti
    for root, dirs, files in os.walk(start_folder):
        for file in files:
            if file.endswith('.ma'):
                file_path = os.path.join(root, file)
                converted_file = aggiungi_sfera(file_path)
                converted_files.append(converted_file)
    return converted_files

# Esegui la funzione per cercare e modificare i file .ma nella cartella "Starte"
master_folder = "C:\\Users\\Admin\\Desktop\\Start"
converted_files = cerca_file_ma(master_folder)

# Creazione del file Excel
excel_file_path = os.path.join(master_folder, "converted_files.xlsx")
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Converted Files"

# Scrivi i nomi dei file FBX convertiti nel file Excel
for idx, file_path in enumerate(converted_files, start=1):
    sheet.cell(row=idx, column=1, value=file_path)

# Salva il file Excel
workbook.save(excel_file_path)




""" import sys
!{sys.executable} -m pip install openpyxl """