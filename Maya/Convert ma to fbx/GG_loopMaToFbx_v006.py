import os
import maya.cmds as cmds

def add_change(file_path):
    # Apri il file
    cmds.file(new=True, force=True)
    cmds.file(file_path, open=True)
    
    # Aggiungi una sfera di raggio 3
    cmds.polySphere(radius=3)
    
    # Salva il file come FBX
    file_name = os.path.basename(file_path)
    print("file_name =", file_name)
    #save_path = os.path.join(os.path.dirname(file_path), file_name.replace('.ma', '_OK.ma'))
    save_path = os.path.join(os.path.dirname(file_path), file_name)
    print("save_path =", save_path)
    cmds.file(rename=save_path)
    cmds.file(force=True, options="v=0;", type="FBX export", pr=True, es=True)
    return file_name  # Restituisci il percorso del file FBX salvato

def cerca_file_ma(start_folder):
    converted_files = []  # Lista per memorizzare i nomi dei file convertiti
    for root, dirs, files in os.walk(start_folder):
        for file in files:
            if file.endswith('.ma'):
                file_path = os.path.join(root, file)
                converted_file = add_change(file_path)
                converted_files.append(converted_file)
    return converted_files

# Esegui la funzione per cercare e modificare i file .ma nella cartella "Start"
master_folder = "C:\\Users\\luigi.marazzi\\Desktop\\Prova"
converted_files = cerca_file_ma(master_folder)

# Creazione del file di testo
text_file_path = os.path.join(master_folder, "converted_files.txt")

with open(text_file_path, "w") as text_file:
    nFile = 1
    for file_path in converted_files:
        print("nFile =", nFile)
        print("file_path2 =", file_path)
        text_file.write(f'{nFile}   {file_path}\n' )
        nFile=nFile+1