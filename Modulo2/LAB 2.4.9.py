# Cenário
# Milhas e quilômetros são unidades de comprimento ou distância.

# Lembrando que 1 milha é igual a aproximadamente 1.61 quilômetros, complete o programa no editor para que converta:

# milhas em quilômetros;
# quilômetros em milhas.
# Não altere nada no código atual. Escreva seu código nos locais indicados por ###. Teste seu programa com os dados que fornecemos no código-fonte.

# Preste atenção especial ao que está acontecendo na função de print(). Analise como fornecemos multiplos argumentos para a função e como produzimos os dados esperados.

# Observe que alguns dos argumentos dentro da função print() são strings (por exemplo, "milhas é", enquanto outros são variáveis (por exemplo, miles).

#   Dica  
# Há mais uma coisa interessante acontecendo lá. Você pode ver outra função dentro da função print()? É a função round(). Seu trabalho é arredondar o resultado de saída para o número de casas decimais especificadas entre parênteses e retornar um float (dentro da função round() você pode encontrar o nome da variável, uma vírgula e o número de casas decimais que pretendemos por). Falaremos sobre funções muito em breve, então não se preocupe que tudo pode não estar totalmente claro ainda. Só queremos despertar a sua curiosidade.

# Depois de concluir o laboratório, abra o Sandbox e experimente um pouco mais. Tente escrever conversores diferentes, por exemplo, um conversor de USD para EUR, um conversor de temperatura, etc. - deixe sua imaginação voar! Tente gerar os resultados combinando strings e variáveis. Tente usar e experimentar a função round() para arredondar seus resultados para uma, duas ou três casas decimais. Confira o que acontece se você não fornecer qualquer número de dígitos. Lembre-se de testar seus programas.

# Experimente, tire conclusões e aprenda. Seja curioso.

# Saída esperada
# 7.38 milhas é 11.88 quilômetros
# 12.25 quilômetros é 7.61 milhas

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")
