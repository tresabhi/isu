# CPRE 287 Lab 1

## Approach

I first decided to take it slow and start off by declaring all the constants. I.e. the list of consonants, vowels, exceptions to the rules like the character `y` and the two letter combos like `sh`, `th`, and `ch`.

With the constants declared, using the random library's `randint` function, I generated the number of characters that I must have for the name and started looping using the `range` function and `i` to keep track of the indices.

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

## What method or library did you use to generate random characters, and why did you choose that approach?

I used the `random` library because it comes built into Python.

## What steps did you take to ensure each character in the name is truly random while implementing the rules?

Please see the double counting check above (the numbered list).

## How did you test the generator to ensure all the requirements were met? Can you describe your testing process and provide examples of names your generator produced?

I just ran it a bunch of times to cover all edge cases and recorded a few for this writeup.

- `Poyhnuc` proves the algorithm's handing of the "y" exception as "h" and "n" are allowed even after "y".
- `Pjaalyq`, among many others, proves the algorithm stops using vowels when double consonants are present. Here, "l" was used after "aa".
- `Chroot` proves the algorithm allowed "r" after "c" and "h" because "ch" is a part of the triple count exception list.

## Errors

The only error I encountered was running the wrong command because I pressed the up arrow one too many times and ended up running:

```bash
clear; bun dev --host
```

That's a command for my encyclopedia; of course, without a Node.JS project, why would it do anything. For reference, this is the command that I meant to run (Windows, PowerShell):

```ps
clear; python .\cpre-287\labs\1\main.py
```

## Solution

The solution is available in this write up and also on Canvas.

```py
# We of course start off importing the ever necessary random module.
import random

# The list function used on a string splits up every single character into its
# own entry in the list.
CONSONANTS = list("bcdfghjklmnpqrstvwxyz")
VOWELS = list("aeiou")
CHARACTERS = CONSONANTS + VOWELS

# Here are the exceptions to the rules listed in the assignment. Namely, y acts
# like neither a vowel or a consonant, so it's exempt from the double counting
# rules.
DOUBLE_COUNTING_EXCEPTIONS = list("y")

# As for triple counting, it allowed if these pairs are present in them.
TRIPLE_COUNTING_EXCEPTIONS = ["sh", "th", "ch"]


# This is the primary function of this toy program. No parameters needed here.
def main():

    # Length is generated immediately along with an empty name.
    length = random.randint(3, 12)
    name = ""

    # Loop through easily using the range function. Note that i will only reach
    # the length - 1.
    for i in range(length):

        # If this is the first character, all characters are allowed, no
        # restrictions. Furthermore, the first character is capitalized.
        if i == 0:
            character = random.choice(CHARACTERS).capitalize()
        else:

            # Grab the last character as it'll be useful for all the rules
            # later. Oh, and I make it lower case because the first character
            # is capitalized.
            last_character = name[-1].lower()

            # The second last character may not exist early on in the loop so I
            # declare a boolean for it.
            has_second_last_character = i > 1

            # Fetch the second last character if it exists. If not, I set it to
            # None but that's not important as none of the code later checks if
            # this is None; the boolean above is used.
            second_last_character = (
                name[-2].lower() if has_second_last_character else None
            )

            # Finally, I just combine the last two characters into one string
            # as it will be useful for the three character rule. Note that if
            # we're still early in the loop and there is no second last
            # character, we just use the last character which will fail the
            # check within TRIPLE_COUNTING_EXCEPTIONS, guaranteed.
            last_two = (
                f"{second_last_character}{last_character}"
                if has_second_last_character
                else last_character
            )

            # Now we check if we have double consonants on our hands.
            is_double_consonants = (
                # First we make sure we even have a second last character.
                has_second_last_character
                # Both of these characters must be constants to be a double
                # consonant.
                and last_character in CONSONANTS
                and second_last_character in CONSONANTS
                # y is an exception to the double consonant rule.
                and last_character not in DOUBLE_COUNTING_EXCEPTIONS
                and second_last_character not in DOUBLE_COUNTING_EXCEPTIONS
                # Exempt the preset combos. In other words, if they show up,
                # it's fine to not consider it as a double consonant.
                and last_two not in TRIPLE_COUNTING_EXCEPTIONS
            )

            # Literally the exact same logic as above but for vowels.
            is_double_vowels = (
                has_second_last_character
                and last_character in VOWELS
                and second_last_character in VOWELS
                and last_character not in DOUBLE_COUNTING_EXCEPTIONS
                and second_last_character not in DOUBLE_COUNTING_EXCEPTIONS
                and last_two not in TRIPLE_COUNTING_EXCEPTIONS
            )

            # By pool here, I mean the pool of characters to choose from.
            pool = None

            # If we're already hitting a double consonant, we must choose from
            # vowels.
            if is_double_consonants:
                pool = VOWELS

            # Vice versa.
            elif is_double_vowels:
                pool = CONSONANTS

            # And if we're not double consonants or double vowels, we have full
            # freedom.
            else:
                pool = CHARACTERS

            # random.choice makes it real easy to choose from the pool.
            character = random.choice(pool)

        # Finally, no matter what if else branch the code went down, we have a
        # character to append so I do it here.
        name += character

    # Return the name.
    return name


if __name__ == "__main__":
    print(main())
```
