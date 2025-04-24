#!/usr/bin/env python3



#words = ['ace', 'king', 'queen', 'jack', 'ten']

def written(words):
    if len(words) == 0:
            print('error: list has no iterables')
    for i in range(len(words)):
        if i == len(words) - 1:
            words[-1] = 'and ' + words[-1]
            written = print(', '.join(words))
                
balcony = ['plants', 'rug', 'bars', 'crates', 'ashtray']
print(balcony)
written(balcony)
print('\n')

spam = ['ace', 'king', 'queen', 'jack', 'ten']
print(spam)
written(spam)
print('\n')

empty = []
print(len(empty))
written(empty)
