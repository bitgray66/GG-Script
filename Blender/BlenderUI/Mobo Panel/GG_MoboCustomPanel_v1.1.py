# Importa i moduli necessari
from typing import Set
import bpy
import os
from bpy.types import Context
import ast  # Importa il modulo ast per la conversione sicura delle stringhe in strutture Python

# Operatore per rinominare tutti i dati degli oggetti selezionati con lo stesso nome dell'oggetto
class CAT_OT_RenameDataOperator(bpy.types.Operator):
    bl_label = "Rename Data"  # Etichetta visualizzata nel pannello
    bl_idname = "cat.rename_data"  # Identificatore univoco per l'operatore

    def execute(self, context):
        # Elenco dei tipi di oggetto di cui rinominare i dati
        MoboType = [
            'CURVE', 'MESH', 'CAMERA', 'CURVE', 'LIGHT',
            'GPENCIL', 'META', 'VOLUME', 'FONT', 'SPEAKER',
            'LATTICE', 'ARMATURE', 'LIGHT_PROBE', 'CURVES'
        ]

        # Ciclo attraverso gli oggetti selezionati
        for obj in bpy.context.selected_objects:
            if obj.type in MoboType:
                obj.data.name = obj.name  # Rinomina i dati per farli corrispondere al nome dell'oggetto

        return {"FINISHED"}

# Operatore per eliminare tutti i dati orfani
class CAT_OT_DeletAllOrphan(bpy.types.Operator):
    bl_label = "Delete Orphan"  # Etichetta visualizzata nel pannello
    bl_idname = "cat.delete_orphan"  # Identificatore univoco per l'operatore

    def execute(self, context):
        # Rimuove tutti gli oggetti
        for obj in bpy.data.objects:
            bpy.data.objects.remove(obj, do_unlink=True)

        # Rimuove tutte le mesh
        for mesh in bpy.data.meshes:
            bpy.data.meshes.remove(mesh, do_unlink=True)

        # Rimuove tutte le collezioni
        for coll in bpy.data.collections:
            bpy.data.collections.remove(coll)

        # Rimuove tutti i materiali
        for mat in bpy.data.materials:
            bpy.data.materials.remove(mat, do_unlink=True)

        return {"FINISHED"}

