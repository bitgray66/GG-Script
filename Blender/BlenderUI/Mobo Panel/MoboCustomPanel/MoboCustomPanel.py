import bpy

class CAT_OT_RenameDataOperator(bpy.types.Operator):

    bl_label = "Rename Data"
    bl_idname = "cat.rename_data"

    def execute(self, context):
        
        MoboType = ['CURVE', 'MESH', 'CAMERA', 'CURVE', 'LIGHT', 'GPENCIL', 'META', 'VOLUME', 'FONT', 'SPEAKER', 'LATTICE', 'ARMATURE', 'LIGHT_PROBE', 'CURVES' ]

        for obj in bpy.context.selected_objects:
            if obj.type in MoboType:
                obj.data.name = obj.name

        return {"FINISHED"}
    

class CAT_OT_DeletAllOrphan(bpy.types.Operator):

    bl_label = "Delete Orphan"
    bl_idname = "cat.delate_orphan"

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

        layout = self.layout

        row = layout.row(align=True)
        row.operator("cat.rename_data", text="Rename Data")

        self.layout.separator()

        row = layout.row(align=True)
        row.operator("cat.delate_orphan", text="Delete Orphan")




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



    







    