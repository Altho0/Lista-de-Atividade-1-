#lista de atividade 3

#1
print("Os cinco primeiros múltiplos de 3 são:")
for i in range(1, 6):
    múltiplos = 3 * i
    print (múltiplos)

#2
print("Contagem: ")
for i in range(1, 101):
    print (i)

contagem = 1
while contagem <= 100:
    print(contagem)
    contagem += 1

#3
contagem = 1 
while contagem <= 10:
    print(contagem)
    contagem += 1
print ("Fim")


#4
contagem = 0
while contagem <= 100000:
    print(contagem)
    contagem += 1000

#5
soma = 0 
for i in range(10):
    valores = int(input("Digite os valores: "))
    soma += valores
print(soma) 

#6
media = 0
for i in range(10):
    valores = int(input("Digite os valores: "))
    media += valores 
print(media / 10)

#7
media = 0
contador = 0
for i in range(10):
    positivos = int(input("Digite os valores positivos: "))
    if positivos %2== 0: 
        media += positivos
        contador += 1 
print(media / contador)

#8
lista = [ ]
for i in range(10): 
    numeros = int(input("Digite os numeros: "))
    lista.append(numeros)
print (max(lista) , min(lista))

#9
lista = [ ]
for i in range(10):
    impares = int(input("Digite os valores: "))
    if impares %2!= 0: 
        lista.append(impares)
print(lista)

#10
soma = 0
for i in range(50):
    if i %2== 0:
        soma += i
print(soma)

#11
n = int(input("Digite um número: "))
print("Contagem: ")
for i in range(0, n + 1):
    print(i)

#12
n = int(input("Digite um número: "))
print("Contagem: ")
for i in range(n ,-1 , - 1):
    print (i)

#13
n = int(input("Digite um número: "))
print("Contagem: ")
for i in range(0, n + 1):
    if i %2== 0:
     print(i)

#14
n = int(input("Digite um número: "))
print("Contagem: ")
for i in range(n ,-1 , - 1):
   if i %2== 0:
      print(i) 

#15
n = int(input("Digite um número: "))
print("Contagem: ")
for i in range(0, n + 1):
    if i %2!= 0:
        print(i)

#16
n = int(input("Digite um número: "))
print("Contagem: ")
for i in range(n ,-1 , - 1):
  if i %2!= 0:
        print(i)   

#17
n = int(input("Digite um número: "))
print("Soma dos números: ")
multi = 0
for i in range(n , 0, - 1):
    multi += i
print(multi)

#18
vezes = 1
quantidade = int(input("Digite a quantidade de números: "))
maior = 0
for i in range(quantidade):
    valor = int(input("Digite o valor: "))
    if valor > maior:
        maior = valor  
        vezes = 1
    elif valor == maior: 
        vezes += 1
print(maior)
print(vezes)

#19
numero = int(input("Digite o número entre 100 e 999: "))

while(numero < 100 or numero > 999):

       print(f'Número {numero} invalido, digite novamente.')
       numero = int(input("Digite o número entre 100 e 999: "))
centenas = numero//100
dezenas = (numero - centenas*100)//10
unidades = numero - (centenas*100 + dezenas*10)
print(f'O número {numero} equivale a {centenas*100} + {dezenas*10} + {unidades}')

20#
total = 0
pares = 0
numero = 0

while numero != 1000:
    numero = int(input())
    if numero != 1000:
        total = total + 1
        if numero % 2 == 0:
            pares = pares + 1

print("Total de números lidos:", total)
print("Quantidade de pares:", pares)

21#

inicio = int(input())
fim = int(input())

soma_pares = 0
mult_impares = 1

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma_pares = soma_pares + i
    else:
        mult_impares = mult_impares * i

print("Soma dos pares:", soma_pares)
print("Multiplicação dos ímpares:", mult_impares)

22#
soma = 0
quantidade = 0

