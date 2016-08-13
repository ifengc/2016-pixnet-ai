# -*- coding: utf-8 -*-

word_dict = dict()
with open('cat.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        if line not in word_dict.keys():
            word_dict[line] = 1
        else:
            word_dict[line] += 1
        for word in word_dict.keys():
            print '%s\t%s' % (word, word_dict[word])
