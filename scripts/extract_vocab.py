with open('words.txt', 'r', encoding='utf-8') as f, \
     open('vocabs.txt', 'w', encoding='utf-8') as out:
    for line in f:
        if line.startswith('#'): continue
        if len(line.strip()) > 1:
            out.write(line.strip() + '\n')
