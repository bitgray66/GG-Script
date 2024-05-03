import os
from PIL import Image


def converti_png_jpg(cartella):

    n = 0
    for root, _, file_names in os.walk(cartella):
        for file_name in file_names:
            if file_name.endswith('.png'):

                nome_file, estensione = os.path.splitext(file_name)

                file_jpg = os.path.join(root, nome_file + '.jpg')
                print(f"convertito {file_jpg} ")
                n = n+1

                try:
                    immagine_png = Image.open(os.path.join(root, file_name))
                    immagine_jpg = immagine_png.convert('RGB')
                    immagine_jpg.save(file_jpg, 'JPEG')
                except Exception as e:
                    print(f"Errore durante la conversione di {file_name}: {e}")

    print(f"File convertiti {n} ")

if __name__ == '__main__':

    cartella_master = "D:\\PRP"


    converti_png_jpg(cartella_master)
