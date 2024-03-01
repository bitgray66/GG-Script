import bpy

########## START Clear

for obj in bpy.data.objects:
    bpy.data.objects.remove(obj)

for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)

for coll in bpy.data.collections:
    bpy.data.collections.remove(coll)

for mat in bpy.data.materials:
    bpy.data.materials.remove(mat)













class MyPanel(bpy.types.Panel):
    bl_label = "Material Creator"
    bl_idname = "PT_MyPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Enter Material Name:")
        row = layout.row()
        row.prop(context.scene, "my_material_name")
        
        row = layout.row()
        row.operator("object.create_material_operator")

def register():
    bpy.utils.register_class(MyPanel)
    bpy.types.Scene.my_material_name = bpy.props.StringProperty(name="Material Name", default="")

def unregister():
    bpy.utils.unregister_class(MyPanel)
    del bpy.types.Scene.my_material_name

if __name__ == "__main__":
    register()










##############
    import bpy

# If there ARE objects selected then act on all objects
if bpy.context.selected_objects != []:
    for obj in bpy.context.selected_objects:
        print(obj.name, obj, obj.type)
        if obj.type == 'MESH': 
            print("&gt;&gt;&gt;&gt;", obj.name)


# If there are NO objects selected then act on all objects
if bpy.context.selected_objects == []:
    print('selected:')
    for obj in bpy.context.scene.objects: 
        print(obj.name, obj, obj.type)
        if obj.type == 'MESH': 
            print("&gt;&gt;&gt;&gt;", obj.name)    




########## START obj in collections
            
# For an if statement, I want to check if my current object is in collection 'coll' Here's what I have so far:

def GO():
    objects = bpy.data.objects
    for obj in objects:
        if obj.parent==None and obj.type=='MESH' and obj.collection.name('coll'):

# Answers
# Assuming your object is in only one collection, you can use:

if obj.users_collection[0].name == "coll":
    print("yes")

# If your object is present in multiple collections and you want to just check if it is also part of the collection named "coll", you can use:

if "coll" in [c.name for c in obj.users_collection]:
    print("yes")



# There is no collection member in bpy.types.Object
# instead you need to search the collection for the object:

def is_in_collection(name, obj):
    try:
        col = bpy.data.collections[name]
        for o in col.objects:
            if obj is o:
                return True
        return False
    except KeyError:
        return False
    return False

########## STOP obj in collections