while True:
    nota = float(input())
    if nota < 10 or nota > 20:
        break
    soma = soma + nota
    quantidade = quantidade + 1

if quantidade > 0:
    media = soma / quantidade
    print("Média:", media)
else:
    print("Nenhuma nota válida foi digitada.")

23#

n = int(input())

for i in range(1, n + 1):
    if n % i == 0:
        print(i)


n = int(input())
soma = 0

24#
for i in range(1, n):
    if n % i == 0:
        soma = soma + i

print("Soma dos divisores:", soma)

soma = 0

25#
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        soma = soma + i

print("Soma:", soma)

26# 
n = int(input())

while True:
    n = n + 1
    if n % 11 == 0 or n % 13 == 0 or n % 17 == 0:
        print("Primeiro múltiplo:", n)
        break
        
27# 
n = int(input())
h = 0

for i in range(1, n + 1):
    h = h + 1 / i

print("H(n) =", h)


28# 
n = int(input("Digite um número inteiro positivo: "))
e = 1

for i in range(1, n + 1):
    f = 1
    for j in range(1, i + 1):
        f *= j
    e += 1 / f

print("Valor de E:", e)

29#



numero_termos = 5
soma = 0.0

for k in range(numero_termos):
    # calcula o fatorial de (2*k)
    fatorial = 1
    limite = 2 * k
    for j in range(1, limite + 1):
        fatorial = fatorial * j

    termo = k / fatorial
    soma = soma + termo
    
    print("Termo", k+1, ":", k, "/", limite, "! =", termo)


print("Valor de S com", numero_termos, "termos:", soma)

30#

numero_final = int(input("Digite o valor de n: "))
soma_total = 0
for inteiro_atual in range(1, numero_final + 1):
    soma_total = soma_total + inteiro_atual
print("Resultado da soma de 1 até", numero_final, ":", soma_total)


numero_de_termos = int(input("Digite o número de termos n: "))
soma_das_potencias = 0
for contador_de_termos in range(1, numero_de_termos + 1):
    base_do_termo = 2 * contador_de_termos - 1
    expoente_do_termo = 2 * contador_de_termos
    resultado_potencia = 1
    for repeticao in range(expoente_do_termo):
        resultado_potencia = resultado_potencia * base_do_termo
    soma_das_potencias = soma_das_potencias + resultado_potencia
print("Resultado da soma das potências:", soma_das_potencias)

numero_de_termos = int(input("Digite o número de termos n: "))
soma_numeros_impares = 0
for contador in range(1, numero_de_termos + 1):
    termo_impar_atual = 2 * contador - 1
    soma_numeros_impares = soma_numeros_impares + termo_impar_atual
print("Resultado da soma dos ímpares:", soma_numeros_impares)

31#
soma = 0
for i in range(1, 51):
    soma += (2*i - 1) / i
print("Valor de S:", soma)

32#

import random

n = int(input("Digite o número de lançamentos: "))
for _ in range(n):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 > d2:
        rel = ">"
    elif d1 < d2:
        rel = "<"
    else:
        rel = "="
    print(d1, rel, d2)

33#
n = int(input())
i = int(input())
j = int(input())
resultados = []
k = 0
while len(resultados) < n:
    if k % i == 0 or k % j == 0:
        resultados.append(k)
    k += 1
print(*resultados, sep=',')

34#

n = 1
while True:
    divisivel = True
    for i in range(1, 21):
        if n % i != 0:
            divisivel = False
            break
    if divisivel:
        print(n)
        break
    n += 1

35#

valor_inicial, valor_final = map(int, input("Digite o valor inicial e valor final: ").split())
if valor_inicial > valor_final:
    print("Intervalo de valores invalido")
else:
    soma = 0
    for num in range(valor_inicial, valor_final + 1):
        if num % 2 != 0:
            soma = soma + num
    print("Soma dos impares neste intervalo:", soma)


36#

