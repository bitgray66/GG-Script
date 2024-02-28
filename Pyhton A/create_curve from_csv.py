import bpy
import csv

#data blocks for the mesh
verts = []
edges = []
faces = []

#read file change file path
csvPoints = r"C:\Users\luigi.marazzi\Desktop\test.csv"
pointsReader = csv.reader(open(csvPoints, newline=''), delimiter=',')   

#add points to verts
for row in pointsReader:
    vert = (float(row[0]), float(row[1]), 0) 
    verts.append(vert)
    
#Add points indexes to edges
for idx, vert in enumerate(verts):
    startPoint = idx
    if idx < len(verts)-1:
        endPoint = idx+1
    else:
        endPoint = 0
    edge = startPoint, endPoint
    edges.append(edge)

#create mesh 
newMesh = bpy.data.meshes.new("Boundary")
    
#cAdd python data blocks to mesh
newMesh.from_pydata(verts,edges,faces)
newMesh.update(calc_edges=True)

#create an object
newObject = bpy.data.objects.new("Boundary",newMesh)

#set mesh location
bpy.context.collection.objects.link(newObject)