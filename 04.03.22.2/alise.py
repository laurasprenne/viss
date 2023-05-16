f = open("alise.txt")
gar = len(f.read(1))
f.seek(0)
parent = f.read(1)
mezgls = ""
mezgli = []
for i in range(gar):
    mezgls += f.read(1)
    if mezgls == " ":
        mezgls = ""
    elif mezgls == "\n":
        parent = f.read(1)
        mezgli = []
    else:
        mezgli.insert(mezgls)