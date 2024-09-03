import json

def calculate_faturamento(file_path):
    with open(file_path, 'r') as file:
        faturamento_mensal = json.load(file)

    menor_faturamento = float('inf')
    maior_faturamento = float('-inf')
    soma_faturamento = 0
    dias_superior_media = 0
    num_dias_com_faturamento = 0

    for entry in faturamento_mensal:
        valor = entry['valor']
        
        if valor == 0:
            continue

        if valor < menor_faturamento:
            menor_faturamento = valor

        if valor > maior_faturamento:
            maior_faturamento = valor

        soma_faturamento += valor
        num_dias_com_faturamento += 1

    if num_dias_com_faturamento > 0:
        media_mensal = soma_faturamento / num_dias_com_faturamento
    else:
        media_mensal = 0

    for entry in faturamento_mensal:
        valor = entry['valor']
        if valor > media_mensal:
            dias_superior_media += 1

    return menor_faturamento, maior_faturamento, dias_superior_media, media_mensal

def main():
    try:
        json_data = 'dados.json'

        menor_faturamento, maior_faturamento, dias_superior_media, media_mensal = calculate_faturamento(json_data)

        print("Menor valor de faturamento:", menor_faturamento)
        print("Maior valor de faturamento:", maior_faturamento)
        print("Média mensal de faturamento:", media_mensal)
        print("Número de dias com faturamento superior à média:", dias_superior_media)

    except FileNotFoundError:
        print(f"Erro: Arquivo '{json_data}' não encontrado. Verifique o caminho e tente novamente.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{json_data}' não é um JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
