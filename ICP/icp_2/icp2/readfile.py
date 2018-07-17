filepath = r'C:\Users\bsidd\Desktop\bhargavi.txt'
with open(filepath) as fp:
    with open("Sample1.txt", "w") as fp1:
     for line in fp:
        length = str(len(line.strip()))
        line1 = line.strip()+',' + length
        print(line1)
        fp1.write(line1)
        fp1.write("\n")

gh = open(r"C:\Users\bsidd\Desktop\bsid.txt", "r")
count = 0
data = gh.read()
each_line = data.split("\n")
for i in each_line:
    word = i.split(" ")
    print( " ".join(word), len(word))

