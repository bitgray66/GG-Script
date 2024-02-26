import os
import maya.cmds as cmds
import tkinter as tk
from tkinter import filedialog

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

def cerca_file_ma(start_folder):
    for root, dirs, files in os.walk(start_folder):
        for file in files:
            if file.endswith('.ma'):
                file_path = os.path.join(root, file)
                aggiungi_sfera(file_path)

def seleziona_cartella_master():
    root = tk.Tk()
    root.withdraw()  # Nasconde la finestra principale di Tkinter
    master_folder = filedialog.askdirectory(title="Seleziona cartella master")
    if master_folder:
        cerca_file_ma(master_folder)

seleziona_cartella_master()
