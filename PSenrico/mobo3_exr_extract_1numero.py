import os, shutil


source = input('Inserire il nome della cartella principale')
print('cartella principale-> '+source)


numExtraFolder = input('Oltre a Beauty e Bg esiste un\'altra cartella da considerare ? 1 = si 0 = no')
extraFolder1 = 'nessuna' # PortieraAperta
if numExtraFolder=='1' :
    extraFolder1 = input('Inserire il nome della cartella extra')


os.chdir(source)  #originale Render2

path = os.getcwd()

parent = os.path.abspath(os.path.join(path, os.pardir))


os.makedirs('../PSmaster', exist_ok=True)



dirList = []
dirList = os.listdir()

for dir in dirList:
    
    dirSuf = (dir[16:]) 
    

    fList = []
    fList = os.listdir(dir)
    

    if dirSuf=='Beauty' or dirSuf=='Bg' or dirSuf=='Piedistallo' or dirSuf=='PortieraAperta' or dirSuf=='Beauty_AO':
        dirName = (dir[:15])
        
        os.makedirs('../PSmaster/'+dirName, exist_ok=True)
        dirTarget = os.path.abspath(os.path.join(parent, 'PSmaster/'+dirName))
        

        for f in fList:
            
            fileSuf = (f[16:])
            
            fSuf = fileSuf[:-6]
            
            old_file = os.path.join(dir, f)
            
            match fSuf:
                case "Beauty":
                    new_file = os.path.join(dirTarget, 'beauty.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_maskGeo":
                    new_file = os.path.join(dirTarget, 'beauty_maskGeo.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_maskShd":
                    new_file = os.path.join(dirTarget, 'beauty_maskShd.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_utils":
                    new_file = os.path.join(dirTarget, 'beauty_utils.exr')
                    shutil.copy(old_file, new_file)
                case "Bg":
                    new_file = os.path.join(dirTarget, 'bg.exr')
                    shutil.copy(old_file, new_file)
                case "Bg_maskGeo":
                    new_file = os.path.join(dirTarget, 'bg_maskGeo.exr')
                    shutil.copy(old_file, new_file)
                case "Bg_maskShd":
                    new_file = os.path.join(dirTarget, 'bg_maskShd.exr')
                    shutil.copy(old_file, new_file)
                case "Bg_utils":
                    new_file = os.path.join(dirTarget, 'bg_utils.exr')
                    shutil.copy(old_file, new_file)
                case "PortieraAperta":
                    new_file = os.path.join(dirTarget, 'portieraaperta.exr')
                    shutil.copy(old_file, new_file)
                case "PortieraAperta_maskGeo":
                    new_file = os.path.join(dirTarget, 'portieraaperta_maskGeo.exr')
                    shutil.copy(old_file, new_file)
                case "PortieraAperta_maskShd":
                    new_file = os.path.join(dirTarget, 'portieraaperta_maskShd.exr')
                    shutil.copy(old_file, new_file)
                case "PortieraAperta_utils":
                    new_file = os.path.join(dirTarget, 'portieraaperta_utils.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_AO":
                    new_file = os.path.join(dirTarget, 'beauty_AO.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_AO_maskGeo":
                    new_file = os.path.join(dirTarget, 'beauty_AO_maskGeo.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_AO_maskShd":
                    new_file = os.path.join(dirTarget, 'beauty_AO_maskShd.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_AO_utils":
                    new_file = os.path.join(dirTarget, 'beauty_AO_utils.exr')
                    shutil.copy(old_file, new_file)
                case _:
                    print('file non considerato')
                


    if dirSuf=='Beauty_NIGHT' or dirSuf=='Bg_NIGHT' or dirSuf=='Piedistallo_NIGHT' :
        dirName = (dir[:15])
        
        os.makedirs('../PSmaster/'+dirName+'_NIGHT', exist_ok=True)
        dirTarget = os.path.abspath(os.path.join(parent, 'PSmaster/'+dirName+'_NIGHT'))
        

        for f in fList:
            
            fileSuf = (f[16:])
            
            fSuf = fileSuf[:-6]
            
            old_file = os.path.join(dir, f)
            
            match fSuf:
                case "Beauty_NIGHT":
                    new_file = os.path.join(dirTarget, 'beauty_night.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_NIGHT_maskGeo":
                    new_file = os.path.join(dirTarget, 'beauty_night_maskGeo.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_NIGHT_maskShd":
                    new_file = os.path.join(dirTarget, 'beauty_night_maskShd.exr')
                    shutil.copy(old_file, new_file)
                case "Beauty_NIGHT_utils":
                    new_file = os.path.join(dirTarget, 'beauty_night_utils.exr')
                    shutil.copy(old_file, new_file)
                case "Bg_NIGHT":
                    new_file = os.path.join(dirTarget, 'bg_night.exr')
                    shutil.copy(old_file, new_file)
                case "Bg_NIGHT_maskGeo":
                    new_file = os.path.join(dirTarget, 'bg_night_maskGeo.exr')
                    shutil.copy(old_file, new_file)
                case "Bg_NIGHT_maskShd":
                    new_file = os.path.join(dirTarget, 'bg_night_maskShd.exr')
                    shutil.copy(old_file, new_file)
                case "Bg_NIGHT_utils":
                    new_file = os.path.join(dirTarget, 'bg_night_utils.exr')
                    shutil.copy(old_file, new_file)
                case "Piedistallo_NIGHT":
                    new_file = os.path.join(dirTarget, 'piedistallo_night.exr')
                    shutil.copy(old_file, new_file)
                case "Piedistallo_NIGHT_maskGeo":
                    new_file = os.path.join(dirTarget, 'piedistallo_night_maskGeo.exr')
                    shutil.copy(old_file, new_file)
                case "Piedistallo_NIGHT_maskShd":
                    new_file = os.path.join(dirTarget, 'piedistallo_night_maskShd.exr')
                    shutil.copy(old_file, new_file)
                case "Piedistallo_NIGHT_utils":
                    new_file = os.path.join(dirTarget, 'piedistallo_night_utils.exr')
                    shutil.copy(old_file, new_file)    
                case _:
                    print('file non considerato')          



   




    

           
    










                
   