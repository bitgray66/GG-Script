import bpy
import os
import time

from bpy_extras.node_shader_utils import PrincipledBSDFWrapper
from bpy_extras.image_utils import load_image




class ConvertFBXOperator(bpy.types.Operator):

    bl_idname = "wm.convert_fbx"
    bl_label = "Convert FBX Files"


    def execute(self, context):

        folder_path = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'

        log_file_path = os.path.join(folder_path, "processing_log.txt")


        start_time = time.time()


        with open(log_file_path, "w") as log_file:
            log_file.write("Processing Log:\n")


            total_files = 0
            changed_files = 0
            failed_files = 0


            for root, dirs, files in os.walk(folder_path):
                for file in files:

                    if file.lower().endswith(".fbx"):
                        total_files += 1
                        fbx_path = os.path.join(root, file)

                        file_name = os.path.splitext(file)[0]
                        print('file_name =', file_name)


                        for obj in bpy.data.objects:
                            bpy.data.objects.remove(obj)

                        for mesh in bpy.data.meshes:
                            bpy.data.meshes.remove(mesh)

                        for coll in bpy.data.collections:
                            bpy.data.collections.remove(coll)

                        for mat in bpy.data.materials:
                            bpy.data.materials.remove(mat)


                        bpy.ops.import_scene.fbx(filepath=fbx_path)




                        





                        bpy.ops.wm.empty_to_collection()


































                        texture_folder = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'

                        def find_textures(file_name, texture_folder):

                            suffices = ['_DIF', '_NRM', '_RGH']


                            prefix = file_name
                            print('prefix  =', prefix)


                            matching_files = []


                            def find_matching_files_with_prefix(folder, prefix):
                                for root, dirs, files in os.walk(folder):
                                    for file in files:
                                        if file.startswith(prefix):
                                            matching_files.append(os.path.join(root, file))


                            find_matching_files_with_prefix(texture_folder, prefix)


                            return matching_files



                        def create_asset_material(file_name):

                            matching_textures = find_textures(file_name, texture_folder)

                            for file_path in matching_textures:
                                print(file_path)


                            material_name = file_name+'_MAT'


                            mat = bpy.data.materials.new(name=material_name)


                            mat.diffuse_color = (0.8, 0.2, 0.2, 1)

                            mat.use_nodes = True
                            nodescale = 300
                            principled = PrincipledBSDFWrapper(mat, is_readonly=False)
                            principled.base_color = (0.8, 0.8, 0.5)

                            print("File trovati per '{}':".format(file_name))

                            for file_path in matching_textures:
                                tipo = file_path[-8:-4]
                                if tipo == '_DIF':
                                    print("_DIF:", file_path)
                                    principled.base_color_texture.image = load_image(file_path) 
                                elif tipo == '_RGH':
                                    print("_RGH:", file_path)
                                    principled.roughness_texture.image = load_image(file_path) 
                                elif tipo == '_NRM':
                                    print("_NRM:", file_path)
                                    principled.normalmap_texture.image = load_image(file_path) 

                            bpy.data.materials["MM_PRP_AlarmClock_A_A_MAT"].node_tree.nodes["Principled BSDF"].label = material_name

                                    

                            return mat




                        mat = create_asset_material(file_name)


                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.ops.object.select_by_type(type='MESH')


                        for obj in bpy.context.selected_objects:
                            obj.data.materials.clear()
                            obj.data.materials.append(mat)












                    








                        blend_file_path = os.path.join(root, f"{file_name}.blend")
                        bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)



                        coll_for_asset = file_name+'_COL'
                        print('coll_for_asset =', coll_for_asset)
                        bpy.data.collections[coll_for_asset].asset_mark()



                        blend_file_path = os.path.join(root, f"{file_name}_marked.blend")
                        bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)

                        

                        


                        changed_files += 1
                        log_file.write(f"{changed_files}\t{file_name}_v01.blend\n")


            end_time = time.time()
            total_time = end_time - start_time
            log_file.write(f"\nTotal processing time: {total_time} seconds\n")


        self.report({'INFO'}, f"Total files {total_files} | Changed {changed_files} | Failed {failed_files}")
        return {'FINISHED'}






class ConvertEmptyToCollectionOperator(bpy.types.Operator):

    bl_idname = "wm.empty_to_collection"
    bl_label = "Convert Empty to Collection"


    def execute(self, context):
        print('@@@@@@@@@@@@@@@@@@@@@@@@')


        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


        bpy.ops.object.select_all(action='DESELECT')
        

        if len(bpy.context.selected_objects):
            objects = bpy.context.selected_objects
        else:
            objects = get_scene_children()

        for o in objects:

            if len(o.users_collection):
                parent_collection = o.users_collection[0]
            else:
                parent_collection = bpy.context.scene.collection

            self.empties_to_collections(o, parent_collection)
        

        self.create_geo_collection()
        

        bpy.ops.object.select_all(action='SELECT')


        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        

        for ch_col in bpy.context.scene.collection.children:
            print(ch_col)
            suffix = '_COL'
            suffixNo = '_GEO_COL'
            scene_collection = bpy.context.scene.collection
            if  ch_col.name.endswith(suffixNo):
                print('ch_col =', ch_col.name)
                nameGeoCol = ch_col.name[:-8]
                print('nameGeoCol =', nameGeoCol)
                nameCol = nameGeoCol+'_COL'
                print('nameCol =', nameCol)
            elif ch_col.name.endswith(suffix):
                print('IF = OUT')
                scene_collection.children.unlink(ch_col)
        
        return {'FINISHED'}


    def empties_to_collections(self, o, parent_collection):
        children = get_objects_children(o)

        if hasattr(o, 'type') and o.type == 'EMPTY':
            o.name = o.name.replace("_GRP", "_COL")

            new_collection = bpy.data.collections.new(o.name)
            parent_collection.children.link(new_collection)

            for ch in o.children_recursive:
                for old_collection in ch.users_collection:
                    old_collection.objects.unlink(ch)
                new_collection.objects.link(ch)
            bpy.data.objects.remove(o)

            for ch in children:
                self.empties_to_collections(ch, new_collection)
        else:

            for ch in children:
                self.empties_to_collections(ch, parent_collection)
                

    def create_geo_collection(self):

        master_collection = self.find_master_collection()
        if not master_collection:
            self.report({'ERROR'}, "Non è stata trovata una collezione principale.")
            return {'CANCELLED'}
        

        new_collection_name = master_collection.name.replace("_COL", "_GEO_COL")
        new_collection = bpy.data.collections.new(new_collection_name)
        

        bpy.context.collection.children.link(new_collection)
        

        self.move_collection(master_collection, new_collection)
    

    def find_master_collection(self):
        for collection in bpy.context.scene.collection.children:
            if collection.objects:
                return collection
        return None
    

    def move_collection(self, src_collection, dst_collection):

        dst_collection.children.link(src_collection)



    

def get_objects_children(obj):
    obs = []
    if hasattr(obj, 'children'):
        obs.extend(obj.children)
    if hasattr(obj, 'objects'):
        obs.extend(obj.objects)
    return obs


def get_scene_children():
    """List of the 'Scene' collection's children."""
    children = []
    for o in bpy.data.objects:
        if hasattr(o, 'parent') and o.parent is None:
            children.append(o)
    return children



bpy.utils.register_class(ConvertFBXOperator)
bpy.utils.register_class(ConvertEmptyToCollectionOperator)


bpy.ops.wm.convert_fbx()
