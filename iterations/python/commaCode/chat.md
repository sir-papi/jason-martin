spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.. lint check my code for this challenge:  
```
def written(words):
    if len(words) == 0:
            print('error: list has no iterables')
    for i in range(len(words)):
        if i == len(words) - 1:
            words[-1] = 'and ' + words[-1]
            written = print(', '.join(words))
```
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
powerhouse OS 1% | 

<br>

Your function logic is on the right track, but there are a few issues both with the code and formatting. Let’s fix it up:

Issues:
    You're modifying the list inside the loop, which is not needed.

    You use print() inside the function — but the task says to return a string.

    You named the function and a variable the same (written) — this can cause confusion.

    The for loop doesn't actually do anything except on the last iteration.

    Error handling could be improved by returning a value or raising an error, not just printing.   

<hr><hr>

```
def written(words):
if len(words) == 0:
        print('error: list has no iterables')
for i in range(len(words)):
    if i == len(words) - 1:
        words[-1] = 'and ' + words[-1]
        words = ', '.join(words)
        return(words)  
```
```
['plants', 'rug', 'bars', 'crates', 'ashtray']
plants, rug, bars, crates, and ashtray
['ace', 'king', 'queen', 'jack', 'ten']
ace, king, queen, jack, and ten
0
error: list has no iterables
['apples', 'bananas', 'tofu', 'cats']
apples, bananas, tofu, and cats
>>> 
```      
<br>

**Lint & Logic Feedback — No Rewrite**:
Indentation: print('error: list has no iterables') is indented too far. That won’t cause an error, but it's not consistent with usual Python style.

Early return?: You're looping, but only returning on the last iteration. The rest of the loop does nothing. Does the loop need to run at all, or can you just handle that last element directly?

Mutating the list: You're modifying words[-1] directly. Ask yourself: what happens if this list is used later after calling written()?

Edge cases: What happens if words has only 1 item? Or 2 items? Try printing those scenarios and see if the output matches what you expect.

print() vs return: You print() the error for an empty list, but return the result in all other cases. Should it always return?


**Key Improvements & Notes**:
if not words is a cleaner Pythonic way to check for an empty list.

Handling single-item lists: We return the single item without adding a comma or "and".

Don't mutate the input list: Your original code changed words[-1] directly, which is risky. It’s better to leave the original list unchanged and construct the output string from slices.

Returning a string: The original print() was for error only — the corrected version consistently returns a string for all cases.

<hr><hr>

**corrected version**: