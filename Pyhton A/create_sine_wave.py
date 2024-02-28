import bpy
import math

for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)


mesh = bpy.data.meshes.new('sin curve')
samples = 100
lenght = 30
height = 3
step = lenght/samples

mesh.vertices.add(samples)
mesh.edges.add(samples-1)

for i in range(samples):
    current_vertex = mesh.vertices[i]
    current_vertex.co = (0, i, math.sin(i))
    if i < (samples):
        mesh.edges[1].vertices = (i, i+1)

obj = bpy.data.objects.new('sin curve', mesh)

bpy.context.collection.objects.link(obj)

obj.modifiers.new(type='SKIN', name='skin')
