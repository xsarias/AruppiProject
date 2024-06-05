"""
This is a main file of Aruppi project (initial point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from .anime_subsystem import AnimeFacade, Anime

MENU="""
......   ......   .... .... ......   ......  .......
|  _  |  |  _  \  |  | |  | |  _  \  |  _  \ |_   _|  
| |_| |  | |_|  | |  | |  | | |_\  | | |_\  |  | |
|  _  |  |     /  |  |_|  | |   __/  |   __/  _| |_
|_| |_|  |__|\_\  |_______| |__|     |__|    |_____|
        >>>> ALL JAPAN IN A SAME PLACE <<<
What do you want to explore?
1). Anime.
2). Radio.
3). News.
4). View my user profile.
"""
menu=AnimeFacade()
def main():
    """This if the main file of the project."""
    print(MENU)
    op=input(print("Please, select an option:"))
    if op=="1":
        
        print("no hace nada xd")
        menu.anime_menu()
    elif op=="2":
        pass
    elif op=="3":
        pass

if __name__ == "__main__":
    main()
