import os
from PIL import Image


def converti_png_jpg(cartella):
#  Questa funzione converte tutti i file PNG in JPG all'interno di una cartella e le sue sottocartelle.
    n = 0
    for root, _, file_names in os.walk(cartella):
        for file_name in file_names:
            if file_name.endswith('.png'):
                # Ottieni il nome e l'estensione del file
                nome_file, estensione = os.path.splitext(file_name)
                # Crea il percorso del file JPG
                file_jpg = os.path.join(root, nome_file + '.jpg')
                n = n+1
                # Apri il file PNG e convertilo in JPG
                try:
                    immagine_png = Image.open(os.path.join(root, file_name))
                    immagine_jpg = immagine_png.convert('RGB')
                    immagine_jpg.save(file_jpg, 'JPEG')
                except Exception as e:
                    print(f"Errore durante la conversione di {file_name}: {e}")

    print(f"File convertiti {n} ")

if __name__ == '__main__':
    # Imposta il percorso della cartella da analizzare
    cartella_master = "D:\PRP\G\MM_PRP_Guitar_A_A\Tx\Hi"

    # Esegui la funzione di conversione
    converti_png_jpg(cartella_master)
