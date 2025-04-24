spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.. lint check my code for this challenge:  

def written(words):
    if len(words) == 0:
            print('error: list has no iterables')
    for i in range(len(words)):
        if i == len(words) - 1:
            words[-1] = 'and ' + words[-1]
            written = print(', '.join(words))
            <hr>
🔋33% 04.24.2025 | 8:30:13 
powerhouse OS 1% | ./42425.py
['plants', 'rug', 'bars', 'crates', 'ashtray']
plants, rug, bars, crates, and ashtray


['ace', 'king', 'queen', 'jack', 'ten']
ace, king, queen, jack, and ten


0
error: list has no iterables
🔋52% 04.24.2025 | 9:59:32 
powerhouse OS 1% | <hr>
Your function logic is on the right track, but there are a few issues both with the code and formatting. Let’s fix it up:

Issues:
    You're modifying the list inside the loop, which is not needed.

    You use print() inside the function — but the task says to return a string.

    You named the function and a variable the same (written) — this can cause confusion.

    The for loop doesn't actually do anything except on the last iteration.

    Error handling could be improved by returning a value or raising an error, not just printing.            