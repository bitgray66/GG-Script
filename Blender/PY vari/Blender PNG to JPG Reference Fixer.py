import bpy

for img in bpy.data.images:
    img.filepath = img.filepath.replace('.png', '.jpg')
    img.name = img.name.replace('.png', '.jpg')
    img.reload()
print("Done! Save your blend file!")

#When it's finished make sure everything looks correct and save the blend file with a new name ie > Save-As "Packname_jpg.blend"