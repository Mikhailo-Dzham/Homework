def lyoha_separatist(txt):
    with open('lyohas_file.txt', 'w') as f:
        for line in range (0, len(txt), 40):
            print(txt[line:(line + 40)], file=f)


#############################

lyoha_separatist(input())