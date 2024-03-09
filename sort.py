import os, sys
import shutil

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

h_table = {}
for file_name in os.listdir(path):
    extenstion = file_name.split(".")[1]

    if extenstion not in h_table:
        h_table[extenstion] = 1
    else:
        h_table[extenstion] += 1

if "py" in h_table:
    if h_table["py"] > 1:
        h_table["py"] -= 1
    else:
        del h_table["py"]


for key, value in list(h_table.items()):

    if value >= int(range_of_sorting):
        os.makedirs(key, exist_ok = True)

        for i in os.listdir(path):
            if key == extension(i) and path + i != program_path:
                destination_path = path + "\\" + key
                shutil.move((path + "\\" + i), destination_path)

        del h_table[key]


for i in os.listdir(path):
    if os.path.isfile(path + "\\" + i) and path + i != program_path:
        os.makedirs("other", exist_ok = True)
        destination_path = path + "\\" + "other"
        shutil.move((path + "\\" + i), destination_path)

