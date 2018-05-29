import os
from subprocess import call

if __name__ == '__main__':
    home = os.environ['HOME']
    folder = home + '/Pictures/TerminalWallpapers/'
    fileformats = ['.jpg', '.png']
    wallpapers = list(filter(lambda x: x[-4:] in fileformats, os.listdir(folder)))

    currentwallpaper = ''

    with open(home + '/Documents/Scripts/current_wallpaper.txt') as db:
        currentwallpaper = db.read().strip()

    conffile = home + '/.config/xfce4/terminal/terminalrc'
    fileLines = []
    with open(conffile, 'r') as conf:
        for line in conf:
            if line[:len('BackGroundImageFile')] == ('BackgroundImageFile'):
                filepath = line.split('=')[1]
                currentwallpaper = filepath[filepath.rfind('/')+1:].strip()
            fileLines.append(line)

    nextwallpaper = currentwallpaper
    for i, wallpaper in enumerate(wallpapers):
        if wallpaper == currentwallpaper:
            if i < (len(wallpapers) - 1):
                nextwallpaper = wallpapers[i+1]
                print('Next wallpaper:', wallpapers[i+1])
                break
            else:
                nextwallpaper = wallpapers[0]
                print('Next wallpaper:', wallpapers[0])
                break

    if nextwallpaper == currentwallpaper:
        currentwallpaper = wallpapers[0]

    call([home + '/Documents/Scripts/xfce_changebg.sh', folder + nextwallpaper])
