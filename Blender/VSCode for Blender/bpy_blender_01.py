import bpy




bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

bpy.ops.mesh.primitive_cube_add(size=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

cube_obj = bpy.context.active_object

loc= cube_obj.location

cube_obj.location.x =5
cube_obj.location.y =5
cube_obj.location.z =5


