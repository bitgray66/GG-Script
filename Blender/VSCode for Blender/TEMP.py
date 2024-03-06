import os

def find_textures(file_name, texture_folder):
    # Lista dei suffissi da cercare
    suffices = ['_DIF', '_NRM', '_RGH']

    # Ottieni il prefisso del nome del file
    prefix = file_name
    print('prefix  =', prefix)

    # Lista dei file trovati
    matching_files = []

    # Funzione per trovare i file con il prefisso specificato nella cartella specificata
    def find_matching_files_with_prefix(folder, prefix):
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.startswith(prefix):
                    matching_files.append(os.path.join(root, file))

    # Trova tutti i file con il prefisso specificato
    find_matching_files_with_prefix(texture_folder, prefix)

    # Lista dei path delle texture corrispondenti
    return matching_files

# Esempio di utilizzo
file_name = 'MM_PRP_AlarmClock_A_A'
texture_folder = 'C:\\Users\\luigi.marazzi\\Desktop\\PRP'

matching_textures = find_textures(file_name, texture_folder)

print("File trovati per '{}':".format(file_name))
for file_path in matching_textures:
    tipo = file_path[-8:-4]  # Prendi gli ultimi 4 caratteri prima dell'estensione (.png)
    if tipo == '_DIF':
        print("A:", file_path)
    elif tipo == '_RGH':
        print("B:", file_path)
    elif tipo == '_NRM':
        print("C:", file_path)