n = 100

soma_dos_quadrados = (n * (n + 1) * (2 * n + 1)) // 6
quadrado_da_soma = ((n * (n + 1)) // 2) ** 2

diferenca = quadrado_da_soma - soma_dos_quadrados

print("Diferença:", diferenca)

37#


for numero in range(1000, 10000):
    parte_alta = numero // 100      # primeiros dois dígitos
    parte_baixa = numero % 100      # últimos dois dígitos
    soma = parte_alta + parte_baixa
    if soma * soma == numero:
        print(numero)

38#

for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            print(f"Terno pitagórico: a={a}, b={b}, c={c}")
            print(f"Produto: {a * b * c}")
            break

            
39# 

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

if base > 0 and altura > 0:
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")
else:
    print("Erro: base e altura devem ser maiores que zero.")


40#

maior = None
menor = None

while True:
    numero = int(input("Digite um numero inteiro (negativo para encerrar): "))
    if numero < 0:
        break
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

if maior is not None:
    print(f"Maior numero lido: {maior}")
    print(f"Menor numero lido: {menor}")
else:
    print("Nenhum numero válido foi digitado.")


41#
r1 = float(input("Digite o valor de R1:"))
r2 = float(input("Digite o valor de R2:"))

while r1 != 0 and r2 != 0:
    R = (r1 * r2) / (r1 + r2)
    print("Resistência equivalente:", R)

    r1 = float(input("Digite o valor de R1: "))
    r2 = float(input("Digite o valor de R2: "))

print("Valor igual a zero")


42#
n = float(input("Digite um numero:"))

while n > 0:
    q = n * n
    c = n * n * n
    r = n ** 0.5

    print("Quadrado:", q)
    print("Cubo:", c)
    print("Raiz quadrada:", r)

    print()
    n = float(input("Digite outro numero:"))

print("Programa encerrado.")

43#
soma = 0
qtdd = 0

i = int(input("Digite uma idade:"))

while i != 0:
    soma = soma + i
    qtdd = qtdd + 1
    i = int(input("Digite outra idade:"))

if qtdd > 0:
    media = soma / qtdd
    print("Média das idades:", media)


44#
n = int(input("Digite um numero positivo:"))

a = 0
b = 1

print(a)
print(b)

c = a + b

while c <= n:
    print(c)
    a = b
    b = c
    c = a + b

45#
op = 0

while op != 3:
    print("1 = km/h para m/s")
    print("2 = m/s para km/h")
    print("3 = sair")

    op = int(input("Escolha uma opção:"))

    if op == 1:
        km = float(input("Digite a velocidade em km/h:"))
        ms = km / 3.6
        print("Velocidade em m/s:", ms)
    if op == 2:
        ms = float(input("Digite a velocidade em m/s:"))
        km = ms * 3.6
        print("Velocidade em km/h:", km)
    if op == 3:
        print("Encerrando")

46#
import random

n = random.randint(1, 1000)
c = 0
t = 0

while c != n:
    c = int(input("Tente adivinhar o numero:"))
    t = t + 1

    if c < n:
        print("muito baixo")
    if c > n:
        print("muito alto")

print("Voce acertou!!! Tentativas:", t)


48#

49#
sc = float(input("Salario do Carlos:"))
sj = sc / 3

tc = float(input("taxa mensal da poupança:"))
tfc = tc / 100
tj = float(input("taxa mensal do fundo de renda fixa:"))
tfj= tj / 100

vc = sc
vj = sj
meses = 0

while vj < vc:
    vc = vc + vc * tfc
    vj = vj + vj * tfj
    meses = meses + 1

print("Meses necessarios:", meses)
print("Valor de Carlos:", round(vc, 2))
print("Valor de João:", round(vj, 2))

50#
ac = 1.50
az = 1.10

cc = 0.02
cz = 0.03

anos = 0

while az <= ac:
    ac = ac + cc
    az = az + cz
    anos = anos + 1

print("Anos necessarios:", anos)


51#
s = 2000
au = 0.015
a = 1996
a_atual = int(input("Digite o ano atual:"))

while a <= a_atual:
    s = s + s * au
    au = au * 2
    a = a + 1

print("Salario atual é:", s)


52#

53#
n = int(input("Digite um numero inteiro positivo:"))

n1 = 1
for i in range(1, n + 1):
    l = ""
    for j in range(i):
        l += str(n1) + " "
        n1 += 1
    print(l)

54#
n = int(input("Digite um numero inteiro maior que 1"))

c = 0
for i in range(1, n + 1):
    if n % i == 0:
        c += 1

if c == 2:
    print("O numero é primo")
else:
    print("O numero não é primo")


55#
n = int(input("Digite um numero não negativo:"))

s = 0
c = 0
n = 2

while c < n:
    div = 2
    primo = True
    while div < n:
        if n % div == 0:
            primo = False
            break
        div = div + 1
    if primo:
        s = s + n
        c = c + 1
    n = n + 1

print("Soma do numero primo escolhido n vezes é:", s)


56#
lim = 2000000
s = 0
n = 2

while n < lim:
    div = 2
    primo = True
    while div < n:
        if n % div == 0:
            primo = False
            break
        div = div + 1
    if primo:
        s = s + n
    n = n + 1

print("Soma dos primos é:", s)


57#
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))

