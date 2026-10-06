def find_char_index(string, c):
    if string.find(c) != -1:
        return string.index(c)
    else:
        return False

#text out function
print(find_char_index('Edouard', 'b'))
print(find_char_index('Edouard', 'd'))


def is_palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False

#try if it works
print(is_palindrome("tets"))
print(is_palindrome("coloc"))

# perfect number

# strat with get_devisor helper function

def get_div(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)

    return div


print("get div 6")
print(get_div(6))

#now add perfect number function

def is_perfect(n):
    div = get_div(n)
    if sum(div) == n:
        return True
    else:
        return False

print(is_perfect(6))
print(is_perfect(7))

        


