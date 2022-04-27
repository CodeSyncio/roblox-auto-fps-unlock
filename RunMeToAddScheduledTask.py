import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    import os
    os.system(r'SchTasks /Create /SC ONLOGON /TN "auto-fps-unlock" /TR "'+os.getcwd()+'/main.py"')
else:
    
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
