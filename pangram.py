def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()  # convert to lowercase
    for letter in alphabet:
        if letter not in s:
            return False
    return True
text = input("Enter a sentence: ")
if is_pangram(text):
    print("The string is a pangram.")
else:
    print("The string is NOT a pangram.")