# Operatore per sovrascrivere collezioni, oggetti, dati e materiali
class CAT_OT_Override(bpy.types.Operator):
    bl_label = "Override Obj"  # Etichetta visualizzata nel pannello
    bl_idname = "cat.over_objects"  # Identificatore univoco per l'operatore

    @staticmethod
    def get_list_selected():
        # Restituisce un elenco di oggetti selezionati e le loro posizioni
        try:
            list_selected = bpy.context.selected_objects
            selected_col = [o.name for o in list_selected]

            list_location = [obj.location for obj in list_selected]

            return selected_col, list_location
        except Exception as e:
            print(f"Errore in get_list_selected: {e}")
            return [], []

    @staticmethod
    def override_collections(selected_col):
        # Sovrascrive le collezioni degli oggetti selezionati
        for obj in selected_col:
            try:
                col = bpy.data.objects.get(obj)
                if col:
                    bpy.context.view_layer.objects.active = col
                    bpy.ops.object.make_override_library()
                    print(f"Override eseguito per l'oggetto: {obj}")
                else:
                    print(f"Oggetto non trovato: {obj}")
            except Exception as e:
                print(f"Errore in override_collections per l'oggetto {obj}: {e}")

    @staticmethod
    def get_list_prefixes(selected_col):
        # Restituisce un elenco di prefissi degli oggetti selezionati
        try:
            list_prefixes = [item.replace('_COL', '') for item in selected_col]
            return list_prefixes
        except Exception as e:
            print(f"Errore in get_list_prefixes: {e}")
            return []

    @staticmethod
    def reselect_objects(list_prefixes):
        # Riseleziona gli oggetti in base ai prefissi forniti
        try:
            meshes = bpy.data.meshes
            for mesh in meshes:
                mesh_name = mesh.name
                for prefix in list_prefixes:
                    if mesh_name.startswith(prefix):
                        obj = bpy.data.objects.get(mesh_name)
                        if obj:
                            obj.select_set(True)
                            bpy.context.view_layer.objects.active = obj
                        else:
                            print(f"Oggetto non trovato: {mesh_name}")
            return meshes
        except Exception as e:
            print(f"Errore in reselect_objects: {e}")
            return []

    @staticmethod
    def override_selected_object():
        # Sovrascrive gli oggetti selezionati
        try:
            selected_objects = bpy.context.selected_objects
            for obj in selected_objects:
                obj = bpy.data.objects.get(obj.name)
                if obj:
                    bpy.context.view_layer.objects.active = obj
                    bpy.ops.object.make_override_library()
                    print(f"Override eseguito per l'oggetto: {obj.name}")
                else:
                    print(f"Oggetto non trovato: {obj.name}")
        except Exception as e:
            print(f"Errore in override_selected_object: {e}")

    @staticmethod
    def relocate_objects(prefix_location):
        # Rilocazione degli oggetti in base ai prefissi e alle posizioni fornite
        try:
            ob_selected = bpy.context.selected_objects
            for ob in ob_selected:
                ob_name = ob.name
                for key in prefix_location:
                    if ob_name.startswith(key):
                        obj = bpy.data.objects.get(ob_name)
                        if obj:
                            bpy.context.view_layer.objects.active = obj
                            val = prefix_location[key]
                            
                            try:
                                val_tuple = ast.literal_eval(val)
                                if isinstance(val_tuple, tuple) and len(val_tuple) == 3:
                                    obj.location = val_tuple
                                    print(f"Oggetto {obj.name} spostato a {val_tuple}")
                                else:
                                    print(f"Formato posizione non valido per {val}: deve essere una tupla di tre valori.")
                            except (ValueError, SyntaxError) as ve:
                                print(f"Errore nella conversione di {val} in una tupla: {ve}")
                        else:
                            print(f"Oggetto non trovato: {ob_name}")
        except Exception as e:
            print(f"Errore in relocate_objects: {e}")

    def execute(self, context):
        # Funzione principale di esecuzione dell'operatore
        try:
            selected_col, list_location = self.get_list_selected()

            list_position = [str(loc)[8:-1] for loc in list_location]

            self.override_collections(selected_col)

            list_prefixes = self.get_list_prefixes(selected_col)

            self.reselect_objects(list_prefixes)

            self.override_selected_object()

            prefix_location = {list_prefixes[i]: list_position[i] for i in range(len(list_prefixes))}

            self.relocate_objects(prefix_location)
        except Exception as e:
            print(f"Errore nell'esecuzione principale: {e}")

        return {"FINISHED"}

# Classe del pannello per visualizzare gli operatori nella Vista 3D
class VIEW3D_PT_MoboPanel(bpy.types.Panel):  # Cambia il nome della classe per conformarsi alle convenzioni di denominazione di Blender
    bl_space_type = "VIEW_3D"  # Posizione del pannello nella Vista 3D
    bl_region_type = "UI"  # Regione del pannello (Sidebar)
    bl_category = 'Mobo'  # Categoria del pannello nella Sidebar
    bl_label = "Mobo Scripts"  # Etichetta del pannello
    bl_idname = "VIEW3D_PT_MoboPanel"  # Assicurati che idname corrisponda al nome della classe

    def draw(self, context):
        layout = self.layout

        # Prima riga con due pulsanti
        row = layout.row(align=True)
        row.operator("cat.rename_data", text="Rename Data")
        row.separator()  # Aggiungi un separatore per creare spazio tra i pulsanti
        row.operator("cat.delete_orphan", text="Delete Orphan")

        # Aggiungi spazio tra le righe
        layout.separator()
        
        # Seconda riga con due nuovi pulsanti
        row = layout.row(align=True)
        row.operator("cat.over_objects", text="Override OBJ")
        row.separator()  # Aggiungi un separatore per creare spazio tra i pulsanti
        #row.operator("cat.another_action", text="Another Action")

# Registra le classi
classes = (
    CAT_OT_RenameDataOperator,
    CAT_OT_DeletAllOrphan,
    CAT_OT_Override,
    VIEW3D_PT_MoboPanel,  # Assicurati che il nome della classe sia corretto qui
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

# Registra l'addon quando lo script viene eseguito
if __name__ == "__main__":
    register()
