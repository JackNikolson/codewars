# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    result = []
    for letter in text:
        result.append(letter.lower())

    duplicates = [x for x in result if result.count(x) >= 2]
    print(duplicates)
    return len(set(duplicates))

print(duplicate_count('abcdeaB'))

     