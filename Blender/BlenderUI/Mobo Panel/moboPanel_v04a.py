bl_info = {
    "name": "Mobo Custom Panel",
    "author": "Luigi Marazzi",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D Viewport > Sidebar > Mobo",
    "description": "Mobo setting panel",
    "category": "Development",
}

import bpy


class CAT_OT_RenameMeshOperator(bpy.types.Operator):
    """Rename Mesh Objects"""
    bl_label = "Rename Mesh Objects"
    bl_idname = "cat.rename_mesh"

    def execute(self, context):
        selected_object = context.active_object
        selected_name = selected_object.name

        for obj in bpy.context.selected_objects:
            if obj.type in {'MESH', 'CURVE'}:
                obj.name = selected_name
                if obj.data:
                    obj.data.name = selected_name + "_Mesh"

        return {'FINISHED'}


class VIEW3D_PT_MoboPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mobo'
    bl_label = "Mobo Panel"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row(align=True)
        row.operator("cat.rename_mesh", text="Rename Mesh Objects")



classes = (
    CAT_OT_RenameMeshOperator,
    VIEW3D_PT_MoboPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.my_bool = bpy.props.BoolProperty(name="Sezione 01", default=True)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_bool


if __name__ == "__main__":
    register()
