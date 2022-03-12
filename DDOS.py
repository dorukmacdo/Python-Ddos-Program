import subprocess
import platform

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '9999999999', host]
    return subprocess.call(command)

host = 'Write Website Domain'
print(ping(host))