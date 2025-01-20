#Aula 1 PWBE
#Revisão

#Soma
# num1 = int(input("Digite um numero: "))
# num2 = int(input("Digite um numero: "))
# result = num1 + num2

# print(result)

#Calculo de idade
# nome = input("Digite seu nome: ")
# ano = int(input("Digite o ano que você nasceu: "))
# idade = 2025 - ano

# print(f"Olá {nome}, em 2025 você terá {idade} anos")

# #Impar ou par
# num = int(input("Digite um numero: "))
# if num % 2 == 0:
#     print("Esse numero é par!")
# else:
#     print("Esse numero é impar!")

#Media das notas
# media = 0
# for aluno in range(0,5):
#     nota = float(input("Digite sua nota: "))
#     media = media + nota

# if media/5 >= 5:
#     print("Aprovado")
# elif media/5 < 5 and media/5 > 2.5:
#     print("Recuperação")
# else:
#     print("Reprovado")

#Numero até zero
# num = int(input("Digite um numero: "))
# for numero in range(num, -1, -1):
#     print(numero)

#Solicitar numeros até negativo e identifica qual o maior
# num = int(input("Digite um numero: "))
# lista = []
# while num > -1:
#     num = int(input("Digite um outro numero: "))
#     lista.append(num)

# print(f"O maior numero digitado é {max(lista)}")

#Função para inverter string
# def inverter_string(palavra):
#     palavra_invertida = ""
#     for letra in palavra:
#         palavra_invertida = letra + palavra_invertida
#     print(palavra_invertida)

# palavra = input("Digite uma palavra pra inverte-la: ")
# inverter_string(palavra)

#Contador de caractere
def contar_carateres(palavra):
    conta = {}
    for letra in palavra:
        if letra in conta:
            conta[letra] += 1
        else:
            conta[letra] = 1
    print(conta)

palavra = input("Digite uma palavra para contar o numero de caracter: ")    
contar_carateres(palavra)