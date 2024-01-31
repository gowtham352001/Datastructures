def fetch_vowels(name):
    number_of_vowels = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(name)):
        if (name[i] in vowels):
            number_of_vowels += 1
    return number_of_vowels
print("Number of vowels in the given name is :", fetch_vowels("Gowtham KAnna"))



