import time,random,json,os,platform

def clearCLI():
    if platform.system()=="Linux":
        os.system("clear")
    elif platform.system()=="Windows":
        os.system("cls")

def welcome():
    start="""
HELLO
Welcome to MineSweeper in commandline environment originally made by github.com/CallofVoid and improved by companions.
send `H` to display helpful tips.



and ...

please don't cheat

I hate cheaters and winning by cheating is failure :-/
"""
    for line in start.split("\n"):
        for char in line:
            print(f"\033[32m{char}",flush=True,end="")
            time.sleep(0.05)
        print()
        time.sleep(0.5)

helper="""
This game is based on a coordinate system.
That means that you can retrieve data of a cell by entering its coordinates in this format:
    row:column

If you guess that there's a mine below a cell, you can mark it with a flag this way:
    row:column-sf

You can unflag a flagged cell via:
    row:col-uf

If you retrieve a cell with a mine within, all of the mines explode,
and if only the mine cells are flagged, you win.

H to show this message again

Q or CTRL-C to stop game and exit (progress won't be saved)

"""

keep_alive=True
result=None# 'win' or 'lose', depending on outcome.
mines=[]#mine coordinates as [(row,col),…]
showed_map=[]#map that is shown to the user as a 2D list
main_map=[]#map that is used to run checks as a 2D list
flagged=[]#flagged tiles as [(row,col),…]
retrieved=[]#retrieved tiles as [(row,col),…]

#loading settings
with open('setting.json') as f:
    setting=json.load(f)

#generate mines
def init_mine():
    if(setting['minecount']<=setting['mapsize']['row']*setting['mapsize']['col']):
        while len(mines) < setting['minecount']:
            row=random.randint(1,setting['mapsize']['row'])
            col=random.randint(1,setting['mapsize']['col'])
            #checks if this pair of coordinates already has a mine associated with it
            if (row,col) not in mines:
                mines.append((row,col))
    else:
        print("challenging yourself with a land full of mines is good,but putting mines more than capacity of your area will have bad consequences")
        exit(1)
#generates the main and showed map
def generateMap():
    global mines
    mines.sort()
    #generating main map with mine positions
    for rowcount in range(1,setting['mapsize']['row']+1):
        main_map.append(["\033[31m💣\033[0m" if (rowcount,colcount) in mines else 0 \
             for colcount in range(1,setting['mapsize']['col']+1)])
    #generating mine indicators in main map
    for mine in mines:
        #going over the 3x3 field around the mine
        #and incrementing the mine indicators
        for row in range(mine[0]-2,mine[0]+1):
            for col in range(mine[1]-2,mine[1]+1):
                if row>=0 and col>=0 \
                    and row<setting["mapsize"]["row"] and col<setting["mapsize"]["col"] \
                    and type(main_map[row][col])==int:#don't increment if a bomb is there
                    
                    main_map[row][col]+=1
    #generating showed map
    for rows in range(setting['mapsize']['row']):
        showed_map.append(["■",]*setting['mapsize']['col'])

#checks a tile and handles the bomb beneath it, if present
def retrieve(row,col):
    global keep_alive
    global result
    if col<=0 or row<=0 or col>setting['mapsize']['col'] or row>setting['mapsize']['row'] :
        print('out of range :-/')
    elif (row,col) in mines:
        result='lose'
        keep_alive=False
    elif (row,col) not in flagged:
        showed_map[row-1][col-1]=main_map[row-1][col-1]
        if (row,col) not in retrieved:
            retrieved.append((row,col))
    clearCLI()
    show_map(showed_map)

#flags a tile
def setflag(row,col):
    rtrvd_before=False
    #checking boundaries
    if not col<=0 and not row <=0 and not col>setting['mapsize']['col'] and not row>setting['mapsize']['row'] :
        #check if tile is already open
        if (row,col) in retrieved:
            print('you tried to aftermath after the fact')
        else:
            print("I remember you flagged this cell, double checking is not necessary")#if flagging is successful this message will not be seen by human eye
            #adding coords to flagged list
            if (row,col) not in flagged:
                flagged.append((row,col))
                showed_map[row-1][col-1]='🚩'#setting 'flagged' icon
                clearCLI()
                show_map(showed_map)

