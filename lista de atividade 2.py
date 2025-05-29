1#
n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))
if n1 > n2:
    print("O numero maior é:", n1)
elif n2 == n1:
    print("Os numeros sáo iguais")
else:
    n2 > n1
    print("O numero maior é:", n2)

2#
import math

n1 = float(input("Digite um numero:"))
if n1 >= 0:
    raiz = math.sqrt(n1)
    print("A raiz quadrada é:", raiz)
else:
    print("Numero negativo, tente outro numero")

3#
import math

n1 = float(input("Digite um número:"))
if n1 >= 0:
    raiz = math.sqrt(n1)
    print("A raiz quadrada é:", raiz)
else:
    quadrado = n1 ** 2
    print("O número é negativo ao quadrado é:", quadrado)


4#
import math

n1 = float(input("Digite um numero:"))
if n1 >= 0:
    quadrado = n1 ** 2
    raiz = math.sqrt(n1)
    print("O numero ao quadrado é:", quadrado)
    print("A raiz quadradan é:", raiz)
else:
    print("O numero não é positivo.")


5#
n1 = int(input("Digite um numero inteiro:"))

if n1 % 2 == 0:
    print("O numero é par.")
else:
    print("O numero é impar.")


6#
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

if n1 > n2:
    maior = n1
    diferenca = n1 - n2
else:
    maior = n2
    diferenca = n2 - n1

print("O maior número é:", maior)
print("A diferença entre eles é:", diferenca)



7#
n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

if n1 > n2:
    print("O maior número é:", n1)
elif n2 > n1:
    print("O maior número é:", n2)
else:
    print("Números iguais.")


8#
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

if 0 <= n1 <= 10 and 0 <= n2 <= 10:
    media = (n1 + n2) / 2
    print("A média das notas é:", media)
else:
    print("Nota inválida")


9#
s = float(input("Digite o salario:"))
p = float(input("Digite o valor da prestação:"))

if p > 0.2 * s:
    print("Emprestimo não concedido")
elif p < 0.2 * s:
    print("Emprestimo concedido")


10#
h = float(input("Digite a altura:"))
s = input("Digite M para masculino ou F para feminino:")

valores_validos = ("M", "m", "F", "f")

if s in valores_validos:
    if s == "M" or s == "m":
        ideal = (72.7 * h) - 58
        print("Peso ideal:", ideal)
    else:
        peso_ideal = (62.1 * h) - 44.7
        print("Peso ideal:", ideal)
else:
    print("Resposta invalida")

11#
n = int(input("Digite um numero inteiro maior que zero:"))

if n <= 0:
    print("Numero invalido")
else:
    soma = 0
    while n > 0:
        soma = soma + (n % 10)
        n = n // 10
    print("A soma dos algarismos é:", soma)


12#
import math

n1 = int(input("Digite um numero inteiro:"))

if n1 < 0:
    print("Numero invalido")
elif n1 == 0:
    print("Numero invalido")
else:
    logaritmo = math.log(n1)
    print("O logaritmo do número é:", logaritmo)


13#
n1 = float(input("Digite a nota da primeira prova:"))
n2 = float(input("Digite a nota da segunda prova:"))
n3 = float(input("Digite a nota da terceira prova:"))

media = (n1 * 1 + n2 * 1 + n3 * 2) / 4

print("A média ponderada é:", media)

if media >= 60:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

14#
n1 = float(input("Digite a nota do trabalho do laboratorio:"))
n2 = float(input("Digite a nota da avaliacao semestral:"))
n3 = float(input("Digite a nota do exame final:"))

media = (n1 * 2 + n2 * 3 + n3 * 5) / 10

print("A media ponderada é:", media)

if media >= 0 and media <= 2.9:
    print("Aluno reprovado")
elif media >= 3 and media <= 4.9:
    print("Aluno de recuperacao")
elif media >= 5 and media <= 10:
    print("Aluno aprovado")
else:
    print("valor invalido")

15#
#pesquisei e falaram que não tem função switch no python prof, fiz na mão mesmo. :c

n1 = int(input("Digite um numero de 1 a 7:"))

if n1 == 1:
    print("Domingo")
