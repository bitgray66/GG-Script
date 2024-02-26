import os
import maya.cmds as cmds

def add_change(file_path):
    # Apri il file
    cmds.file(new=True, force=True)
    cmds.file(file_path, open=True)
    
    # Controllo gruppi nella scena
    scene_name = os.path.splitext(os.path.basename(file_path))[0]
    group_name = scene_name + "_GRP"
    groups = cmds.ls(group_name)
    if len(groups) != 1 or groups[0] != group_name:
        # Se non c'è un gruppo o ce ne sono più di uno, annota nel file di testo
        with open("error_log.txt", "a") as error_file:
            error_file.write(f"{file_path}: Da controllare\n")
        return
    
    # Aggiungi una sfera di raggio 3
    cmds.polySphere(radius=3)
    
    # Scalare il gruppo del 10%
    selection = cmds.ls(selection=True)
    if selection:
        cmds.scale(1.1, 1.1, 1.1, selection[0], relative=True)
    
    # Salva il file con il suffisso "_OK"
    save_path = os.path.join(os.path.dirname(file_path), scene_name + '_OK.ma')
    cmds.file(rename=save_path)
    cmds.file(force=True, options="v=0;", type="FBX export", pr=True, es=True)

def cerca_file_ma(start_folder):
    for root, dirs, files in os.walk(start_folder):
        for file in files:
            if file.endswith('.ma'):
                file_path = os.path.join(root, file)
                add_change(file_path)

# Esegui la funzione per cercare e modificare i file .ma nella cartella "Start"
master_folder = "C:\\Users\\Admin\\Desktop\\Start"
error_log_path = os.path.join(master_folder, "error_log.txt")
if os.path.exists(error_log_path):
    os.remove(error_log_path)  # Rimuovi il file di log precedente se esiste
cerca_file_ma(master_folder)
