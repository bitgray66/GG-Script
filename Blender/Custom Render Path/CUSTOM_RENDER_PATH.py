import bpy
import os

def get_file_directory_from_path(filepath):
    return os.path.dirname(bpy.path.abspath(filepath)) + os.path.sep

class ButtonPanel(bpy.types.Panel):
    bl_label = "Set Path Panel"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"

    def draw(self, context):
        layout = self.layout
        layout.operator("render.set_render_path_and_render")

class SetRenderPathThenRender(bpy.types.Operator):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "render.set_render_path_and_render"
    bl_label = "Set Render Path"

    def execute(self, context):
        context.scene.render.filepath = os.path.join(
            get_file_directory_from_path(
                context.scene.render.filepath
            ),
            bpy.context.scene.name + '.mp4'
        )
#        bpy.ops.render.render(animation=True)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ButtonPanel)
    bpy.utils.register_class(SetRenderPathThenRender)


def unregister():
    bpy.utils.unregister_class(SetRenderPathThenRender)
    bpy.utils.unregister_class(ButtonPanel)


if __name__ == "__main__":
    register()