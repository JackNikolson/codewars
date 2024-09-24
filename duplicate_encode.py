# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
def duplicate_encode(word):
    word_lower = word.lower()

    return ''.join('(' if word_lower.count(char) == 1 else ')' for char in word_lower)


print(duplicate_encode('hello'))
print(duplicate_encode('kasd,d'))
