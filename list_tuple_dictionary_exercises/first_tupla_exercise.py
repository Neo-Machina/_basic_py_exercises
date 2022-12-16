# 4. Data la tupla: frutta = ("mela", "mango", "papaya", "ananas", "ciliegia") eseguire
# l’unpack in: verde, tropicale, rosso.

frutta = ("mela", "mango", "papaya", "ananas", "ciliegia")

(verde, *tropicale, rosso) = frutta

print(verde, tropicale, rosso)

frutti_tropicali = ''
for frutto_tropicale in tropicale:
    frutti_tropicali += f'{frutto_tropicale} '

print(f'La {verde} è un frutto di colore verde')
print(f'{frutti_tropicali} sono frutti tropicali')
print(f'la {rosso} è un frutto di colore rosso')