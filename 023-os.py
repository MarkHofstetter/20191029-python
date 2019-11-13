import os, shutil
from pprint import pprint

# cmd = 'ls'

# a = os.system(cmd)
# print(a)

# output = os.popen(cmd).read()
# print(output)

# h: python 021-qt qt-table.py

filename = os.path.join("h:\\", "python", "021-qt", "qt-table.py")

print(os.sep)
print(filename)
if os.path.isfile(filename):
    print("is file")

for root, dirs, files in os.walk('021-qt'):
    pprint(root)
    pprint(dirs)
    pprint(files)


'''
for filename in os.listdir("."):
   if filename.endswith(".py"):
       print(filename)
'''
