"""WAF: uncommon_words() that takes two sentences (strings)
as its arguments, and returns the common words in both the sentences.
[Hint: store all the in a set. Read the documentation for set.]
"""


def find_common_words_set(sentence1, sentence2):
    # code here
    s1 = set(sentence1)
    s2 = set(sentence2)
    s3 = s1.intersection(s2)
    return s3


def uncommon_words(first_sentence, second_sentence):
    s1 = set(first_sentence)
    s2 = set(second_sentence)
    s3 = find_common_words_set(first_sentence, second_sentence)
    s4 = (s1 - s3).union(s2 - s3)
    return s4


sentence_1 = input().split()
sentence_2 = input().split()

print(*uncommon_words(sentence_1, sentence_2))
