"""Check Palindrome"""

word = 'reviver'
word2 = 'revivers'
print(word.find(word[::-1]), '+', 1, '=', word.find(word[::-1]) + 1)
p1 = bool(word.find(word[::-1]) + 1)
print(p1)
print(word2.find(word2[::-1]), '+', 1, '=', word2.find(word2[::-1]) + 1)
p2 = bool(word2.find(word2[::-1]) + 1)
print(p2)

print("----------------------------Next item -------------------------------")
"""all of the below evaluate to False.
Everything else will evaluate to True in Python.
"""
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))
