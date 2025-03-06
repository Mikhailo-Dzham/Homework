incoming_str = input()
output_str = ""
for i in range(len(incoming_str)):
    if incoming_str[i] in "qwertyuiopasdfghjklzxcvbnm" or incoming_str[i] in "qwertyuiopasdfghjklzxcvbnm".upper():
        output_str += incoming_str[i] * 2
    else:
        output_str += incoming_str[i]
print(output_str)