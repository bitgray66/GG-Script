bl_info = {
    "name": "Mobo Custom Panel",
    "author": "Luigi Marazzi",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D Viewport > Sidebar > Mobo",
    "description": "Mobo setting panel",
    "category": "Development",
}

# give Python access to Blender's functionality
from typing import Set
import bpy
import os
from bpy.types import Context


class CAT_PT_rnm_mesh(bpy.types.Operator):
    """"Setting the render output path"""

    bl_label = "label1" # found at the top of the Panel
    bl_idname = "boo.reset1" # found at the top of the Panel

    def execute(self, context):
        selected_object = bpy.context.active_object

        if selected_object is None:
            print("Nessun oggetto selezionato.")
            quit()

        selected_name = selected_object.name
        print(selected_name)

        for obj in bpy.context.scene.objects:
            if obj.type in ['MESH', 'CURVE']:
                obj.name = selected_name

                if obj.data:
                    obj.data.name = selected_name + "_Mesh"

        print("Operazione completata con successo.")
        return {"FINISHED"}
    









class VIEW3D_PT_mobo_panel(bpy.types.Panel):

    # where to add the panel in the UI
    bl_space_type = "VIEW_3D"  # 3D Viewport area (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items)
    bl_region_type = "UI"  # Sidebar region (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items)
   
    bl_category = 'Mobo' # found in the Sidebar
    bl_label = "Mobo Panel" # found at the top of the Panel
    bl_idname = "PT_MoboPanel"
    

    def draw(self, context):
        """define the layout of the panel"""
        layout = self.layout

        row = layout.row()
        row.operator("boo.reset1", text="rename_M_C")
        # row.operator("boo.reset2", text="clear All")

        self.layout.separator()









def register():
    bpy.utils.register_class(VIEW3D_PT_mobo_panel)
    bpy.utils.register_class(CAT_PT_rnm_mesh)
    # bpy.utils.register_class(CAT_PT_clear_all)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_mobo_panel)
    bpy.utils.unregister_class(CAT_PT_rnm_mesh)
    # bpy.utils.unregister_class(CAT_PT_clear_all)

if __name__ == "__main__":
    register()
    







    