# print([i + j for i in "abc" for j in "def"])
# print([i.lower() for i in "HELLO"])
#
# text = "Zero One Two Three Four Five Six Seven Eight Nine"
# result = [word[0] + word[-1] for word in text.split()]
# print(result)
#
# result = [word[0] + word[-1] for word in text.split() if word[0] > word[-1]]
# print(result)
#
# text = "bangalore : city with lakes and punctures"
# result = [word for word in text.split() if word.startswith((‘a’,’e’,’I’,’o’,’u’)) ] -- > gives syntax error
# print(result)
