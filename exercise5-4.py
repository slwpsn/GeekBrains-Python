englword = ['One', 'Two', 'Three', 'Four']
rusword = ['Один', 'Два', 'Три', 'Четыре']

in_f = open('text4.txt')
out_f = open('text4-1.txt', 'w')

for i in range(4):
    for line in in_f:
        out_f.write(line.replace(englword[i], rusword[i]))
        i += 1

in_f.close()
out_f.close()
