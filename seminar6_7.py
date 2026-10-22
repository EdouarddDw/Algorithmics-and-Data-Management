

def is_palindrom(s, start, end):
    if start < 0 | end >= len(s) | start > end :
        raise ValueError("invalid input to the function")
    else:
        sub_string = s[start:end + 1]
        if sub_string == sub_string[::-1]:
            return True
        else:
            return False

s = "abcdeffedcquipopz"

print("1.41")
print(is_palindrom(s, start= 5, end= 6))
print("1.4.2")
print(is_palindrom(s, start=3, end= 8))

print("1.4.3")
print(is_palindrom(s, start=3, end= 9))



print('Exercices 2:')

def find_pal(s, k):
    if k < 0:
        raise ValueError("index must be positve")
    for i in range(0, len(s) - k):
        substring = s[i:i+k]
        if substring == substring[::-1]:
            return substring
        else:
            continue
    return -1

s = "abcdeffedcquipopz"

print("2.2.3.1")
print(find_pal(s, k = 2))

print("2.2.3.2")
print(find_pal(s, k = 6))

print("2.2.3.2")
print(find_pal(s, k = 10))


print("test error")
print(find_pal(s, k = -6))



