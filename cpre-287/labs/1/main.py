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


def generate():
    length = random.randint(3, 12)
    name = ""

    for i in range(length):
        if i == 0:
            character = random.choice(CHARACTERS).capitalize()
        else:
            last_character = name[-1].lower()
            has_second_last_character = i > 1
            second_last_character = (
                name[-2].lower() if has_second_last_character else None
            )
            last_two = f"{second_last_character}{last_character}"

            is_double_consonants = (
                has_second_last_character
                and last_character in CONSONANTS
                and second_last_character in CONSONANTS
                and second_last_character not in DOUBLE_COUNTING_EXCEPTIONS
                and last_two not in TRIPLE_COUNTING_EXCEPTIONS
            )

            is_double_vowels = (
                has_second_last_character
                and last_character in VOWELS
                and second_last_character in VOWELS
                and second_last_character not in DOUBLE_COUNTING_EXCEPTIONS
                and last_two not in TRIPLE_COUNTING_EXCEPTIONS
            )

            pool = None

            if is_double_consonants:
                pool = VOWELS
            elif is_double_vowels:
                pool = CONSONANTS
            else:
                pool = CHARACTERS

            character = random.choice(pool)

        name += character

    return name


print(generate())
