minha_lista_de_compras = ['Sabao', 'Arroz', 'Feijao', '10', [1, 2, 3]]

for coisa in minha_lista_de_compras:
    print (coisa)


# Slice

print('*' * 20)
print('*******Slices*******')
print('*' * 20)

n = [0,1,2,3,4,5,6,7,8,9]

n[0] # 0
n[6:] # [6,7,8,9]
n[:-6] # [0,1,2,3]
n[::2] # [0,2,4,6,8]

# [De onde : Até onde : de quanto em quanto]
# [2 : 10 : 3]

for coisa in minha_lista_de_compras:
    print (coisa[::-1])

# >>> matriz = [[0,1,2], [3,4,5], [7,8,9]]

# >>> matriz[0] #[0,1,2]
# >>> matriz[0][1:] #[1,2]

# >>> matriz3d = [[[0,0,0]], [[0,0,0]]]
# >>> matriz3d[0][0][0] # 0

# Métodos
print('*' * 20)
print('*******Métodos*******')
print('*' * 20)

# >>> x = [1,2,3]

# >>> x.append(4) #[1,2,3,4]

# >>> x.insert(4,0) #[1,2,3,0]

# >>> x.count(2) #[1]

# >>> x.remove(2) #[1,3]

# >>> x.append(4) #[1,2,3,4]

# >>> x.pop() # 3 | #[1,2]

# >>> x.reverse() #None | #[3,2,1]

lista_de_compras = []
resposta = ''

while resposta == 'acabou':
    reposta = input('O que temos que comrpar?  ')
    if reposta != 'acabou':
        lista_de_compras.append(reposta)

print(lista_de_compras)