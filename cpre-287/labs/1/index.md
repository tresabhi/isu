# CPRE 287 Lab 1

## Approach

I first decided to take it slow and start off by declaring all the constants. I.e. the list of consonants, vowels, exceptions to the rules like the character `y` and the two letter combos like `sh`, `th`, and `ch`.

With the constants declares, using the random library's `randint` function, I generated the number of characters that I must have for the name and started looping using the `range` function and `i` to keep track of the indices.

Feeling overwhelmed by the rules and exceptions, I decided to simply handle the easiest case first: the first character. This special letter has the opportunity to be picked from any character in the English alphabet. I do this when `i == 0` and capitalize.

If we're past the first iteration of the loop, I started listing off as many important pieces of information that I know I will need in the future. This includes:

- The last character
- A boolean to dictate wether or not the second last character exists
- The second last character (this is `None` on the very second iteration)
- The last two characters combined (to check for the two letter combos)

Then, I declared two composite booleans dictating wether there are two consonants or vowels in a row. They are two if and only if:

1. There is a second last character
2. The last character is a consonant
3. The second last character is a consonant
4. The last character is not a double counting exception (y)
5. The second last character is also not a double counting exception
6. The last two characters combined do not include `sh`, `th`, or `ch`

The same is done, but for vowels. Then, an empty pool variable is declared which will hold all valid list of characters. The pool is filled with vowels if we had double consonants and vice versa. If we had neither double consonants nor double vowels, then all characters are allowed. Finally, the random character is picked from the pool and appended to the name.

## Errors

The only error I encountered was running the wrong command because I pressed the up arrow one too many times and ended up running:

```bash
clear; bun dev --host
```

That's a command for my encyclopedia; of course, without a Node.JS project, why would it do anything. For reference, this is the command that I meant to run (Windows, PowerShell):

```ps
clear; python .\cpre-287\labs\1\main.py
```
