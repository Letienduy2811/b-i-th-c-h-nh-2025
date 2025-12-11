f = open('D:/a.txt', 'r', encoding='utf-8')

char = 0   # Đếm ký tự
wc = 0     # Đếm từ
lc = 0     # Đếm dòng

for line in f:
    lc += 1
    char += len(line)
    words = line.split()
    wc += len(words)

f.close()

print("The number of characters is %d" % char)
print("The number of words is %d" % wc)
print("The number of lines is %d" % lc)
