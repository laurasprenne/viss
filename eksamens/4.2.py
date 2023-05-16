with open("teksts.txt", "r") as f:
    text = f.read()
    text = text.lower()
    print(text)
    nevajadzigi = ".,!?:;()"
    for char in nevajadzigi:
        text.replace(char, "")
    text = text.split(" ")
    print(text)

    vardu_skaits = {}
    for vards in text:
        if len(vards) > 3:
            vardu_skaits[vards] = text.count(vards)

    print(sorted(vardu_skaits, key=vardu_skaits.get()))

    print(vardu_skaits)