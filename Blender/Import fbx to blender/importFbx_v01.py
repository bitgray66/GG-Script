import bpy
import os
import time

# Definizione della classe operatore
class ConvertFBXOperator(bpy.types.Operator):
    # Identificatori univoci per l'operatore
    bl_idname = "wm.convert_fbx"
    bl_label = "Convert FBX Files"

    # Metodo chiamato quando l'operatore è eseguito
    def execute(self, context):
        # Cartella di origine dei file FBX
        folder_path = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'
        # Percorso del file di log
        log_file_path = os.path.join(folder_path, "processing_log.txt")

        # Inizializza il tempo di inizio
        start_time = time.time()

        # Apri il file di log per scrivere
        with open(log_file_path, "w") as log_file:
            log_file.write("Processing Log:\n")

            # Inizializza il conteggio dei file elaborati
            total_files = 0
            changed_files = 0
            failed_files = 0

            # Itera ricorsivamente attraverso i file nella cartella sorgente
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    # Controlla se il file è un file FBX
                    if file.lower().endswith(".fbx"):
                        total_files += 1
                        fbx_path = os.path.join(root, file)
                        # Ottieni il nome del file senza estensione
                        file_name = os.path.splitext(file)[0]

                        # Pulisci la scena
                        for obj in bpy.data.objects:
                            bpy.data.objects.remove(obj)

                        for mesh in bpy.data.meshes:
                            bpy.data.meshes.remove(mesh)

                        for coll in bpy.data.collections:
                            bpy.data.collections.remove(coll)

                        for mat in bpy.data.materials:
                            bpy.data.materials.remove(mat)

                        # Importa il file FBX
                        bpy.ops.import_scene.fbx(filepath=fbx_path)

                        # Effettua le operazioni aggiuntive
                        # In questo esempio, aggiungiamo una sfera
                        bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=(0, 0, 0))

                        add_principled_setup()  # Aggiungi il materiale Principled BSDF

                        bpy.ops.node.nw_add_textures_for_principled()














                        # Salva il file .blend nella stessa cartella del file FBX
                        blend_file_path = os.path.join(root, f"{file_name}_v01.blend")
                        bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)

                        # Aggiorna il file di log
                        changed_files += 1
                        log_file.write(f"{changed_files}\t{file_name}_v01.blend\n")

            # Scrivi il tempo totale impiegato per processare i file
            end_time = time.time()
            total_time = end_time - start_time
            log_file.write(f"\nTotal processing time: {total_time} seconds\n")

        # Stampa le informazioni
        self.report({'INFO'}, f"Total files {total_files} | Changed {changed_files} | Failed {failed_files}")
        return {'FINISHED'}


    def add_principled_setup():
        # Aggiungi il materiale Principled BSDF
        mat = bpy.data.materials.new(name="Principled_BSDF")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        principled_bsdf = nodes.get("Principled BSDF")

        # Assegna il materiale a tutti gli oggetti nella scena
        for obj in bpy.data.objects:
            if obj.type == 'MESH':
                obj.data.materials.clear()  # Rimuovi eventuali materiali esistenti
                obj.data.materials.append(mat)


# Registra la classe dell'operatore in Blender
bpy.utils.register_class(ConvertFBXOperator)

# Esegui l'operatore
bpy.ops.wm.convert_fbx()
