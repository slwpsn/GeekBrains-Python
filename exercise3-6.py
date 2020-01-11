def int_func(text):
    return text.capitalize()

text = input('Введите любой текст из маленьких латинских букв, мы сделаем первую букву первого слова прописной: ')
print(int_func(text))

text2 = list(input('А теперь напишите несколько слов, а мы сделаем прописной первую букву каждого слова: ').split())

for i in range(len(text2)):
    text2[i] = int_func(text2[i])
print(*text2)
