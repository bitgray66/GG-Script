bl_info = {
    "name": "Mobo Custom Panel",
    "author": "Luigi Marazzi",
    "version": (1, 1, 0),
    "blender": (4, 1, 0),
    "location": "3D Viewport > Sidebar > Mobo",
    "description": "Mobo setting panel",
    "category": "Development",
}

import bpy

from .MoboCustomPanel import CAT_OT_RenameDataOperator, VIEW3D_PT_MoboPanel, CAT_OT_DeletAllOrphan, CAT_OT_Override

classes = (
    CAT_OT_RenameDataOperator,
    CAT_OT_DeletAllOrphan,
    CAT_OT_Override,
    VIEW3D_PT_MoboPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
