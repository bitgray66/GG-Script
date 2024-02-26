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
        row = layout.row()
        col =layout.column()
        props = bpy.context.scene.eevee.taa_samples
        col.prop(props, "taa_samples", text="Viewport")
        row.label(text="prova")
        layout.operator("render.set_render_path_and_render")

class SetRenderPathThenRender(bpy.types.Operator):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "render.set_render_path_and_render"
    bl_label = "Set Render Path"

    def execute(self, context):
        basePath = "R:/Melody_Momon/Production/Assets/RenderLayers/RenderAssets/PRP/"
        print(basePath)
        path = bpy.path.basename(bpy.context.blend_data.filepath)
        fileName = path[:-6]
        cam = bpy.context.scene.camera.name
        bpy.context.scene.render.filepath = os.path.join(basePath +'/'+ fileName +'/')
        """ gigi = '{file}_{scene}_{camera}_####'.format(
            file=bpy.data.filepath.rpartition('.')[0],
            scene=bpy.scene.name,
            camera=bpy.scene.camera.name,
            ) """

        return {'FINISHED'}

def register():
    bpy.utils.register_class(ButtonPanel)
    bpy.utils.register_class(SetRenderPathThenRender)


def unregister():
    bpy.utils.unregister_class(SetRenderPathThenRender)
    bpy.utils.unregister_class(ButtonPanel)


if __name__ == "__main__":
    register()



    
def render_filepath_set(scene):
    scene.render.filepath = '{file}_{scene}_{camera}_####'.format(
            file=bpy.data.filepath.rpartition('.')[0],
            scene=scene.name,
            camera=scene.camera.name,
            )
    
bpy.app.handlers.render_init.append(render_filepath_set)