import json

# Dicionário para mapear o número do clube com o nome do clube
CLUBES = {
    1: "Criciúma",
    2: "Avaí",
    3: "Figueirense",
    4: "Outros"
}

# Função para carregar dados do arquivo JSON ou criar um novo se não existir
def carregar_dados():
    try:
        with open('torcedores_por_clube.json', 'r') as arquivo_json:
            return json.load(arquivo_json)
    except FileNotFoundError:
        return {str(1): [], str(2): [], str(3): [], str(4): []}  # Chaves como strings

# Função para coletar dados dos torcedores e salvar em JSON
def coleta_dados():
    torcedores_por_clube = carregar_dados()  # Carregar os dados existentes ou iniciar do zero

    while True:
        clube = int(input("Digite o clube de preferência (1-Criciúma, 2-Avaí, 3-Figueirense, 4-Outros, 5-Fim da pesquisa): "))
        
        if clube == 5:
            break  # Encerra o loop quando o usuário escolhe "5"
        
        nome = input("Digite seu nome completo: ")  # Coletar o nome completo
        salario = float(input("Digite o seu salário: "))  # Coletar o salário

        torcedor = {
            "nome": nome,
            "salario": salario
        }

        # Adicionar o torcedor à lista do clube, convertendo 'clube' para string
        torcedores_por_clube[str(clube)].append(torcedor)

    # Salvar os dados atualizados no arquivo JSON
    with open('torcedores_por_clube.json', 'w') as arquivo_json:
        json.dump(torcedores_por_clube, arquivo_json, indent=4)

    print("Dados salvos com sucesso no arquivo 'torcedores_por_clube.json'.")

# Função para contar torcedores e calcular a média salarial dos torcedores do Criciúma
def contagem_e_media_salarial():
    with open('torcedores_por_clube.json', 'r') as arquivo_json:
        torcedores_por_clube = json.load(arquivo_json)

    # Contar o número de torcedores por clube
    for clube, torcedores in torcedores_por_clube.items():
        print(f"{CLUBES[int(clube)]} tem {len(torcedores)} torcedores.")

    # Calcular a média salarial dos torcedores do Criciúma (clube 1)
    torcedores_criciuma = torcedores_por_clube["1"]
    if torcedores_criciuma:  # Verificar se há torcedores do Criciúma
        soma_salarios = sum(torcedor['salario'] for torcedor in torcedores_criciuma)
        media_salarial = soma_salarios / len(torcedores_criciuma)
        print(f"A média salarial dos torcedores do Criciúma é: {media_salarial:.2f}")
    else:
        print("Não há torcedores do Criciúma para calcular a média salarial.")

# Função para encontrar o torcedor com o maior salário
def maior_salario():
    with open('torcedores_por_clube.json', 'r') as arquivo_json:
        torcedores_por_clube = json.load(arquivo_json)

    maior_salario = 0
    torcedor_rico = None
    clube_rico = None

    # Percorrer todos os clubes e seus torcedores
    for clube, torcedores in torcedores_por_clube.items():
        for torcedor in torcedores:
            if torcedor['salario'] > maior_salario:
                maior_salario = torcedor['salario']
                torcedor_rico = torcedor['nome']
                clube_rico = clube

    if torcedor_rico:
        print(f"O torcedor com o maior salário é {torcedor_rico} do clube {CLUBES[int(clube_rico)]}, com um salário de {maior_salario:.2f}")
    else:
        print("Não foi encontrado nenhum torcedor.")

# Função principal para controlar o fluxo do programa
def main():
    coleta_dados()

    # Após o fim da pesquisa, perguntar se o usuário quer ver os resultados
    ver_resultados = input("Deseja ver os resultados da pesquisa? (SIM/NAO): ").strip().upper()

    if ver_resultados == 'SIM':
        contagem_e_media_salarial()
        maior_salario()

# Iniciar o programa
if __name__ == "__main__":
    main()
