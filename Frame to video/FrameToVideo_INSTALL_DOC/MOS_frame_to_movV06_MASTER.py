import cmd
import os
import cv2
import subprocess as sp
import time

cartella_P = input('Inserire il nome della cartella principale: ')
cartella_P = cartella_P.upper()

if cartella_P=='BLD' or cartella_P=='CH' or cartella_P=='ENV' or cartella_P=='FL' or cartella_P=='GRD' or cartella_P=='PR' :

    print('\n')
    target = input('SE LE CARTELLE SONO TUTTE TUE !!! Inserire T altrimenti si prega di inserire il nome della singola cartella per il mov : ')
    print('\n')

    if target == 'T' or target == 't':
        
        source_path = 'R:\mini_eroi\Production\Assets\RenderLayers\Library\\'+cartella_P+'\\'
        #print(' source_path2-> '+source_path)
        out_path = 'R:\mini_eroi\Library\MovJpg_Nimbus\\'
        #print(' target2-> '+target)
        os.chdir(source_path)

        sources = os.listdir(os.getcwd()) 

        for source in sources:
            print(' source-> '+source)
            a = source[-3:]
           
            if a == '_MD' or a == '_TX':
                
                path = source_path + source +'//' 
                
                pre_imgs = os.listdir(path) 
                out_video_name = pre_imgs[0][:-6]
                out_video_ext = 'mp4'
                out_video_full_path = out_path+out_video_name+out_video_ext

                img = []

                for i in pre_imgs:
                    i = path+i
                    img.append(i)

                cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                frame =cv2.imread(img[0])  

                size = list(frame.shape)
                del size[2]
                size.reverse()
                
                video = cv2.VideoWriter(out_video_full_path, cv2_fourcc, 24, size ) 

                for i in range(len(img)):
                    video.write(cv2.imread(img[i]))

                video.release()

                time.sleep(2)
                new_video_ext = 'mov'
                new_out_video_full_path = out_path+out_video_name+new_video_ext
                
                os.system(f'ffmpeg -i ' + out_video_full_path + ' -f mov '+ new_out_video_full_path)
                os.remove(out_video_full_path)
                print('\n')
                print('creato ' +source+ '.mov in ', out_path[:-1])

            else :

                print('La cartella non è valida')


    else :

        source_path = 'R:\mini_eroi\Production\Assets\RenderLayers\Library\\'+cartella_P+'\\'
        #print(' source_path2-> '+source_path)
        out_path = 'R:\mini_eroi\Library\MovJpg_Nimbus\\'       
        #print(' target2-> '+target)
        os.chdir(source_path)

        a = target[-3:]
        b = target[0:3]
        #print(' a-> '+a)
        #print(' b-> '+b)

        if a == '_MD' or a == '_TX' and b == 'ME_':
            
            path = source_path + target +'//' 
            
            pre_imgs = os.listdir(path) 
            out_video_name = pre_imgs[0][:-6]
            out_video_ext = 'mp4'
            out_video_full_path = out_path+out_video_name+out_video_ext
            
            img = []

            for i in pre_imgs:
                i = path+i
                img.append(i)

            cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            frame =cv2.imread(img[0])  

            size = list(frame.shape)
            del size[2]
            size.reverse()
            
            video = cv2.VideoWriter(out_video_full_path, cv2_fourcc, 24, size ) 

            for i in range(len(img)):
                video.write(cv2.imread(img[i]))

            video.release()

            time.sleep(2)
            new_video_ext = 'mov'
            new_out_video_full_path = out_path+out_video_name+new_video_ext
            
            
            os.system(f'ffmpeg -i ' + out_video_full_path + ' -f mov '+ new_out_video_full_path)
            os.remove(out_video_full_path)
            print('\n')
            print('creato' +target+ '.mov in ', out_path[:-1])

        else :

            print('La cartella '+target+' non esiste o non è valida')   


else :
    print('La cartella principale '+cartella_P+' non è valida')



       