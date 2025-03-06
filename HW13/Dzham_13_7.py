#Вписуємо назву файла без '.txt' в наступному рядкувідповідний варіант задачі
#Через пробіл замість файла буде відкриватися 'test.txt' що дуже зручно тестувати

def variants(var):
    if var == 'a':
        a_longest_word(file_name)
    elif var == 'b':
        b_words_count(file_name)
    elif var == 'c':
        c_cleaner_spaces(file_name)
    elif var == 'd':
        d_cleaner_plus(file_name)
    elif var == 'e':
        e_ninty_symbol(file_name)

def a_longest_word(f_name):
    with open(f_name, 'r', encoding='utf-8') as f:
        string_txt = f.read().split()
        max_len_word = ''
        for word in string_txt:
            if len(max_len_word) < len(word):
                max_len_word = word
    print(max_len_word)

def b_words_count(f_name):
    with open(f_name, 'r', encoding='utf-8') as f:
        string_txt = f.read().split()
    print(len(string_txt))

def c_cleaner_spaces(f_name):
    cleaned_text = []
    with open(f_name, 'r', encoding='utf-8') as f:
        for line in f:
            string_txt = line.split()
            string_txt = " ".join(string_txt)
            cleaned_text.append(string_txt)
    writer(cleaned_text)

def d_cleaner_plus(f_name):
    cleaned_text = []
    with open(f_name, 'r', encoding='utf-8') as f:
        for line in f:
            string_txt = line.split()
            string_txt = [word for word in string_txt if len(word) > 1]
            cleaned_text.append(" ".join(string_txt))
    writer(cleaned_text)

def e_ninty_symbol(f_name):
    remastered_txt = []
    with open(f_name, 'r', encoding='utf-8') as f:
        for line in f:
            string_txt = line.split()
            line = line.strip()
            length_char = 0
            length_all = len(line)

            if len(string_txt) > 1:
                for el in string_txt:
                    length_char += len(el)
                length_space = ' ' * ((80 - length_all)//(len(string_txt) - 1))
                ost_space = (80 - length_all) % (len(string_txt) - 1)
                for i in range(ost_space):
                    string_txt[i] = string_txt[i] + ' '
                string_txt = length_space.join(string_txt)
                remastered_txt.append(string_txt)
            else:
                remastered_txt.append(line)
    writer(remastered_txt)



def writer(text):
    with open('H.txt', 'w', encoding='utf-8') as f:
        for line in text:
           f.write(line + '\n')




##################################################3333

print("Назва файла без '.txt':")
file_name = input() + '.txt'
var_ = input()
if file_name == '.txt':
    file_name = 'test.txt'
variants(var_)