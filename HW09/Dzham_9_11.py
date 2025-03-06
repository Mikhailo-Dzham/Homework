import re

def check_essay(n, m, dictionary, essay):
    dictionary_set = set(word.lower() for word in dictionary)
    essay_words = re.findall(r'\b\w+\b', essay.lower())
    essay_set = set(essay_words)
    
    if not essay_set.issubset(dictionary_set):
        return "Some words from the text are unknown."
    
    if not dictionary_set.issubset(essay_set):
        return "The usage of the vocabulary is not perfect."
    
    return "Everything is going to be OK."

n, m = map(int, input().split())
dictionary = [input().strip() for _ in range(n)]
essay = ' '.join(input().strip() for _ in range(m))

print(check_essay(n, m, dictionary, essay))
