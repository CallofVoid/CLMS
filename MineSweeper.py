import time,random,json,os,platform

def welcome():
    start="""
HELLO
Wlcome to MineSweeper in commandline format
this game is made by github.com/CallofVoid
If you want to stop the game you can send `Q` or CTRL+C
For reading help send `H`



and ...


if you think its boring to do all this step by step
you can simply edit the script and call show_map(main_map) function to see the main map or print(mines) to locate mines and other kind of cheating 

but remember...

I hate cheaters and winning by cheating is your fault :-/
"""
    for line in start.split("\n"):
        for char in line:
            print("\033[32m"+char,flush=True,end="")
            time.sleep(0.05)
        print("")
        time.sleep(0.5)

helper="""
This game is baesd on coordinating system
it means that you can retrieve data of a cell by entering its coordinates in this format:
row:column

you can set a flag on the cell that you guess theres a mine under it in this way:
row:column-sf

unglagging a flagged cell by :
row:col-uf
if you retrieve a cell with mine all of the mines are exploded
and if only the mine cells are flagged you win

H to show this message again

Q or CTRL-C to stop game and exit(progress won't be saved)

"""

keep_alive=True
result=None
mines=[]
showed_map=[]
main_map=[]
flagged=[]
retrieved=[]
setting=json.load(open('setting.json'))


def init_mine():
    def checksum(row,col):
        for mine in mines:
            if row in mine and mine[row]==col:
                return 1
        return 0
        
    while len(mines) < setting['minecount']:
        row=random.randint(1,setting['mapsize']['row'])
        col=random.randint(1,setting['mapsize']['col'])
        errors=checksum(row,col)
        if not errors==0:
            continue
        else:
            mines.append({row:col})


