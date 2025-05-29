#lista de atividades 1

1#

n = int(input("Digite um numero inteiro:"))
print("O numero é:", n)


2#
n = float(input("Digite um numero real:"))
print("O numero é:", n)


3#
n1 = int(input("digite o primeiro valor:"))
n2 = int(input("digite o segundo valor:"))
n3 = int(input("digite o terceiro valor:"))
print(n1 + n2 + n3)


4#
n = float(input("Digite o numero:"))
q = n * n
print("o quadrado desse numero é:", q)


5# 
a = float(input("digite o numero:"))
print(a / 5)


6#
c = float(input("digite a temperatura em Celsius:"))
f = c * (9/5) + 32
print("a temperatura em Fahrenheit é:", f)


7#
f = float(input("digite a temperatura em Fahrenheit:"))
c = 5 * (f - 32) / 9
print("a temperatura em Celsius é:", c)


8#
k = float(input("digite a temperatura em Kelvin:"))
c = k - 273.15
print("a temperatura em celsius é:", c)


9#
c = float(input("digite a temperatura em Celsius:"))
k = c + 273.15
print("a temperatura em Kelvin é:", k)


10#
k = float(input("digite a velocidade em Km/h:"))
m = k / 3.6
print("a velocidade em M/s é:", m)


11#
m = float(input("digite a velocidade em M/s:"))
k = m * 3.6
print("a velocidade em Km/h é:", k) 


12#
m = float(input("digite a distância em Milhas:"))
k = 1.61 * m
print("a distância em Quilômetros é:", k)


13#
k = float(input("digite a distância em Quilômetros:"))
m = k / 1.61
print("a distância em Milhas é:", m)


14#
import math

g = float(input("digite qual é o ângulo em graus:"))
r = g * math.pi / 180
print("O ângulo em radianos é:", r)


15#
import math

r = float(input("digite qual é o ângulo em radianos:"))
g = r * 180 / math.pi
print("O ângulo em radianos é:", g)


16#
p = float(input("Digite o valor em Polegadas: "))
c = p * 2.54
print("O tamanho em Centímetros é:", c)


17#
c = float(input("Digite comprimento em centimetros:"))
p = c / 2.54

print("O comprimento em polegadas é:", p)


18#
v = float(input("Digite um volume em metros cubicos:"))
l= 1000 * v

print("O volume convertido em litros é:", l)


19#
v = float(input("Digite um volume em litros:"))
m3 = v/ 1000

print("O volume em metros cubicos é :", m3)

20#
m= float(input("Digite um valor em kg:"))
l = m/ 0.45

print("O valor convertido para libras é:", l)

21#
m_l = float(input("Digite a massa em libras:"))
km = m_l * 0.45

print("A conversão em km é:", km)

22#
c_j = float(input("Digie o comprimento em Jardas:"))
m = 0.91 * c_j

print("o comprimento em M é:", m)

23#
comprimento_metros = float(input("Digite um comprimento em metros"))
jardas = comprimento_metros/0.91

print(jardas)

24#

m2 = float(input("Digite a área em metros quadrados (m²): "))
acres = m2 * 0.000247
print(f"A área em acres é: {acres}")

25#

acres = float(input("Digite a área em acres: "))
m2 = acres * 4048.58
print(f"A área em metros quadrados é: {m2}")

26#

m2 = float(input("Digite a área em metros quadrados (m²): "))
hectares = m2 * 0.0001
print(f"A área em hectares é: {hectares}")

27#

hectares = float(input("Digite a área em hectares: "))
m2 = hectares * 10000
print(f"A área em metros quadrados é: {m2}")

28#

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))
soma = a**2 + b**2 + c**2
print(f"Soma dos quadrados: {soma}")

29#

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
media = (n1 + n2 + n3 + n4) / 4
print(f"Média das notas: {media}")

30#

real = float(input("Valor em reais: "))

cotacao = float(input("Cotação do dólar: "))
print(f"Dólares: {real / cotacao:.2f}")

31#

num = int(input("Número inteiro: "))
print(num - 1, num + 1)

32#

num = int(input("Número inteiro: "))
print((3 * num + 1) + (2 * num - 1))

33#

lado = float(input("Lado do quadrado: "))
print(lado ** 2)

34#

raio = float(input("Raio: "))
print(3.141592 * raio ** 2)

35#
import math

a = float(input("Cateto a: "))

b = float(input("Cateto b: "))
print(math.sqrt(a ** 2 + b ** 2))

36#

raio = float(input("Raio: "))

altura = float(input("Altura: "))
print(3.141592 * raio ** 2 * altura)

37#

valor = float(input("Valor do produto: "))
print(valor * 0.88)

38#

salario = float(input("Salário atual: "))
print(salario * 1.25)

39#

total = 780000
print(total * 0.46, total * 0.32, total * 0.22)

40#

dias = int(input("Dias trabalhados: "))
print(dias * 30 * 0.92)

41#

hora = float(input("Valor hora: "))

mes = float(input("Horas no mês: "))
print(hora * mes * 1.10)

42#

base = float(input("Salário base: "))
print(base * 1.05 - base * 0.07)

43#

valor = float(input("Valor total: "))
desc = valor * 0.9
parcela = valor / 3
print(desc, parcela, desc * 0.05, valor * 0.05)

44#

degrau = float(input("Altura do degrau: "))

alvo = float(input("Altura a alcançar: "))
print(int(alvo / degrau))

45#

letra = input("Letra maiúscula: ")
print(chr(ord(letra) + 32))

46#

num = int(input("informe um número de 100 a 999:"))
inv = str(num)[::-1]
print(int(inv))

47#

num = input("Digite um número de 4 dígitos (1000 a 9999): ")
for digito in num:
    print(digito)

48#

segundos = int(input("Digite um valor em segundos: "))
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60
print(f"{horas}h {minutos}min {segundos}s")

49#

hora = int(input("Hora de início: "))
minuto = int(input("Minuto de início: "))
segundo = int(input("Segundo de início: "))

duracao = int(input("Duração em segundos: "))

total_segundos = hora * 3600 + minuto * 60 + segundo + duracao

hora_fim = (total_segundos // 3600) % 24
minuto_fim = (total_segundos % 3600) // 60
segundo_fim = total_segundos % 60

print(f"Término: {hora_fim:02d}:{minuto_fim:02d}:{segundo_fim:02d}")

50#

idade = int(input("Digite sua idade: "))

ano_atual = int(input("Digite o ano atual: "))
nascimento = ano_atual - idade
print(f"Ano de nascimento: {nascimento}")

51#
import math

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))
distancia = math.sqrt(x * 2 + y * 2)
print(f"Distância da origem: {distancia:.2f}")

52#

a = float(input("Valor investido pelo amigo 1: "))
b = float(input("Valor investido pelo amigo 2: "))
c = float(input("Valor investido pelo amigo 3: "))

premio = float(input("Valor do prêmio: "))

total = a + b + c
print(f"Amigo 1: R${premio * a / total:.2f}")
print(f"Amigo 2: R${premio * b / total:.2f}")
print(f"Amigo 3: R${premio * c / total:.2f}")

53#

c = float(input("Comprimento do terreno (em metros): "))

l = float(input("Largura do terreno (em metros): "))

p = float(input("Preço do metro da tela: "))
perimetro = 2 * (c + l)
custo = perimetro * p
print(f"Custo para cercar o terreno: R${custo:.2f}")

