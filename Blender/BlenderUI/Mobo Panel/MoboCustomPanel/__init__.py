bl_info = {
    "name": "Mobo Custom Panel",
    "author": "Luigi Marazzi",
    "version": (0, 1, 0),
    "blender": (5, 0, 1),
    "location": "3D Viewport > Sidebar > Mobo",
    "description": "Mobo setting panel",
    "category": "Development",
}

import bpy

from .MoboCustomPanel import CAT_OT_RenameDataOperator, WIEW3D_PT_MoboPanel, CAT_OT_DeletAllOrphan

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
