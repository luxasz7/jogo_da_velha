import subprocess
import platform

class Clear:
    def clear():
        if platform.system() == 'Linux' or platform.system() == 'Darwin':
            subprocess.call('clear', shell=True)
        elif platform.system() == 'Windows':
            subprocess.call('cls', shell=True)