#removes the flag from a tile
def unflag(row,col):
    #do nothing if the tile isn't flagged
    if (row,col) in flagged:
        #yes, this removes this tuple from the list. If it doesn't, it throws an exception, so you'd notice
        flagged.remove((row,col))
        showed_map[row-1][col-1]='■'#setting icon for unretrieved tile
        clearCLI()
        show_map(showed_map)

#prints a map to console
def show_map(mapp):
    for i in range(setting['mapsize']['col']+1):
        print(f"\033[36m{i:<4d}\033[0m",end="")
    print('column\n')
    rowc=1
    for i,row in enumerate(mapp,1):
        print(f"\033[36m{i:<4d}\033[0m",end='')
        for col in row:
            print(col,end='   ')
            
        print(end="\n\n")
    print('row')

def main_loop():
    for i in range(setting['mapsize']['col']+1):
        print(f"\033[36m{i:<4d}\033[0m",end='')
    print('column\n')
    rowc=1
    for i,row in enumerate(showed_map,1):
        print(f"\033[36m{i:<4d}\033[0m",end='')
        for col in row:
            print(col,end='   ')
            
        print(end="\n\n")
    print('row')
    global keep_alive
    global result
    while keep_alive:
        try:
            #getting the action from the user
            user_input=input('\033[32myour action? [H | Q | row:col | row:col-sf]\033[0m :  ')
            #splitting the coordinates and -sf or -uf, if they exist
            commands=user_input.split('-')
            #getting coordinates
            coords=commands[0].split(':')
            #processing setflag and unflag commands
            if len(commands)==2:
                if(coords[0].isnumeric() and coords[1].isnumeric()):
                    if commands[1]=='sf':
                        setflag(int(coords[0]),int(coords[1]))
                        continue
                    elif commands[1]=='uf':
                        unflag(int(coords[0]),int(coords[1]))
                        continue
                else:
                    print("I don't know where this position is")
                    continue
            #processing help, quit, and retrieving
            elif len(commands)==1:
                if user_input=='H':
                    print(helper)
                    continue
                if user_input=='Q':
                    keep_alive=False
                    continue
                if len (coords)==2:
                    if(coords[0].isnumeric() and coords[1].isnumeric()):
                        #retrieving tile, clearing screen, and showing resulting map
                        retrieve(int(coords[0]),int(coords[1]))
                        clearCLI()
                        show_map(showed_map)
                    else:
                        print("sorry I don't know where that position is")
                else:
                    print("the coordinates you entred is out of dimensions that i work")
            else:
                print("I tried, but I couldn't understand what you want me to do in this format")
            
            
            
        except KeyboardInterrupt:
            keep_alive=False#Ctrl+C counts as quitting
        #checking if all the mines, and only the mines, are flagged
        if len(flagged)==len(mines):
            allflagged = True
            for pair in flagged:
                if pair not in mines:
                    allflagged = False
                    break
            if allflagged:
                keep_alive=False
                result="win"
        
        
    if result=="win":
        show_map(main_map)
        print("\033[37mYou've neutralized all of the mines in this field.")
        exit(0)
    elif result=="lose":
        show_map(main_map)
        print("KABOOOM! You detonated a mine and it caused the whole area turn into ruins\n ... ah-choo!\n Sorry, I'm allergic to burnt gun powder and napalm smell.")
        exit(2)
    elif result==None:
        print("Game stopped without any result :(")
        exit(1)
welcome()#comment this to skip the intro dialog
init_mine()#creating mines with unique location
generateMap()#putting mines in map and then adding indication numbers

main_loop()
#function that demonstrates the game main_loop
#including calling retrieve() , setflag() and unflag() functions
#it also checks for conditions of winning and loosing game and updating showed map
