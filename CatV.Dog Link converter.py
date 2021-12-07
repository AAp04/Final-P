import re

data = open("Link.txt", 'r')
output = open('Newlink.txt', 'w')
text = data.read()
print(text)

baseurl = "https://drive.google.com/uc?export=download&id="

m = re.findall('d/(.+?)/view', text)
#print(m)

newurl = ''
for i in m:
    newurl = baseurl+i +"\t"+"\t"+"\t"
    #print(baseurl+i)
    print(newurl)
    output.write(newurl)
output.close()
    




