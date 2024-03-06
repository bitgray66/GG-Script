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



class CAT_OT_RenameMeshOperator(bpy.types.Operator):
    """"Rename all mesh from selected Coll"""
    bl_label = "Rename Mesh Objects"
    bl_idname = "cat.rename_mesh"

    def execute(self, context):
        
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                obj.data.name = obj.name
            if obj.type == 'CURVES':
                obj.data.name = obj.name

        return {"FINISHED"}
    

class CAT_OT_DeletAllOperator(bpy.types.Operator):
    """"Delete Coll Objects Mesh Mat"""
    bl_label = "Delete Coll Objects Mesh Mat"
    bl_idname = "cat.delate_all"

    def execute(self, context):
        
        for obj in bpy.data.objects:
            bpy.data.objects.remove(obj)

        for mesh in bpy.data.meshes:
            bpy.data.meshes.remove(mesh)

        for coll in bpy.data.collections:
            bpy.data.collections.remove(coll)

        for mat in bpy.data.materials:
            bpy.data.materials.remove(mat)

        return {"FINISHED"}



class WIEW3D_PT_MoboPanel(bpy.types.Panel):

    # where to add the panel in the UI
    bl_space_type = "VIEW_3D"  # 3D Viewport area (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items)
    bl_region_type = "UI"  # Sidebar region (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items)
    bl_category = 'Mobo' # found in the Sidebar
    bl_label = "Mobo Scripts" # found at the top of the Panel
    bl_idname = "PT_MoboPanel"
    

    def draw(self, context):
        """define the layout of the panel"""
        layout = self.layout

        row = layout.row(align=True)
        row.operator("cat.rename_mesh", text="Rename Mesh Objects")

        self.layout.separator()

        row = layout.row(align=True)
        row.operator("cat.delete_all", text="Delete Coll Objects Mesh Mat")




classes = (
    CAT_OT_RenameMeshOperator,
    WIEW3D_PT_MoboPanel,
    CAT_OT_DeletAllOperator,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    


if __name__ == "__main__":
    register()



    







    