elif n1 == 2:
    print("Segunda-feira")
elif n1 == 3:
    print("Terca-feira")
elif n1 == 4:
    print("Quarta-feira")
elif n1 == 5:
    print("Quinta-feira")
elif n1 == 6:
    print("Sexta-feira")
elif n1 == 7:
    print("Sabado")
else:
    print("Digite um numero de 1 a 7.")


16#
#mesma coisa da questao passada.

n1 = int(input("Digite um numero de 1 a 12:"))

if n1 == 1:
    print("Janeiro")
elif n1 == 2:
    print("Fevereiro")
elif n1 == 3:
    print("Marco")
elif n1 == 4:
    print("Abril")
elif n1 == 5:
    print("Maio")
elif n1 == 6:
    print("Junho")
elif n1 == 7:
    print("Julho")
elif n1 == 8:
    print("Agosto")
elif n1 == 9:
    print("Setembro")
elif n1 == 10:
    print("Outubro")
elif n1 == 11:
    print("Novembro")
elif n1 == 12:
    print("Dezembro")
else:
    print("Escolha um numero de 1 a 12.")


17#
b1 = float(input("Digite a base maior:"))
b2 = float(input("Digite a base menor:"))
altura = float(input("Digite a altura:"))

if b1 <= 0 or b2 <= 0:
    print("Base invalida")
else:
    area = (b1 + b2) * altura / 2
    print("A area do trapezio e:", area)

