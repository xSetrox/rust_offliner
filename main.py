import a2s
import ctypes
import configparser
from time import sleep

config = configparser.ConfigParser()
config.read('config.ini')
names = config['rust_offliner']['playernames'].split(',')
ip, port = config['rust_offliner']['ip'].split(':')
addr = (ip, int(port))
while True:
    plys = [p.name for p in a2s.players(addr)]
    print('Current players: ', ', '.join(plys))
    for name in names:
        if name not in plys:
            print(f'\"{name}\" does not appear to be on the server!')
            print(f'Monitoring is now OFF for \"{name}\" as they have went offline.')
            names.remove(name)
            ctypes.windll.user32.MessageBoxW(0, f'Player \"{name}\" was not found on the server. Time to offline.', 'Rust offliner: It is time', 0x1000)
    if not names:
        print('No more names left to monitor. Exiting.')
        break
    sleep(10)