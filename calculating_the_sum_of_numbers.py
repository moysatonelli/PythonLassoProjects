#João recebeu uma lista de valores representando as receitas de sua loja de roupas.
#Ele quer calcular a soma total dessas receitas para entender o desempenho financeiro semanal.
#Crie um programa que ajude João a calcular o valor total.

valores = [10, 20, 30, 40, 50]
soma = 0

for calculo in valores:
    soma = soma + calculo # soma += calculo também dará certo
    print(f"A soma total das receitas é: {soma}")