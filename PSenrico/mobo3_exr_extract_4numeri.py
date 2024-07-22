import os, shutil


source = "v000"
os.chdir(source)


path = os.getcwd()

parent = os.path.abspath(os.path.join(path, os.pardir))


os.makedirs('../PSmaster', exist_ok=True)



dirList = []
dirList = os.listdir()


for dir in dirList:
    
    dirSuf = (dir[16:]) 
    

    fList = []
    fList = os.listdir(dir)
    
    

    if dirSuf=='Beauty' or dirSuf=='Bg' or dirSuf=='Piedistallo':
        dirName = (dir[:15])
        
        os.makedirs('../PSmaster/'+dirName, exist_ok=True)
        dirTarget = os.path.abspath(os.path.join(parent, 'PSmaster/'+dirName))
        

        for f in fList:
            
            fileSuf = (f[16:])
            
            fSuf = fileSuf[:-9] 
            
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
                case "Piedistallo":
                    new_file = os.path.join(dirTarget, 'piedistallo.exr')
                    shutil.copy(old_file, new_file)
                case "Piedistallo_maskGeo":
                    new_file = os.path.join(dirTarget, 'piedistallo_maskGeo.exr')
                    shutil.copy(old_file, new_file)
                case "Piedistallo_maskShd":
                    new_file = os.path.join(dirTarget, 'piedistallo_maskShd.exr')
                    shutil.copy(old_file, new_file)
                case "Piedistallo_utils":
                    new_file = os.path.join(dirTarget, 'piedistallo_utils.exr')
                    shutil.copy(old_file, new_file)
                case _:
                    print('file non considerato')
                


    if dirSuf=='Beauty_NIGHT' or dirSuf=='Bg_NIGHT' or dirSuf=='Piedistallo_NIGHT':
        dirName = (dir[:15])
        
        os.makedirs('../PSmaster/'+dirName+'_NIGHT', exist_ok=True)
        dirTarget = os.path.abspath(os.path.join(parent, 'PSmaster/'+dirName+'_NIGHT'))
        

        for f in fList:
            
            fileSuf = (f[16:])
                        
            fSuf = fileSuf[:-9] 
            
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


print("SCRIPT ESEGUITO !!!!")
   




    

           
    










                
   