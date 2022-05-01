import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    import os
    import time
    print('Please type the password of the current user : \n\n\n')
    os.system('SchTasks /Create /SC ONLOGON /V1 /TN "auto-fps-unlock" /TR \"'+os.getcwd()+r'\main.py'+ '"')
    print('task has been created sucessfully , script will automatically launch on next logon!')
    print('\n\nquitting in 5 sec...')
    time.sleep(5)
else:                                                                       
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)