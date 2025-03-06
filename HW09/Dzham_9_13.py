def create_latin_english_dictionary(n, english_latin_dict):
    latin_english_dict = {}

    for entry in english_latin_dict:
        english_word, translations = entry.split(' - ')
        latin_words = translations.split(', ')
        
        for latin_word in latin_words:
            if latin_word not in latin_english_dict:
                latin_english_dict[latin_word] = []
            latin_english_dict[latin_word].append(english_word)
    
    sorted_latin_english_dict = sorted(latin_english_dict.items())
    
    result = []
    for latin_word, english_words in sorted_latin_english_dict:
        result.append(f"{latin_word} - {', '.join(sorted(english_words))}")
    
    return result

n = int(input())
english_latin_dict = [input().strip() for _ in range(n)]

latin_english_dict = create_latin_english_dictionary(n, english_latin_dict)

print(len(latin_english_dict))
for entry in latin_english_dict:
    print(entry)
