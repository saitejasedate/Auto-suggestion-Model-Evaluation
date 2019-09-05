import re
# f = open("cleandata.txt", "r", encoding = "utf-8")
# for x in f:
#     cs1 = re.sub(r'[a-zA-Z0-9]+', '', x)
#     cs2 =  cs1.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+\n''"})
#     cs3 = cs2.replace("    ","").split(" ")
#     cs3.remove('')
#     cs4 = []
#     cs4.append(cs3[:5])
#     print(cs4)
    # print(cs4)
    # word = open('word.txt', 'w',encoding = "utf-8")
    # print(cs4,file = word)
    # word.close()
    
f = open('cleandata.txt', "r",encoding = "utf-8")
# # cs4 = []
while True:
    cs4 = []
    for line in f:
        cs1 = re.sub(r'[a-zA-Z0-9]+', '', line)
        cs2 =  cs1.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+\n''"})
        # print(cs2)
        cs3 = cs2.replace("    ","").split(" ")
        for i in range(0,len(cs3)-2):
            cs4.append(cs3[:5])
    print(cs4)
        # cs4.append(cs3[:3])
    # if not line:
    #     break
f.close()

# places = []

# # open file and read the content in a list
# with open('cleandata.txt', "r",encoding = "utf-8") as filehandle:  
#     filecontents = filehandle.readlines()

#     for line in filecontents:
#         # remove linebreak which is the last character of the string
#         current_place = line[:-1]
#         nplace = current_place.split(" ")

#         # add item to the list
#         places.append(nplace)
#         print(places)
# infile = open('cleandata.txt', "r",encoding = "utf-8")
# firstLine = infile.readline().split(" ")
# print(firstLine)
# # new_list = [firstLine[x:x+3] for x in range(0, len(firstLine) - 2, 3)]
# # # print(new_list)
# new_list = []
# new_list.append(firstLine[:3])
# print(new_list)

