### This program is for educational purposes only. It's not made to make Rust any more toxic.

# rust_offliner
Monitors a Rust gameserver and alerts you when a player disconnects. Can also monitor multiple playernames at once.

## How it works
Rust uses Source as its server system. Because it does, we are able to query the server using A2S queries and get info on the server,
such as amount of players, map name, etc. This is the reason you are able to view servers through Steam without actually being in the game.

## Setup  
Install requirements: `pip install -r requirements.txt`.  
Set the server IP:port in config.ini. (also, the default server in there is a battleground server, so dont worry)  
Then set the names of the players to monitor in config.ini as well, separated by commas.  
Done.
  
## Fake players
Apparently a whole lot of servers use fake players to boost their player count, so you will see them whenever the program prints the player list (they have basic names like christopher, etc). This will not affect your player monitoring as long as you do not enter the name of a fake player.


