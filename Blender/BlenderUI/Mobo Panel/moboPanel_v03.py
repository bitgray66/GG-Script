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


class CAT_PT_add_scene_name(bpy.types.Operator):
    """"Setting the render output path"""

    bl_label = "scene label" # found at the top of the Panel
    bl_idname = "boo.add_scene_name" # found at the top of the Panel

    def execute(self, context):
        startPath = bpy.context.scene.render.filepath
        print(startPath)
        basePath = "R:\Melody_Momon\Production\Assets\RenderLayers\RenderAssets\PRP"
        print(basePath)
        path = bpy.path.basename(bpy.context.blend_data.filepath)
        fileName = path[:-6]
        bpy.context.scene.render.filepath = os.path.join(basePath +'/'+ fileName +'/')
        return {"FINISHED"}
    
class CAT_PT_add_camera_name(bpy.types.Operator):
    """"Setting the render output path"""

    bl_label = "camera label" # found at the top of the Panel
    bl_idname = "boo.add_camera_name" # found at the top of the Panel

    def execute(self, context):
        startPath = bpy.context.scene.render.filepath
        bpy.context.scene.render.filepath = os.path.join(startPath+'/'+bpy.context.scene.camera.name)
        return {"FINISHED"}
    
class CAT_PT_add_camera_name(bpy.types.Operator):
    """"Setting the render output path"""

    bl_label = "file label" # found at the top of the Panel
    bl_idname = "boo.add_file_name" # found at the top of the Panel

    def execute(self, context):
        startPath = bpy.context.scene.render.filepath
        bpy.context.scene.render.filepath = os.path.join(startPath+'/'+bpy.context.scene.camera.name)
        return {"FINISHED"}

class CAT_PT_reset(bpy.types.Operator):
    """"Setting the render output path"""

    bl_label = "reset label" # found at the top of the Panel
    bl_idname = "boo.reset" # found at the top of the Panel

    def execute(self, context):
        bpy.context.scene.render.filepath = "\\"
        return {"FINISHED"}



class VIEW3D_PT_mobo_panel(bpy.types.Panel):

    # where to add the panel in the UI
    bl_space_type = "VIEW_3D"  # 3D Viewport area (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items)
    bl_region_type = "UI"  # Sidebar region (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items)
   
    bl_category = 'Mobo' # found in the Sidebar
    bl_label = "Render Path" # found at the top of the Panel
    bl_idname = "PT_MoboPanel"
    

    def draw(self, context):
        """define the layout of the panel"""
        layout = self.layout

        row = self.layout.row()
        row.operator("mesh.primitive_cube_add", text="Add Cube")

        self.layout.separator()

        row = layout.row()
        row.operator("boo.add_scene_name", text="Add SceneName")

        row = layout.row()
        row.operator("boo.add_camera_name", text="Add CameraName")

        row = layout.row()
        row.operator("boo.reset", text="Reset")





def register():
    bpy.utils.register_class(VIEW3D_PT_mobo_panel)
    bpy.utils.register_class(CAT_PT_add_scene_name)
    bpy.utils.register_class(CAT_PT_add_camera_name)
    bpy.utils.register_class(CAT_PT_reset)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_mobo_panel)
    bpy.utils.unregister_class(CAT_PT_add_scene_name)
    bpy.utils.unregister_class(CAT_PT_add_camera_name)
    bpy.utils.unregister_class(CAT_PT_reset)

if __name__ == "__main__":
    register()
    







    