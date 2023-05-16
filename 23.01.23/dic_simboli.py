dic = {}
sv = input("ievadi tekstu:")
for char in sv:
    if char.isalpha():
        dic[char] = sv.count(char)

sorted_dic = sorted(dic, key=dic.get, reverse=True)
print(sorted_dic)