def classificar_triangulo():
    # Leitura dos ângulos
    angulo_a = int(input("Digite o valor do ângulo A: "))
    angulo_b = int(input("Digite o valor do ângulo B: "))
    angulo_c = int(input("Digite o valor do ângulo C: "))
    
    # Verificar se a soma dos ângulos é 180 graus
    if angulo_a + angulo_b + angulo_c != 180:
        print("Os ângulos fornecidos não formam um triângulo válido.")
        return
    
    # Classificar o triângulo
    if angulo_a == 90 or angulo_b == 90 or angulo_c == 90:
        print("O triângulo é retângulo.")
    elif angulo_a > 90 or angulo_b > 90 or angulo_c > 90:
        print("O triângulo é obtusângulo.")
    else:
        print("O triângulo é acutângulo.")

# Chamar a função classificar_triângulo
classificar_triangulo()