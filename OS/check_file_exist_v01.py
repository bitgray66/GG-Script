import os
import time

def trova_file(master_folder, estensioni_cercate, output_file):
    with open(output_file, 'w') as file_output:
        # Variabile per tenere traccia del numero progressivo
        numero_progressivo = 1
        # Ciclo che scorre tutti i file nella cartella master e nelle sue sottocartelle
        for cartella_padre, cartelle, files in os.walk(master_folder):
            for nome_file in files:
                nome_completo_file = os.path.join(cartella_padre, nome_file)
                estensione = os.path.splitext(nome_completo_file)[1].lower()
                if estensione in estensioni_cercate:
                    # Scrive il numero progressivo, il nome del file e il percorso completo nel file di output
                    #file_output.write(f"{numero_progressivo}\t{nome_file}\t{nome_completo_file}\n")
                    file_output.write(f"{numero_progressivo}\t{nome_file}\n")
                    # Incrementa il numero progressivo per la prossima riga
                    numero_progressivo += 1

# Cartella master
cartella_master = r"D:\PRP"

# Estensioni da cercare
estensioni_cercate = {'.ma', '.fbx', '.blend'}

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