def generateMap():
    global mines
    mines=sorted(mines, key=lambda mine: list(mine.items()))
    rowcount=0
    for row in range(setting['mapsize']['row']):
        colcount=0
        rowcount+=1
        row=[]
        for col in range(setting['mapsize']['col']):
            colcount+=1
            bombed=False
            for eachmine in mines:
                if rowcount in eachmine and eachmine[rowcount]==colcount:
                    row.append("\033[31m"+'■'+"\033[0m")
                    bombed=True
            if bombed==True:
                pass
            else:
                row.append(0)
                
        main_map.append(row)
    for mine in mines:
        minecol=list(mine.values())[0]-1
        minerow=list(mine.keys())[0]-1
        if not minerow==0:
            if not minerow ==setting['mapsize']['row']-1:
                if not minecol==0:
                    if not minecol==setting['mapsize']['col']-1:
                        if type(main_map[minerow-1][minecol-1]) == int:
                            main_map[minerow-1][minecol-1]+=1
                            
                        if type(main_map[minerow-1][minecol]) == int:
                            main_map[minerow-1][minecol]+=1
                            
                        if type(main_map[minerow-1][minecol+1]) == int:
                            main_map[minerow-1][minecol+1]+=1
                            
                        if type(main_map[minerow][minecol-1]) == int:
                            main_map[minerow][minecol-1]+=1
                            
                        if type(main_map[minerow][minecol+1]) == int:
                            main_map[minerow][minecol+1]+=1
                            
                        if type(main_map[minerow+1][minecol-1]) == int:
                            main_map[minerow+1][minecol-1]+=1
                        
                        if type(main_map[minerow+1][minecol]) == int:
                            main_map[minerow+1][minecol]+=1
                        
                        if type(main_map[minerow+1][minecol+1]) == int:
                            main_map[minerow+1][minecol+1]+=1
                            
                    elif minecol==setting['mapsize']['col']-1:
                        if type(main_map[minerow-1][minecol-1]) == int:
                            main_map[minerow-1][minecol-1]+=1
                            
                        if type(main_map[minerow-1][minecol]) == int:
                            main_map[minerow-1][minecol]+=1
                            
                        if type(main_map[minerow][minecol-1]) == int:
                            main_map[minerow][minecol-1]+=1
                            
                        if type(main_map[minerow+1][minecol-1]) == int:
                            main_map[minerow+1][minecol-1]+=1
                        
                        if type(main_map[minerow+1][minecol]) == int:
                            main_map[minerow+1][minecol]+=1
                elif minecol==0:
                    if type(main_map[minerow-1][minecol]) == int:
                            main_map[minerow-1][minecol]+=1
                        
                    if type(main_map[minerow-1][minecol+1]) == int:
                        main_map[minerow-1][minecol+1]+=1
                        
                    if type(main_map[minerow][minecol+1]) == int:
                        main_map[minerow][minecol+1]+=1
                        
                    if type(main_map[minerow+1][minecol]) == int:
                            main_map[minerow+1][minecol]+=1
                        
                    if type(main_map[minerow+1][minecol+1]) == int:
                        main_map[minerow+1][minecol+1]+=1
                        
            elif minerow ==setting['mapsize']['row']-1:
                if not minecol==0:
                    if not minecol==setting['mapsize']['col']-1:
                        if type(main_map[minerow-1][minecol-1]) == int:
                            main_map[minerow-1][minecol-1]+=1
                            
                        if type(main_map[minerow-1][minecol]) == int:
                            main_map[minerow-1][minecol]+=1
                            
                        if type(main_map[minerow-1][minecol+1]) == int:
                            main_map[minerow-1][minecol+1]+=1
                            
                        if type(main_map[minerow][minecol-1]) == int:
                            main_map[minerow][minecol-1]+=1
                            
                        if type(main_map[minerow][minecol+1]) == int:
                            main_map[minerow][minecol+1]+=1
                        
                    elif minecol==setting['mapsize']['col']-1:
                        if type(main_map[minerow-1][minecol-1]) == int:
                            main_map[minerow-1][minecol-1]+=1
                            
                        if type(main_map[minerow-1][minecol]) == int:
                            main_map[minerow-1][minecol]+=1
                            
                        if type(main_map[minerow][minecol-1]) == int:
                            main_map[minerow][minecol-1]+=1
                            
                elif minecol==0:
                    if type(main_map[minerow-1][minecol]) == int:
                            main_map[minerow-1][minecol]+=1
                        
                    if type(main_map[minerow-1][minecol+1]) == int:
                        main_map[minerow-1][minecol+1]+=1
                        
                    if type(main_map[minerow][minecol+1]) == int:
                        main_map[minerow][minecol+1]+=1
                        
        elif minerow==0:
            if not minecol==0:
                    if not minecol==setting['mapsize']['col']-1:
                        if type(main_map[minerow][minecol-1]) == int:
                            main_map[minerow][minecol-1]+=1
                            
                        if type(main_map[minerow][minecol+1]) == int:
                            main_map[minerow][minecol+1]+=1
                            
                        if type(main_map[minerow+1][minecol-1]) == int:
                            main_map[minerow+1][minecol-1]+=1
                        
                        if type(main_map[minerow+1][minecol]) == int:
                            main_map[minerow+1][minecol]+=1
                        
                        if type(main_map[minerow+1][minecol+1]) == int:
                            main_map[minerow+1][minecol+1]+=1
                            
                    elif minecol==setting['mapsize']['col']-1:
                        if type(main_map[minerow][minecol-1]) == int:
                            main_map[minerow][minecol-1]+=1
                            
                        if type(main_map[minerow+1][minecol-1]) == int:
                            main_map[minerow+1][minecol-1]+=1
                        
                        if type(main_map[minerow+1][minecol]) == int:
                            main_map[minerow+1][minecol]+=1
            elif minecol==0:
                if type(main_map[minerow][minecol+1]) == int:
                    main_map[minerow][minecol+1]+=1
                    
                if type(main_map[minerow+1][minecol]) == int:
                        main_map[minerow+1][minecol]+=1
                    
                if type(main_map[minerow+1][minecol+1]) == int:
                    main_map[minerow+1][minecol+1]+=1
    for rows in range(setting['mapsize']['row']):
        rowss=[]
        for columnss in range(setting['mapsize']['col']):
            rowss.append("□")
        showed_map.append(rowss)

def retrieve(row,col):
    global keep_alive
    global result
    explode=False
    flagged_before=False
    if not col<=0 and not row <=0 and not col>setting['mapsize']['col'] and not row>setting['mapsize']['row'] :
        for flgd in flagged:
            if row in flgd and flgd[row]==col:
                flagged_before=True
                break
            else: 
                pass
        for mine in mines:
            if row in mine and mine[row]==col:
                explode=True
                break
            else:
                pass
        if explode==True:
            result='lose'
            keep_alive=False
            
        else:
            if not flagged_before==True:
                showed_map[row-1][col-1]=main_map[row-1][col-1]
                if not {row:col} in retrieved:
                    retrieved.append({row:col})
                else:pass
            else:pass
    else:
        print('out of range :-/')
    if platform.system()=="Linux":
        os.system("clear")
    elif platform.system()=="Windows":
        os.system("cls")
    show_map(showed_map)

