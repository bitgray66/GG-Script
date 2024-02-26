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

    bl_label = "scene nome" # found at the top of the Panel
    bl_idname = "boo.add_scene_name" # found at the top of the Panel

    def execute(self, context):
        startPath = bpy.context.scene.render.filepath
        print(startPath)
        sceneName = bpy.path.basename(bpy.data.filepath) #bpy.path.basename(bpy.context.blend_data.filepath)
        sceneName = os.path.splitext(sceneName)[0] #replace('.blend', '')
        print(sceneName)
        finalPath = os.path.join("//", sceneName, filename + "_")
    
    
    
    
    
    
        bpy.context.scene.render.filepath = finalPath
    
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
        row.operator("boo.del_scene_name", text="Del SceneName")

        """ row = layout.row()
        row.prop(context.scene, "my_material_name")
        
        row = layout.row()
        row.operator("object.create_material_operator") """




def register():
    bpy.utils.register_class(VIEW3D_PT_mobo_panel)
    bpy.utils.register_class(CAT_PT_add_scene_name)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_mobo_panel)
    bpy.utils.unregister_class(CAT_PT_add_scene_name)

if __name__ == "__main__":
    register()
    







    