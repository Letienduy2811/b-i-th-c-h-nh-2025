with open('a.txt', 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        count += 1

print("Số dòng trong file là:", count)
