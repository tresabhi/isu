import numpy as np

DROP = 5

# generate 25 random grades between 70 and 100
grades = np.array(np.random.randint(70, 101, 25))

print(grades)
print(f"Average before dropped: {np.mean(grades)}")

# now drop 5 lowest grades
grades = np.delete(grades, np.argpartition(grades, DROP)[:DROP])
print(grades)
print(f"Average after dropped: {np.mean(grades)}")
