def maincfunction():
    

    #---start of importing modules---
    import os                      #-
    from time import sleep         #-
    import ctypes                  #-
    import subprocess              #-
    import winsound                #-
    #----end of importing modules----


    #----------start of settings-------------              -------------------------------------------            
    staticprocname = 'RobloxPlayerBeta.exe'#-              - robloxprocessname (leave it)            -                 
    HiddenMode = 0                         #-              -console visible or not (0 or 1)          -
    NotifSound = 0                         #-              -sound when the process is found (0 or 1) -             
    SettingsFileName = 'settings'          #-              -fps unlocker settings file (don't touch) -  
    FastBoot = 'true'                      #-              -enable / disable fastboot (true or false)-
    #----------end of settings---------------              -------------------------------------------

    
    if HiddenMode == 1:
        ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
    else:
        pass

    with open(SettingsFileName,'r',encoding='utf-8') as file:
        
        data = file.readlines() 
    data[8] = "QuickStart="+FastBoot
    
    with open(SettingsFileName, 'w', encoding='utf-8') as file:
        file.writelines(data) 
    
    def findroblox(process_name):
        call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
        output = subprocess.check_output(call).decode()
        last_line = output.strip().split('\r\n')[-1]
        return last_line.lower().startswith(process_name.lower())
    
    StarterAlreadyStarted = 0

    while True:
    
        if findroblox(staticprocname) == True and StarterAlreadyStarted == 0:
            print('Roblox Process has been found!')
        
            if NotifSound == 1:
                winsound.Beep(440, 250)
            
            Files = os.listdir(os.getcwd()) 
        
            for file in Files:
            
                if file.startswith("rbx"): 
                    GrabbedExec = file
                    print('found the fpsunlocker executable!')
        
            subprocess.Popen(f'{os.getcwd()}/{GrabbedExec}') 
        
            StarterAlreadyStarted = 1
        
            print('finished the starter mechanism!')
    
        elif findroblox(staticprocname) == False and StarterAlreadyStarted == 1:
        
            os.system(f'taskkill /im {GrabbedExec} /f')

            StarterAlreadyStarted = 0
        
            print('sucessfully killed the fpsunlocker process!')
        
            sleep(3)
        
            os.system('cls')
        
        sleep(1)
    
if __name__ == "__main__":
    maincfunction()