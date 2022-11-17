"""Input a string from user, create a list of only those words whose length is more than 5
characters. """

# a list comprehension to store the following in a list


def filter_word_list(word_collection):
    return [w for w in word_collection if len(w) > 5]


word_lst = input().split()
print(filter_word_list(word_lst))
