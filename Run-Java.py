import subprocess
import glob

directory_items = {}
        
for i, j in enumerate(glob.glob("*.java")):
    # print(type(i), type(j), i, j)
    directory_items[i+1] = j

class FileObject:
    def __init__(self, name, has_main_method):
        self.name = name
        self.has_main_method = has_main_method

def check_main_method(filename):
    subprocess.run(f"javac {filename}")
    response = subprocess.run(f"javap {filename.rstrip('.java')}", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return(True if (response.stdout.decode('utf-8').find("main") != -1) else False)

for i, j in (directory_items.items()):
    directory_items[i] = FileObject(j, check_main_method(j))

main_methods = 0
java_file = ""
for i, j in directory_items.items():
    if (j.has_main_method):
        main_methods += 1
        if(main_methods == 1):
            java_file = j.name

if(main_methods > 1):
    files_with_main_method = []
    for j in directory_items.values():
        if (j.has_main_method):
            files_with_main_method.append(j)
    print("Multiple files with Main Method found:")
    for i, j in enumerate(files_with_main_method):
        print(f'\t{i + 1}. {j.name}')
    option = int(input("Enter the file number to run: "))
    java_file = files_with_main_method[option - 1].name
    print("\nRunning file: ", java_file)
    response = subprocess.run(f"java {java_file.rstrip('.java')}", stdout=subprocess.PIPE)
    print(response.stdout.decode('utf-8'))
elif(main_methods == 1):
    print("\nRunning file[Autodetected]: ", java_file)
    response = subprocess.run(f"java {java_file.rstrip('.java')}", stdout=subprocess.PIPE)
    print(response.stdout.decode('utf-8'))
    
hold = input()
