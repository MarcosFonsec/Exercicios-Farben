# Função para ler a base e altura do retângulo
def retangulo():
    base = float(input("Informe a base do retângulo: "))
    altura = float(input("Informe a altura do retângulo: "))
    return base, altura

# Função para calcular e imprimir a área do retângulo
def area_do_retangulo(base, altura):
    area = base * altura
    print(f"A área do retângulo é: {area:.2f}")

# Função principal que mantém o loop de cálculo
def calcular_areas():
    while True:
        # Ler a base e a altura
        base, altura = retangulo()
        
        # Calcular e imprimir a área
        area_do_retangulo(base, altura)
        
        # Perguntar ao usuário se deseja continuar
        resposta = input("Deseja calcular a área de outro retângulo? (SIM ou NAO): ").strip().upper()
        
        if resposta != 'SIM':
            print("Encerrando o programa...")
            break

# Chamar a função principal
calcular_areas()