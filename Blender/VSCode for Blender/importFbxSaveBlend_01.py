from pathlib import Path
import sys 
import os 
import bpy

""" for fbx_file in Path("C:\\Users\\luigi.marazzi\\Desktop\\Prova").glob("*/*.fbx"):
    bpy.ops.wm.read_homefile()
    bpy.ops.import_scene.fbx(filepath=str(fbx_file))
    bpy.ops.wm.save_as_mainfile(filepath=str(fbx_file.with_suffix(".blend"))) """

#"C:\Users\luigi.marazzi\Desktop\Prova\MM_CHR_Melody_A_A_Hi.fbx"

folder = Path(r"C:\\Users\\luigi.marazzi\\Desktop\\Prova")
fbx_files = [f for f in folder.glob("**/*.fbx")]
for fbx_file in fbx_files:
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.import_scene.fbx(filepath=str(fbx_file))