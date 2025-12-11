with open('a.txt', 'r', encoding='utf-8') as f:
    text = f.read()
words = text.split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Các từ dài nhất trong văn bản là:", longest_words)
print("Độ dài của các từ:", max_length)
