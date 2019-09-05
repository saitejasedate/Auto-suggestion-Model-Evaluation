# from xml.etree.ElementTree import parse
# import xml.etree.ElementTree as ET
# tree = ET.parse('bookstore.xml')
# root = tree.getroot()
# root.tag, root.attrib
# for child_of_root in root:
#     print (child_of_root.tag, child_of_root.attrib)
# print([elem.tag for elem in root.iter()])
# print(root.tag)
# for elem in tree.iter(tag='namespace'):
#     print(elem)


import xml.etree.ElementTree as ET
import re
l = []
processed  = []
final_file = open("processed_data.txt", "w+", encoding="utf-8")
tree = ET.parse('bookstore.xml')  
root = tree.getroot()
xmlstr = ET.tostring(root, encoding='unicode')
# xml_str = ET.tostring(xmlstr).decode()
# print       (xmlstr)
for elem in root:  
    for subelem in elem:
        # print(subelem.text)
        if subelem.text != None:
            if ord(subelem.text[0])>120:
             l.append(subelem.text)
for x in l:
    cs1 = re.sub(r'[a-zA-Z0-9]+', '', x)
    cs2 =  cs1.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+\n''"})
    print(cs1)
#     processed.append(x)
# print(len(processed))
    

# Generating the text file
# for ele in range(len(processed)):
# 	final_file.write(processed[ele])
# final_file.close()
	