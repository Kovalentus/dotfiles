import os
from subprocess import call

if __name__ == '__main__':
    home = os.environ['HOME']
    folder = home + '/Pictures/'
    fileformats = ['.jpg', '.png']
    wallpapers = sorted(list(\
                 filter(lambda x: x[-4:] in fileformats, os.listdir(folder))\
    ))

    print('Available wallpapers:\n-----------------')

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
            chosenWallpaper = folder + wallpapers[int(usrInp)]
            acceptedInp = True
        elif  usrInp == 'q':
            exit()
        else:
            print('Not a valid choice, please try again or (q) for exit')

    call(["feh --bg-scale ", chosenWallpaper])
