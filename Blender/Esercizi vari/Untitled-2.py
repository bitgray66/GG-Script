import bpy

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