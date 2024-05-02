# https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

def encode(st: str):
    new_str = ''
    encoded = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5'
    }
    
    for i in st:
        if i not in encoded.keys():
            new_str += i
        
        else:
            new_str += encoded[i]
    
    return new_str

def decode(st: str):
    new_str = ''
    decoded = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }
    
    for i in st:
        if i not in decoded.keys():
            new_str += i
        
        else:
            new_str += decoded[i]
    
    return new_str
