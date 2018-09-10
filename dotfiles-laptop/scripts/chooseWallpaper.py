import os
from subprocess import call
import sys


def numberName(i, name):
    if len(name) > 15:
        name = name[:12] + '...'
    name = name + (15 - len(name)) * ' '

    return str(i) + '\t - ' + name + '\t'


if __name__ == '__main__':
    home = os.environ['HOME']
    folder = home + '/Pictures/'
    fileformats = ['.jpg', '.png']
    wallpapers = sorted(
        list(filter(lambda x: x[-4:] in fileformats, os.listdir(folder))))

    print('Available wallpapers:\n-----------------')

    for i, name in enumerate(wallpapers):
        if (i + 1) % 3 == 0:
            print(numberName(i, name), end='\n')
        else:
            print(numberName(i, name), end=' ')

    print('\nPlease choose number or (q) for quit')

    acceptedInp = False
    while acceptedInp == False:
        try:
            usrInp = input()
            if usrInp != 'q':
                usrInp = int(usrInp)
        except:
            usrInp = -1

        print(usrInp)
        if usrInp == 'q':
            exit()
        elif usrInp in range(len(wallpapers)):
            chosenWallpaper = folder + wallpapers[usrInp]
            acceptedInp = True
        else:
            print('Not a valid choice, please try again or (q) for exit')

    call([home + '/Scripts/setWallpaper.sh', chosenWallpaper])
