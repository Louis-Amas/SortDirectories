from sys import argv
from os import listdir, mkdir, rename
from os.path import isdir, join

if len(argv) != 3:
    print(argv[0], ' src dest')
    exit(1)

directory = argv[1]
dest = argv[2]

mkdir(dest)

name_unsort = 'non_trié'
mkdir(join(dest, name_unsort))

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',  'U', 'V', 
'W', 'X', 'Y', 'Z']

for letter in alphabet:
    mkdir(join(dest, letter))

for path in  listdir(directory):
    fullPath = join(directory, path)
    if isdir(fullPath):
        rename(fullPath, join(dest, path[0].upper(), path))
    else:
        rename(fullPath, join(dest, name_unsort, path))
