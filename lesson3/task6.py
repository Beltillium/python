def int_func(text):
    text_buffer = chr(ord(text[0])-32) + text[1:]
    return text_buffer


text_result = str()
text_input = input('Введите слово из маленьких латинских слов: ').split()
for i in text_input:
    text_result += int_func(i) + ' '
print(f'{text_result}')
