def frequency_of_words(str):
    lst = str.split()
    l1 = len(lst)
    d = {lst[i]: lst.count(lst[i]) for i in range(l1)}
    return d


print(frequency_of_words('count the words in the sentence in'))
