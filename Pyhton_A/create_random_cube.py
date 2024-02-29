import bpy
import random

for obj in bpy.data.objects: # bpy.data.objects genera una collezione degli oggetti in scena
    print(obj)
    bpy.data.objects.remove(obj) 

for i in range(100):

    x_rand_value = random.uniform(-10,10)
    y_rand_value = random.uniform(-10,10)
    z_rand_value = random.uniform(-10,10)

    bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(x_rand_value, y_rand_value, z_rand_value), scale=(1, 1, 1))



 