cont = 0
n = a

while n <= b:
    if n < 2:
        primo = False
    else:
        primo = True
        div = 2
        while div < n:
            if n % div == 0:
                primo = False
                break
            div += 1
    if primo:
        cont += 1
    n += 1

print("A quantidade dds numeros primos é:", cont)


58#
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))

s = 0
n = a

while n <= b:
    if n < 2:
        primo = False
    else:
        primo = True
        div = 2
        while div < n:
            if n % div == 0:
                primo = False
                break
            div += 1
    if primo:
        s += n
    n += 1

print("Soma dos numeros primos é:", s)


59#


60#
s = 0
q = 0
ma = 900000000000
me = 900000000000
s_p = 0
q_p = 0

n = int(input("Digite um numero:"))

while n != -1:
    s += n
    q += 1

    if ma is None or n > ma:
        ma = n
    if me is None or n < me:
        me = n

    if n % 2 == 0:
        s_p += n
        q_p += 1

    n = int(input("Digite um numero:"))

if q > 0:
    m = s / q
else:
    m = 0

if q_p > 0:
    m_p = s_p / q_p
else:
    m_p = 0

print("Soma:", s)
print("Quantidade:", q)
print("Media:", m)
print("Maior numero:", ma)
print("Menor numero:", me)
print("Media dos pares:", m_p)


61#
def eh_palindromo(n):
    return str(n) == str(n)[::-1]

m = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        p = i * j
        if eh_palindromo(p) and p > m:
            m = p

print("O maior palíndromo é:", m)

62#
def numero_por_extenso(n):
    uni = ["", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    esp = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dez = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    cent = ["", "cento", "duzentos", "trezentos", "quatrocentos", 
                "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    if n == 100:
        return "cem"
    if n == 1000:
        return "mil"

    plvr = ""
    c = n // 100
    d = (n % 100) // 10
    u = n % 10

    if c > 0:
        plvr += cent[c]
        if d != 0 or u != 0:
            plvr += "e"

    if d == 1:
        plvr += esp[u]
    else:
        if d > 1:
            plvr += dez[d]
            if u != 0:
                plvr += "e"
        if d != 1:
            plvr += uni[u]

    return plvr

t_l = 0

for i in range(1, 1001):
    plvr = numero_por_extenso(i)
    p_s_e = plvr.replace(" ", "").replace("-", "")
    t_l += len(p_s_e)

print("Total de letras de 1 a 1000:", t_l)
