# LAB   Variáveis ‒ um simples conversor
# Cenário: Milhas e quilômetros são unidades de comprimento ou distância.
#
# Lembrando que 1 milha é igual a aproximadamente 1.61 quilômetros.
# Complete o programa no editor para que converta:
#
# - milhas em quilômetros;
# - quilômetros em milhas.
# 
# Não altere nada no código atual. 
# Escreva seu código nos locais indicados por ###. 
# Teste seu programa com os dados que fornecemos no código-fonte.
#
# Preste atenção especial ao que está acontecendo na função de print(). 
# Analise como fornecemos multiplos argumentos para a função e como produzimos os dados esperados.
#
# Observe que alguns dos argumentos dentro da função print() são strings (por exemplo, "milhas é", enquanto outros são variáveis (por exemplo, miles).
#
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")