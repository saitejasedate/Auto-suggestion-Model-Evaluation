import re
f = open("cleandata.txt", "r", encoding = "utf-8")
for x in f:
    cs1 = re.sub(r'[a-zA-Z0-9]+', '', x)
    cs2 =  cs1.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+\n''"})
    cs3 = cs2.replace("    ","").split(" ")
    cs3.remove('')
    n = 10
    cs4 = [cs3[i * n:(i + 1) * n] for i in range((len(cs3) + n - 1) // n )]
    words = open('words.txt', 'w',encoding = "utf-8")
    print(cs4,file = words)
    words.close()



