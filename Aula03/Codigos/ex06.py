# Programa para calcular a media de um aluno
print('Programa para calcular a media de um aluno\n')

nome = raw_input('Entre com o nome do aluno: ')
nota1 = float(raw_input("Entre com a primeira nota: "))
nota2 = float(raw_input("Entre com a segunda nota: "))
media = (nota1 + nota2)/2
print('{0} teve media igual a: {1:.2f}'.format(nome, media))