def setflag(row,col):
    rtrvd_before=False
    if not col<=0 and not row <=0 and not col>setting['mapsize']['col'] and not row>setting['mapsize']['row'] :
        for retrieveddd in retrieved:
            if row in retrieveddd and retrieveddd[row]==col:
                rtrvd_before=True
                print('retrieved before')
                break
            else: pass
        if rtrvd_before==False:
            print("not retrieved before")
            showed_map[row-1][col-1]='\033[33m'+'○'+'\033[0m'
            if not {row:col} in flagged:
                flagged.append({row:col})
                if platform.system()=="Linux":
                    os.system("clear")
                elif platform.system()=="Windows":
                    os.system("cls")
                show_map(showed_map)
        else :
            pass

def unflag(row,col):
    flgd_before=False
    counter=0
    if not col<=0 and not row <=0 and not col>setting['mapsize']['col'] and not row>setting['mapsize']['row'] :
        for flgd in flagged:
            if row in flgd and flgd[row]==col:
                flgd_before=True 
                del(flagged[counter])
                showed_map[row-1][col-1]='□'
                if platform.system()=="Linux":
                    os.system("clear")
                elif platform.system()=="Windows":
                    os.system("cls")
                show_map(showed_map)
                break
            else:
                counter+=1  

def show_map(mapp):
    
    for i in range(setting['mapsize']['col']+1):
        if i<10:
            print("\033[36m"+str(i)+"\033[0m",end='   ')
        elif i>=10 and i<100:
            print("\033[36m"+str(i)+"\033[0m",end='  ')
        elif i >=100:
            print("\033[36m"+str(i)+"\033[0m",end=' ')
    print ('column\n')
    counter=1
    rowc=1
    for row in mapp:
        if counter<10:
            print("\033[36m"+str(counter)+"\033[0m"+"   ",end='')
            counter+=1
        elif counter>=10:
            print("\033[36m"+str(counter)+"\033[0m"+'  ',end='')
            counter+=1
        elif counter <=100 :
            print("\033[36m"+str(counter)+"\033[0m"+' ',end='')
        for col in row:
            print((col),end='   ')
            
        print('\n')
    print('row')

def main_loop():
    for i in range(setting['mapsize']['col']+1):
        if i<10:
            print("\033[36m"+str(i)+"\033[0m",end='   ')
        elif i>=10 and i<100:
            print("\033[36m"+str(i)+"\033[0m",end='  ')
        elif i >=100:
            print("\033[36m"+str(i)+"\033[0m",end=' ')
    print ('column\n')
    counter=1
    rowc=1
    for row in showed_map:
        if counter<10:
            print("\033[36m"+str(counter)+"\033[0m"+"   ",end='')
            counter+=1
        elif counter>=10:
            print("\033[36m"+str(counter)+"\033[0m"+'  ',end='')
            counter+=1
        elif counter <=100 :
            print("\033[36m"+str(counter)+"\033[0m"+' ',end='')
        for col in row:
            print(col,end='   ')
            
        print('\n')
    print('row')
    global keep_alive
    global result
    while keep_alive:
        try:
            user_input=input('\033[32m'+'your action? [H | Q | row:col | row:col-sf]'+'\033[0m'+' :  ')
            commands=user_input.split('-')
            coords=commands[0].split(':')
            if len(commands)==2:
                if commands[1]=='sf':
                    setflag(int(coords[0]),int(coords[1]))
                elif commands[1]=='uf':
                    unflag(int(coords[0]),int(coords[1]))
            elif len(commands)==1:
                if user_input=='H':
                    print(helper)
                    continue
                if user_input=='Q':
                    keep_alive=False
                    continue
                if len (coords)==2:
                    retrieve(int(coords[0]),int(coords[1]))
                    if platform.system()=="Linux":
                        os.system("clear")
                    elif platform.system()=="Windows":
                        os.system("cls")
                    show_map(showed_map)
                else:
                    print("invalid coords")
            else:
                print('invalid format')
            
            
            
        except KeyboardInterrupt:
            keep_alive=False
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
        print('\033[37m'+"You've nuteralized all of the mines in this field")
        exit(0)
    elif result=="lose":
        show_map(main_map)
        print('KABOOOM! you detonated a mine and it caused the whole area turn into a ruin\n ... ah-choo!\n sorry i have alergy to burnt gun powder and napalm smell')
        exit(2)
    elif result==None:
        print("game stoped without any result :(")
        exit(1)
welcome() #comment this if to skip the intro dialogs
init_mine()#creating mines with unique location
generateMap()
#putting mines in map and then adding instruction numbers
#based on the area that mine is located:
#upper-left codner
#upper-right corner
#upper edge except for the corners
#left edge excluding the corners
#bottom-left corner
#bottom-right corner
#bottom edge except for the corners
#right edge except for the corners
#whole central area that is not edge or corner

main_loop()
#function that demonstrates the game main_loop
#including calling retrieve() , setflag() and unflag() functions
#it also checks for conditions of winning and loosing game and updating showed map
