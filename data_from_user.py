import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\SESA732254\PycharmProjects\pythonProject1\\build\exe.win-amd64-3.10')
# getting settings from settings.txt
data = []  # empty var
with open("settings.txt") as MyFile:  # open settings file
    for line in MyFile:  # loop
        data.append(line.split()[-1])  # getting information
