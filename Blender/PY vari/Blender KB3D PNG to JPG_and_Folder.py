import bpy

for img in bpy.data.images:
    img.filepath = img.filepath.replace('.png', '.jpg')
    img.name = img.name.replace('.png', '.jpg')
    img.filepath = img.filepath.replace('4k', 'Renamemetopackname') #Rename that to whatever you renamed the 4k folder to. ie. CyberDistrict
    img.name = img.name.replace('4k', 'Renamemetopackname') #Rename that to whatever you renamed the 4k folder to. ie. CyberDistrict
    img.reload()
print("Done! Save your blend file!")

#When it's finished make sure everything looks correct and save the blend file with a new name ie > Save-As "Packname_jpg.blend"