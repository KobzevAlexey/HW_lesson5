# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = str(input('Введите какие-нибудь слова: '))
text = text.split()
fragment = str(input('Введите фрагмент чтобы удалить слово его содержащее: '))
new_text = []
for word in text:
    if fragment not in word:
        new_text.append(word)
print(' '.join(new_text))

