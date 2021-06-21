import a2s
import ctypes
import configparser
from time import sleep

config = configparser.ConfigParser()
config.read('config.ini')

name = input('Input exact player name of who you would like to offline raid: ')
ip, port = config['rust_offliner']['ip'].split(':')
addr = (ip, int(port))
while True:
    plys = [p.name for p in a2s.players(addr)]
    print('Current players: ', ', '.join(plys))
    if name not in plys:
        print(name, "does not appear to be on the server! Now is the time to offline.")
        ctypes.windll.user32.MessageBoxW(0, f'Player {name} was not found on the server. Time to offline.', 'Rust offliner: It is time', 0x1000)
        break
    sleep(10)