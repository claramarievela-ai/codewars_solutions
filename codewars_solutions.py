# Solution 1: Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Solution 2: Convert a Number to a String
def number_to_string(num):
    return str(num)

# Solution 3: Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# Solution 4: Vowel Count
def get_count(sentence):
    count = 0
    for char in sentence:
        if char in "aeiou":
            count += 1
    return count