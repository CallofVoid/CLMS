# CLMS
(Command Line Mine Sweeper)
------------------------------

* Information List
  * [Description](#Description)
  * [Installation](#Installation)
  * [Important Notes](#Notes)
  * [Pictures](#Pictures)
  * email <callofvoid0@gmail.com> link to report bugs or suggestions

## Description
If you remember the nostalgia MineSweeper game
in Windows, you know how this game works;
but if you don't know or can't remember there's no problem

In MineSweeper you should avoid clicking on Mines
and use data of each cell carefully to put a flag 
on all of the Mines .
keep in mined that you win if only mine cells are flagged __NOT ALL OF THE CELLS__
and if you choose a mine cell you will loose
there's a more complete description on how the game works inside MineSweeper.py
see the [Important Notes](#Notes) section

## Installation
* [On Linux](#Linux)
* [On Termux](#Termux)
* [On Windows](#Windows)


### Linux
_Download from git or zip file then:_
```bash
cd /path/to/CLMS
apt install python3
python3 MineSweeper.py
```
> send H to see info about game rules and how to play
-----------------------------------------------------



### Termux
_download from git or zip file then:_
```bash
cd /path/to/CLMS
apt install python
python MineSweeper.py
```
> send H to see info about game rules and how to play
-----------------------------------------------------



### Windows
_download from git or zip file then:_
```bash
cd /path/to/CLMS
apt-get install python3
python3 MineSweeper.py
```
> send H to see more inf about game rules and how to play
---------------------------------------------------------

## Notes
- This script is written by python 3.9.5
- Tested only in Termux on Samsung A30s Android 9
- This is not a graphical game 
- you can change columms ,rows and mine counts in `setting.json` file
- reading comments of file can help you understand how it works
- game can handle maps as big as your screen and memory allows



