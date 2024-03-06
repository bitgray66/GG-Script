bl_info = {
    "name": "Mobo Custom Panel",
    "author": "Luigi Marazzi",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D Viewport > Sidebar > Mobo",
    "description": "Mobo setting panel",
    "category": "Development",
}


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
    bl_idname = "cat.delete_all"

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


    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Mobo'
    bl_label = "Mobo Scripts"
    bl_idname = "PT_MoboPanel"
    

    def draw(self, context):
        """define the layout of the panel"""
        layout = self.layout

        row = layout.row(align=True)
        row.operator("cat.rename_mesh", text="Rename eMsh Objects")

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



    







    