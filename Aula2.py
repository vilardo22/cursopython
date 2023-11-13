#n1=int (input ('Digite um numero:'))
#n2= int (input ('Digite mais um numero:'))
#s= n1 + n2
#print('A soma é', s)

#n= float (input ('Digite um Valor:'))
#print(n)

#Crie um progrma que leia dois numeros e mostre a soma entre eles.
#n1 =int (input('Digite um valor: '))
#n2 = int (input('Digite outro valor: '))
#s= n1 + n2

#print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))

#Faça um programa que leia algo  no teclado e mostre na tela o seu tipo primitivo e todas as informções sobre ela
#a = input('Digite algo: ')
#print('O tipo primitivo desse valor é', type(a))

#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor
#n = int(input('Digite um número:'))
#a = n - 1
#s = n + 1
#print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))


#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

#n = int(input('Digite um número '))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print('O dobro de {} vale {}.'.format(n, d))
#print('O triplo de {} vale {}.'.format(n, t))
#print('A raiz quadrada de {} vale {:.2f}.'.format(n, r))

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media.

#n1 = float(input('Primeira nota do aluno: '))
#n2 = float(input('Segunda nota do aluno: '))
#m = (n1 + n2) / 2
#print ('A media do aluno  é igual a {:.1f}'.format(m))

#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

#medida = float(input('Uma distância em metros: '))
#cm = medida * 100
#mm = medida * 1000
#print('A media de {}m correspondente a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

#Fça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

#num = int(input('Digite um número para ver sua tabuada: '))
#print ('-' * 12)
#print('{} x {:2} = {}'.format(num, 1, num*1))
#print('{} x {:2} = {}'.format(num, 2, num*2))
#print('{} x {:2} = {}'.format(num, 3, num*3))
#print('{} x {:2} = {}'.format(num, 4, num*4))
#print('{} x {:2} = {}'.format(num, 5, num*5))
#print('{} x {:2} = {}'.format(num, 6, num*6))
#print('{} x {:2} = {}'.format(num, 7, num*7))
#print('{} x {:2} = {}'.format(num, 8, num*8))
#print('{} x {:2} = {}'.format(num, 9, num*9))
#print('{} x {:2} = {}'.format(num, 10, num*10))
#print ('-' * 12)

#Crie um programa que leia quanto dinheiro uma pessoa 
#tem na carteira e mostre quantos dolare ela pode comprar

#real = float(input('Quanto dinheiro você tem na carteira? R$ '))
#dolar = real / 3.27
#print('Com R${:.2f} você poe comprar US${:.2f}'.format(real,dolar))

#Faça um programa que leia largura e altura da parede em mtrs e calcule a area e quanto de tinta vai usar

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisa de {}L de tinta.'.format(tinta))
