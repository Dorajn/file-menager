#sorting program for windows systems only

copy sort.py to folder in which you want to sort files. 
it will create folders named as extensions of files and move all those files with te same extension to folders

#manual
type: sort.py ARG1 ARG2

ARG1, int - how many files with same ext do you want to group in folders (non grouped files will be moved to 'other' folder

ARG2, string - what extension do you want to group (left empty will group all files)

sample call:

sort.py 5 txt
