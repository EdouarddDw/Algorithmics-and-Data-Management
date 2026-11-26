
# exercices 1
def has_duplicate(arr):
    return len(arr) != len(set(arr))

test1 = [2,3,3,4,5]
test2 = [2,6,3,4,5]

print(has_duplicate(test1))
print(has_duplicate(test2))

def search_string(q, d):
    #build a dictionary d
    positions = []
    dic = {word: i for i, word in enumerate(d)}
    for word in q:
        positions.append(dic.get(word, -1))
    print(" ".join(str(p) for p in positions))

d = ["the" , "evening" , "and", "the", "morning" , "the" , "sky" , "is" , "blue" , "and" , "pink"]
q = ["morning" , "the" , "green" , "sky"]

search_string(q, d)
