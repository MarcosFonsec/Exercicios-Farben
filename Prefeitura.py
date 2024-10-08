import requests

# Função para obter a cotação do dólar
def obter_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        cotacao_dolar = dados['USDBRL']['bid']
        return float(cotacao_dolar)
    else:
        return None

# Função para calcular os valores e imprimir as informações
def calcular_reforma_pracas():
    # Valores em dólares
    verba_usd = 150000  # Verba total da prefeitura em USD
    custo_por_praca_usd = 1350  # Custo de reforma por praça em USD
    
    # Obter a cotação atual do dólar
    cotacao = obter_cotacao_dolar()
    
    if cotacao:
        # Exibir a cotação do dólar
        print(f"Cotação atual do dólar: R${cotacao:.2f}")
        
        # Converter os valores para reais
        verba_brl = verba_usd * cotacao
        custo_por_praca_brl = custo_por_praca_usd * cotacao
        
        # Calcular o número de praças que podem ser reformadas
        num_pracas = verba_usd // custo_por_praca_usd
        
        # Exibir os resultados
        print(f"Verba total em reais: R${verba_brl:.2f}")
        print(f"Custo de reforma de cada praça em reais: R${custo_por_praca_brl:.2f}")
        print(f"Número total de praças que podem ser reformadas: {int(num_pracas)}")
    else:
        print("Não foi possível obter a cotação do dólar.")

# Chamar a função para calcular
calcular_reforma_pracas()