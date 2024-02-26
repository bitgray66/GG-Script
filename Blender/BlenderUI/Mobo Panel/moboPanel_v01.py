bl_info = {
    "name": "Mobo Custom Panel",
    "author": "Luigi Marazzi",
    "version": (0, 0, 1),
    "blender": (3, 00, 0),
    "location": "3D Viewport > Sidebar > Mobo",
    "description": "Mobo setting panel",
    "category": "many",
}

# give Python access to Blender's functionality
import bpy


class VIEW3D_PT_Mobo_panel(bpy.types.Panel):

    # where to add the panel in the UI
    bl_space_type = "VIEW_3D"  # 3D Viewport area (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items)
    bl_region_type = "UI"  # Sidebar region (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items)
   
    bl_category = 'Mobo' # found in the Sidebar
    bl_label = "Render Path" # found at the top of the Panel
    bl_idname = "PT_MoboPanel"
    

    def draw(self, context):
        """define the layout of the panel"""
        layout = self.layout

        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Add SceneName")

        bpy.context.space_data.use_local_camera = True

        row = layout.row()
        row.prop(context.scene, "my_material_name")
        
        row = layout.row()
        row.operator("object.create_material_operator")

def register():
    bpy.utils.register_class(VIEW3D_PT_Mobo_panel)
    bpy.types.Scene.my_material_name = bpy.props.StringProperty(name="Material Name", default="")

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_Mobo_panel)
    del bpy.types.Scene.my_material_name

if __name__ == "__main__":
    register()
    





import bpy

class CreateMaterialOperator(bpy.types.Operator):
    bl_idname = "object.create_material_operator"
    bl_label = "Create Material and Assign"

    def execute(self, context):
        material_name = context.scene.my_material_name

        # Creazione del materiale
        material = bpy.data.materials.new(name=material_name)

        # Assegnazione del materiale al cubo attivo
        if bpy.context.active_object:
            bpy.context.active_object.data.materials.append(material)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(CreateMaterialOperator)

def unregister():
    bpy.utils.unregister_class(CreateMaterialOperator)

if __name__ == "__main__":
    register()

    