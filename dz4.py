def code(strochka):
    new_str = ''
    
    i = 0
    while i < len(strochka):
        count = 1

        while i + 1 < len(strochka) and strochka[i] == strochka[i + 1]:
            count += 1
            i += 1
        new_str += str(count) + strochka[i]
        i += 1
    return new_str
       
def decode(strochka):
    number = ''
    sim = ''
    for i in range(len(strochka)):
        if not strochka[i].isalpha():
            number += strochka[i]
        else:
            sim += strochka[i] * int(number)
            number = ''
    return sim

s = 'vvvvvddddddewww'
print(code(s))
print(decode(code(s)))