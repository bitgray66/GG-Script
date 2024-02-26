################################# BPY.CONTEXT


bpy.context.object.location.x = 1
bpy.context.object.location.x += 0.5
bpy.context.object.location.xy = (1, 2)
type(bpy.context.object.location)
dir(bpy.context.object.location)

################################# BPY.DATA

bpy.data.objects
""" <bpy_collection[3], BlendDataObjects> """

bpy.data.scenes
""" <bpy_collection[1], BlendDataScenes> """

bpy.data.materials
""" <bpy_collection[1], BlendDataMaterials> """

for object in bpy.data.objects :
    print(f"{object.name} is at location {object.location}")

""" Camera is at location <Vector (7.3589, -6.9258, 4.9583)>
Cube is at location <Vector (1.0000, 0.0000, 0.0000)>
Light is at location <Vector (4.0762, 1.0055, 5.9039)>
Sphere is at location <Vector (1.0000, 0.0000, 3.6092)> """

import bpy


# print all objects
for obj in bpy.data.objects:
    print(obj.name)


# print all scene names in a list
print(bpy.data.scenes.keys())


# remove mesh Cube
if "Cube" in bpy.data.meshes:
    mesh = bpy.data.meshes["Cube"]
    print("removing mesh", mesh)
    bpy.data.meshes.remove(mesh)


# write images into a file next to the blend
import os
with open(os.path.splitext(bpy.data.filepath)[0] + ".txt", 'w') as fs:
    for image in bpy.data.images:
        fs.write("%s %d x %d\n" % (image.filepath, image.size[0], image.size[1]))

import os
with open(os.path.splitext(bpy.data.filepath)[0] + ".txt", 'w') as fs:
    for obj in bpy.data.objects:
        fs.write("%s\n" % (obj.name))



################################# OPERATORI
import bpy




# check poll() to avoid exception.
if bpy.ops.object.mode_set.poll():
    bpy.ops.object.mode_set(mode='EDIT')

# calling an operator
bpy.ops.mesh.subdivide(number_cuts=3, smoothness=0.5)

# Remove all objects in scene rather than the selected ones.
import bpy
from bpy import context
context_override = context.copy()
context_override["selected_objects"] = list(context.scene.objects)
with context.temp_override(**context_override):
    bpy.ops.object.delete()

#### Contesto di esecuzione
    
# collection add popup
import bpy
bpy.ops.object.collection_instance_add('INVOKE_DEFAULT')

# Maximize 3d view in all windows.
import bpy
from bpy import context

###
for window in context.window_manager.windows:
    screen = window.screen
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            with context.temp_override(window=window, area=area):
                bpy.ops.screen.screen_full_area()
            break