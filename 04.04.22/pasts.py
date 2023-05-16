f = open("pasts.txt")
gar = len(f.read(1))
f.seek(0)
vards = ""
vietas = []

for i in range(gar):
    c = f.read(1)
    if c == " ":
        if len(vietas) == 0:
            vietas.append(vards)
        else:
            i = 0
            while vards[0] < vietas[i][0] and i < len(vietas):
                i += 1
            vietas.insert (i, vards)
        vards = ""
    else:
        vards += c
        