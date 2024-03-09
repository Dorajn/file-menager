import os, sys
import shutil

#returns file extension as string
def extension(text):
    table = text.split(".")
    length = len(table)
    return table[length - 1]


range_of_sorting = sys.argv[1]
ingredients = sys.argv[0].split("\\")
path = ""
program_path = sys.argv[0]

for i in range(len(ingredients) - 1):
    path += ingredients[i] + "\\"


#creating hashtable with key extension and value count of files with this extension
h_table = {}
for file_name in os.listdir(path):

    if not os.path.isfile(path + "\\" + file_name):
        continue

    extenstion = file_name.split(".")[1]

    if extenstion not in h_table:
        h_table[extenstion] = 1
    else:
        h_table[extenstion] += 1

#this program is not touched with sort alg
if "py" in h_table:
    if h_table["py"] > 1:
        h_table["py"] -= 1
    else:
        del h_table["py"]


#sorting and creating folders
for key, value in list(h_table.items()):

    if value >= int(range_of_sorting):
        os.makedirs(key, exist_ok = True)

        for i in os.listdir(path):
            if key == extension(i) and path + i != program_path:
                destination_path = path + "\\" + key
                shutil.move((path + "\\" + i), destination_path)

        del h_table[key]


flag = True
for i in os.listdir(path):

    if os.path.isfile(path + "\\" + i) and path + i != program_path:
        if flag:
            os.makedirs("other", exist_ok = True)
            flag = False

        destination_path = path + "\\" + "other" 
        shutil.move((path + "\\" + i), destination_path)

