import os
import time

def trova_file(master_folder, estensioni_cercate, output_file):
    with open(output_file, 'w') as file_output:
        # Variabile per tenere traccia del numero progressivo
        numero_progressivo = 1
        # Ciclo che scorre tutti i file nella cartella master e nelle sue sottocartelle
        for cartella_padre, cartelle, files in os.walk(master_folder):
            for nome_file in files:
                if nome_file.endswith('.ma'):
                    # Verifica se esiste un file .fbx o .blend con lo stesso nome nella stessa cartella
                    nome_base = os.path.splitext(nome_file)[0]
                    fbx_file = os.path.join(cartella_padre, nome_base + '.fbx')
                    blend_file = os.path.join(cartella_padre, nome_base + '.blend')
                    fbx_exist = os.path.exists(fbx_file)
                    blend_exist = os.path.exists(blend_file)
                    # Scrive il numero progressivo, i segnaposti e il nome del file nel file di output
                    segnaposto_primo = 'F' if fbx_exist else '-'
                    segnaposto_secondo = 'B' if blend_exist else '-'
                    file_output.write(f"{numero_progressivo}\t{segnaposto_primo}\t{segnaposto_secondo}\t{nome_file}\n")
                    # Incrementa il numero progressivo per la prossima riga
                    numero_progressivo += 1

# Cartella master
cartella_master = r"D:\PRP"

# Estensioni da cercare
estensioni_cercate = {'.ma'}

# Nome del file di output
file_output = "elenco_file_esistenti.txt"

# Percorso completo del file di output
percorso_file_output = os.path.join(cartella_master, file_output)

# Misura il tempo di inizio dell'intero script
start_time = time.time()

# Trova i file e scrivi l'elenco nel file di output
trova_file(cartella_master, estensioni_cercate, percorso_file_output)

# Misura il tempo di fine dell'intero script
end_time = time.time()

# Calcola il tempo totale trascorso
tempo_totale = end_time - start_time

print("Finito! L'elenco dei file è stato salvato in", percorso_file_output)
print("Tempo totale impiegato:", tempo_totale, "secondi")
