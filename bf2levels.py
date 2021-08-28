levels_dir='C:\\Program Files (x86)\\Bull3t\\BFHD\\mods\\bf2\\Levels\\'
import glob
import zipfile
import shutil
import os.path

zipfiles=glob.glob(levels_dir+'*\server.zip')
for file in zipfiles:
    if not os.path.isfile(file[:-4]+'_original.zip'): shutil.copyfile(file, file[:-4]+'_original.zip')
    with zipfile.ZipFile(file,"r") as zip_ref:
        zip_ref.extractall(file[:-10]+'temp10')
    confiles=glob.glob(file[:-10]+'temp10\\GameModes\\**\\GamePlayObjects.con',recursive=True)
    for confile in confiles:
        fin = open(confile, "rt")
        data = fin.read()
        data = data.replace('unableToChangeTeam 1', 'unableToChangeTeam 0')
        data = data.replace('timeToGetControl 0', 'timeToGetControl 20')
        data = data.replace('timeToLoseControl 0', 'timeToLoseControl 20')
        fin.close()
        fin = open(confile, "wt")
        fin.write(data)
        fin.close()
    shutil.make_archive(file[:-4], 'zip', file[:-10]+'temp10')
    shutil.rmtree(file[:-10]+'temp10')