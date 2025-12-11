with open('a.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()    
        print(line[::-1])       
