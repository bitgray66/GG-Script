# give Python access to Blender's functionality
import bpy

bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

print('####################################')
main_col = bpy.context.object.name
print('-A-'+main_col)

i=3
for obj in bpy.data.objects:
    print(obj.name +'---'+ obj.type +'---'+str(i))
    if obj.type == 'EMPTY':
        print(obj.name +'-@-'+ obj.type +'---'+str(i))
        obj.name = obj.name.replace("_GRP", "_COL"+str(i))
        i=i-1

    """ main_coll_name = "main"
    main_coll = bpy.data.collections.new(name=main_coll_name) """









########################################
import bpy

print('####################################')
for obj in bpy.data.objects:
    print(obj.name +'---'+ obj.type )
    if obj.parent:
        print('child')
    else:
        print('parent')
########################################
        
import bpy

print('####################################')
ob = bpy.context.object

tree = [ob]
while ob.parent:
    ob = ob.parent
    tree.append(ob)
    
print("/".join(map(lambda x: x.name, tree[::-1])))

########################################

# If you want to process every object in a collection, you would have to iterate through Collection.all_objects:

collection = bpy.data.collections["collection_name"]
for obj in collection.all_objects:
    print(obj.name) 


########################################
    
import bpy

print('####################################')
main_col = bpy.context.object
i=3
for obj in bpy.data.objects:
    print(obj.name +'---'+ obj.type )
    if obj.type == 'EMPTY':
        obj.name = obj.name.replace("_GRP", "_COL"+str(i))
        i=i-1

########################################
import bpy       
for obj in bpy.data.objects:
    bpy.data.objects.remove(obj)

for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)