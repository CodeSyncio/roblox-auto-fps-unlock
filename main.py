#---start of importing modules---
import os                      #-
import subprocess              #-
from time import sleep         #-
import ctypes                  #-
import subprocess              #-
#----end of importing modules----


#----------start of settings-------------              -------------------------------------               
staticprocname = 'RobloxPlayerBeta.exe'#-              - robloxprocessname (leave it)      -                       
HiddenMode = 0                         #-              -console visible or not (0 or 1)    -
#----------end of settings---------------              -------------------------------------

if HiddenMode == 1:
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
else:
    pass

def findroblox(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name

    output = subprocess.check_output(call).decode()
    
    last_line = output.strip().split('\r\n')[-1]
    
    return last_line.lower().startswith(process_name.lower())
StarterAlreadyStarted = 0

while True:
    
    if findroblox(staticprocname) == True and StarterAlreadyStarted == 0:
        print('Roblox Process has been found!')

        Files = os.listdir(os.getcwd()) 
        
        for file in Files:
            
            if file.startswith("rbx"): 
                
                GrabbedExec = file
                
                print('found the fpsunlocker executable!')
        
        
        subprocess.Popen(os.getcwd()+'/'+GrabbedExec) 
        
        StarterAlreadyStarted = 1
        
        print('finished the starter mechanism!')
    
    elif findroblox(staticprocname) == False and StarterAlreadyStarted == 1:
        
        os.system('taskkill /im '+GrabbedExec+ ' /f')
        
        StarterAlreadyStarted = 0
        
        print('sucessfully killed the fpsunlocker process!')
        
        sleep(3)
        
        os.system('cls')
    
    
