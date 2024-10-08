# Função que converte Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

# Função que gera a tabela de conversão de Celsius para Fahrenheit
def gerar_tabela_celsius_fahrenheit():
    print(f"{'Celsius':>8} {'Fahrenheit':>12}")  # Cabeçalho da tabela
    print("-" * 22)  # Faz uma linha divisória na tabela
    
    # Loop de 0 a 40, com passo de 2
    for celsius in range(0, 41, 2):
        fahrenheit = celsius_para_fahrenheit(celsius)  # Chama a função de conversão
        print(f"{celsius:>8} {fahrenheit:>12.1f}")  # Exibe o valor formatado

# Chamar a função para gerar a tabela
gerar_tabela_celsius_fahrenheit()