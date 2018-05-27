import os
from subprocess import call

if __name__ == '__main__':
    folder = '/home/angel/Pictures/TerminalWallpapers/'
    fileformats = ['.jpg', '.png']
    wallpapers = sorted(list(\
                 filter(lambda x: x[-4:] in fileformats, os.listdir(folder))\
    ))

    print('Available backgrounds:\n-----------------')

    choices = []
    for i, background in enumerate(wallpapers):
        print(i, '\t - ', background)
        choices.append(str(i))
        print

    print('\nPlease choose number or (q) for quit')

    acceptedInp = False
    while acceptedInp == False:
        usrInp = input()
        if usrInp in choices:
            chosenWallpaper = wallpapers[int(usrInp)]
            acceptedInp = True
        elif  usrInp == 'q':
            exit()
        else:
            print('Not a valid choice, please try again or (q) for exit')

    call(['/home/angel/Documents/Scripts/URxvt/background_change.sh', chosenWallpaper])
