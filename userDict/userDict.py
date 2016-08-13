import re
l = []
with open('raw.txt', 'r') as f:
    for line in f:
        line = line.strip()
        words = line.split('.')
        for word in words:
            if word != '\n':
                l.append(word.strip())
for w in l:
    print w.decode('utf-8')
