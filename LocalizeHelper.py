import glob
import re

stringArray = []

def getStrings(text):        
    matches = re.findall(r'"(.+?)"',text)
    return matches

def readFile(text):
    with open(filename) as file:
        for line in file:
            finding = getStrings(line)
            stringArray.extend(finding)

# root_dir needs a trailing slash (i.e. /root/dir/)
root_dir = "/Users/shivvaishnav/Documents/Personal/p/Experience_App_iOS/EXPERIENCES/"
for filename in glob.iglob(root_dir + '**/*.swift', recursive=True):
    readFile(filename)

newArr = list(set(stringArray))
print(newArr)

with open("/Users/shivvaishnav/Documents/Personal/localization.string", "w") as file:
        file.write("")

for string in newArr:
    with open("/Users/shivvaishnav/Documents/Personal/localization.string", "a") as file:
        file.write('"{0}" = "{1}";\n'.format(string, string))

with open("/Users/shivvaishnav/Documents/Personal/localization1.string", "w") as file:
        file.write("")

for string in newArr:
    with open("/Users/shivvaishnav/Documents/Personal/localization1.string", "a") as file:
        file.write('{0}\n\n'.format(string))