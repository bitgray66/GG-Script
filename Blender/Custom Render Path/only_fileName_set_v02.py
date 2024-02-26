import bpy
import os

scene= bpy.context.scene

def render_filepath_set(scene):
    scene.render.filepath = '{file}_{scene}_{camera}_####'.format(
            file=bpy.data.filepath.rpartition('.')[0],
            scene=scene.name,
            camera=scene.camera.name,
            )
    
bpy.app.handlers.render_init.append(render_filepath_set)