18#
print("Menu de operacoes:")
print("1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

op = int(input("Escolha uma opcao:"))

if op >= 1 and op <= 4:
    n1 = float(input("Digite o primeiro valor:"))
    n2 = float(input("Digite o segundo valor:"))

    if op == 1:
        resultado = n1 + n2
        print("Resultado da soma é:", resultado)
    elif op == 2:
        resultado = n1 - n2
        print("Resultado da subtracao é:", resultado)
    elif op == 3:
        resultado = n1 * n2
        print("Resultado da multiplicacao é:", resultado)
    else:
        if n2 == 0:
            print("Divisao por zero na existe")
        else:
            resultado = n1 / n2
            print("Resultado da divisao é:", resultado)


19#
n1 = int(input("Digite um numero inteiro:"))

d3 = (n1 % 3 == 0)
d5 = (n1 % 5 == 0)

if d3 and not d5:
    print("O numero é divisivel por 3 e nao por 5")
elif d5 and not d3:
    print("O numero é divisivel por 5 e nao por 3")
else:
    print("Numero invalido")


20#
a = float(input("Digite o valor do lado A:"))
b = float(input("Digite o valor do lado B:"))
c = float(input("Digite o valor do lado C:"))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print("Triangulo equilatero")
    elif a == b or b == c or a == c:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")


21#
print("Escolha entre as opções abaixo:")
print("1 - Soma de 2 numeros")
print("2 - Diferenca entre 2 numeros")
print("3 - Produto entre 2 numeros")
print("4 - Divisao entre 2 numeros")

op = int(input("Digite a opção:"))

if op >= 1 and op <= 4:
    n1 = float(input("Digite o primeiro numero:"))
    n2 = float(input("Digite o segundo numero:"))

    if op == 1:
        resultado = n1 + n2
        print("Resultado da soma é:", resultado)
    elif op == 2:
        if n1 > n2:
            resultado = n1 - n2
        else:
            resultado = n2 - n1
        print("Resultado da diferenca é:", resultado)
    elif op == 3:
        resultado = n1 * n2
        print("Resultado do produto é:", resultado)
    elif op == 4:
        if n2 == 0:
            print("Escolha um numero diferente de zero")
        else:
            resultado = n1 / n2
            print("Resultado da divisao é:", resultado)
else:
    print("ERRO! Opção invalida")


22#
i = int(input("Digite a idade:"))
t = int(input("Digite o tempo de servico:"))

if i >= 65 or t >= 30 or (i >= 60 and t >= 25):
    print("Pode se aposentar")
else:
    print("Nao pode se aposentar")


23#
a = int(input("Digite o ano:"))

if (a % 400 == 0) or (a % 4 == 0 and a % 100 > 0):
    print("O ano e bissexto")
else:
    print("O ano nao e bissexto")


24#
v = float(input("Digite o valor do produto:"))
e = input("Digite o estado (MG, SP, RJ ou MS):")

if e == "MG":
    i = 0.07
    t = v + (v * i)
    print("O preco final é:", t)
elif e == "SP":
    i = 0.12
    t = v + (v * i)
    print("O preco final é:", t)
elif e == "RJ":
    i = 0.15
    t = v + (v * i)
    print("O preco final é:", t)
elif e == "MS":
    i = 0.08
    t = v + (v * i)
    print("O preco final é:", t)
else:
    print("Escolha um dos estados mencionados.")


25#
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

if a == 0:
    print("Nao é equação do segundo grau")
else:
    d = b ** 2 - 4 * a * c

    if d < 0:
        print("Nao existe raiz")
    elif d == 0:
        r = -b / (2 * a)
        print("Raiz unica:", r)
    else:
        r1 = (-b + d ** 0.5) / (2 * a)
        r2 = (-b - d ** 0.5) / (2 * a)
        print("Primeira raiz:", r1)
        print("segunda raiz:", r2)

26#
km = float(input("Digite a distancia em Km:"))
l = float(input("Digite a quantidade de litros consumido:"))

kml = km / l

if kml < 8:
    print("Venda o carro!")
elif kml >= 8 and kml <= 14:
    print("Economico!")
else:
    print("Super economico!")


27#
i = int(input("Digite a idade do nadador:"))

if 5 <= i <= 7:
    print("Categoria: Infantil A")
elif 8 <= i <= 10:
    print("Categoria: Infantil B")
elif 11 <= i <= 13:
    print("Categoria: Juvenil A")
elif 14 <= i <= 17:
    print("Categoria: Juvenil B")
elif i >= 18:
    print("Categoria: Senior")


28#
x = int(input("Digite o primeiro numero:"))
y = int(input("Digite o segundo numero:"))
z = int(input("Digite o terceiro numero:"))

print("Escolha o tipo de media:")
print("(a) Geometrica")
print("(b) Ponderada")
print("(c) Harmonica")
print("(d) Aritmetica")
op = input("Digite a opcao:")

if op == "a":
    m = (x * y * z) ** (1/3)
    print("Media geometrica é:", m)
elif op == "b":
    m = (1 * x + 2 * y + 3 * z) / 6
    print("Media ponderada é:", m)
elif op == "c":
    m = 3 / ((1/x) + (1/y) + (1/z))
    print("Media harmonica é:", m)
elif op == "d":
    m = (x + y + z) / 3
    print("Media aritmetica é:", m)

29#
import random

acertos = 0

for i in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print("Qual é a soma de:", a, "+", b, "?")
    r = int(input("Resposta:"))
    c = a + b
    if r == c:
        acertos = acertos + 1

print("Voce acertou", acertos, "de 5 perguntas")

30#
a = int(input("Digite o primeiro numero:"))
b = int(input("Digite o segundo numero:"))
c = int(input("Digite o terceiro numero:"))

lista = [a, b, c]
lista.sort()

print("so umeros em ordem crescente:", lista[0], lista[1], lista[2])

31#
a = float(input("Digite a altura:"))
p = float(input("Digite o peso:"))

if a < 1.20:
    if p <= 60:
        print("Classificacao: A")
    elif p <= 90:
        print("Classificacao: D")
    else:
        print("Classificacao: G")
elif a <= 1.70:
    if p <= 60:
        print("Classificacao: B")
    elif p <= 90:
        print("Classificacao: E")
    else:
        print("Classificacao: H")
else:
    if p <= 60:
        print("Classificacao: C")
    elif p <= 90:
        print("Classificacao: F")
    else:
        print("Classificacao: I")


32#
c = int(input("Digite o codigo do produto:"))
q = int(input("Digite a quantidade:"))

if c == 100:
    preco = 1.20
elif c == 101:
    preco = 1.30
elif c == 102:
    preco = 1.50
elif c == 103:
    preco = 1.20
elif c == 104:
    preco = 1.70
elif c == 105:
    preco = 2.20
elif c == 106:
    preco = 1.00
else:
    preco = 0

if preco == 0:
    print("Codigo invalido")
else:
    total = preco * q
    print("Valor a pagar:", total)

33#
pa = float(input("Digite o preco antigo:"))

if pa <= 50:
    percentual = 0.05
elif pa <= 100:
    percentual = 0.10
else:
    percentual = 0.15

pn = pa + (pa * percentual)

print("preco antigo:", pa, ", Novo preco:", pn)

if pn <= 80:
    mensagem = "Barato"
elif pn <= 120:
    mensagem = "Normal"
elif pn <= 200:
    mensagem = "Caro"
else:
    mensagem = "Muito caro"

print(mensagem)

34#
n = float(input("Digite a nota:"))
f = int(input("Digite as faltas: "))

if f > 20:
    if n >= 9.0 and n <= 10.0:
        c = "B"
    elif n >= 7.5 and n <= 8.9:
        c = "C"
    elif n >= 5.0 and n <= 7.4:
        c = "D"
    elif n >= 4.0 and n <= 4.9:
        c = "E"
    elif n >= 0.0 and n <= 3.9:
        c = "E"

else:
    if n >= 9.0 and n <= 10.0:
        c = "A"
    elif n >= 7.5 and n <= 8.9:
        c = "B"
    elif n >= 5.0 and n <= 7.4:
        c = "C"
    elif n >= 4.0 and n <= 4.9:
        c = "D"
    elif n >= 0.0 and n <= 3.9:
        c = "E"
print("Conceito:", c)


35#
dia = int(input("Digite o dia:"))
mes = int(input("Digite o mês:"))
ano = int(input("Digite o ano:"))

bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

if mes == 2:
    max_dia = 29 if bissexto else 28
elif mes in [4, 6, 9, 11]:
    max_dia = 30
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    max_dia = 31
else:
    max_dia = 0

if max_dia == 0:
    print("Mês incorreto.")
elif 1 <= dia <= max_dia:
    print("Data valida:", dia, "/", mes, "/", ano)
else:
    print("Dia incorreto.")


36#
v = float(input("Digite o valor da venda mensal:"))

if v >= 100000:
    c = 700 + (v * 0.16)
elif v >= 80000:
    c = 650 + (v * 0.14)
elif v >= 60000:
    c = 600 + (v * 0.14)
elif v >= 40000:
    c = 550 + (v * 0.14)
elif v >= 20000:
    c = 500 + (v * 0.14)
else:
    c = 400 + (v * 0.14)

print("A comissão do vendedor será de R$", c)


38#
a_atual = 2008

d = int(input("Dia:"))
m = int(input("Mes:"))
a = int(input("Ano:"))

valido = True

if a > a_atual or m < 1 or m > 12 or d < 1:
    valido = False
else:
    if m == 2:
        if (a % 4 == 0 and a % 100 > 0) or (a % 400 == 0):
            if d > 29:
                valido = False
        else:
            if d > 28:
                valido = False
    elif m in [4, 6, 9, 11]:
        if d > 30:
            valido = False
    else:
        if d > 31:
            valido = False

if valido:
    print("data valida")
else:
    print("data invalida")


40#
cf = float(input("Digite o custo de fábrica do carro:"))

if cf <= 12000:
    c = cf * 0.05
    i = 0
elif cf <= 25000:
    c = cf * 0.10
    i = cf * 0.15
else:
    c = cf * 0.15
    i = cf * 0.20

total = cf + c + i

print("O custo ao consumidor é:", total)

41#
p = float(input("Digite o peso:"))
a = float(input("Digite a altura:"))

imc = p / (a * a)

if imc < 18.5:
    c = "Abaixo do Peso"
elif imc <= 24.9:
    c = "Saudável"
elif imc <= 29.9:
    c = "Peso em excesso"
elif imc <= 34.9:
    c = "Obesidade Grau I"
elif imc <= 39.9:
    c = "Obesidade Grau II (severa)"
else:
    c = "Obesidade Grau III (mórbida)"

print("Seu IMC é:", imc)
print("Classificação:", c)

