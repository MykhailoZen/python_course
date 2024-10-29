with open('file.txt', 'r+') as f:
    f.write("tttt")
    f.seek(0)
    print(f.read())

# f = open('file.txt', 'r+')
# f.write("ttrololol")
# f.seek(0)
# print(f.read())
# f.close()
