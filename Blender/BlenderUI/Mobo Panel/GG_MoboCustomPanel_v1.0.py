# give Python access to Blender's functionality
from typing import Set
import bpy
import os
from bpy.types import Context



class CAT_OT_RenameDataOperator(bpy.types.Operator):
    # Rename all data from selected Coll with same name of the
    bl_label = "Rename Data" # found at the top of the Panel
    bl_idname = "cat.rename_data"   # found at the top of the Panel

    def execute(self, context):
        
        MoboType = ['CURVE', 'MESH', 'CAMERA', 'CURVE', 'LIGHT', 'GPENCIL', 'META', 'VOLUME', 'FONT', 'SPEAKER', 'LATTICE', 'ARMATURE', 'LIGHT_PROBE', 'CURVES' ]

        for obj in bpy.context.selected_objects:
            if obj.type in MoboType:
                obj.data.name = obj.name

        return {"FINISHED"}
    

class CAT_OT_DeletAllOrphan(bpy.types.Operator):
    # Delete Orphan
    bl_label = "Delete Orphan"
    bl_idname = "cat.delete_orphan"

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
        # define the layout of the panel
        layout = self.layout

        row = layout.row(align=True)
        row.operator("cat.rename_data", text="Rename Data")

        self.layout.separator()

        row = layout.row(align=True)
        row.operator("cat.delete_orphan", text="Delete Orphan")




classes = (
    CAT_OT_RenameDataOperator,
    WIEW3D_PT_MoboPanel,
    CAT_OT_DeletAllOrphan,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    


if __name__ == "__main__":
    register()



    







    