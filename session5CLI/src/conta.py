import json
from logic import salvar_no_arquivo
from date import obter_data_hora_atual

def adicionar_fundos():
    """Registra entrada de dinheiro na conta."""
    print("\n--- ADICIONAR DINHEIRO ---")
    descricao = input("Descrição (ex: Salário, Depósito): ")
    valor = float(input("Valor: R$ "))
    
    dados = {
        "tipo": "entrada", # Identifica que o dinheiro entrou
        "descricao": descricao,
        "valor": valor,
        "valor_em_conta": valoremconta, # Variável que armazena o valor do depósito para somar ao saldo
        "data_hora": obter_data_hora_atual() # Puxa a hora exata do date.py
    }
    
    texto_json = json.dumps(dados, ensure_ascii=False)
    salvar_no_arquivo(texto_json)
    print(f"Entrada de R${valor:.2f} registrada com sucesso!")

def adicionar_gasto():
    """Registra uma despesa/gasto."""
    print("\n--- REGISTRAR GASTO ---")
    descricao = input("Descrição do gasto (ex: Mercado, Conta de Luz): ")
    valor = float(input("Valor do gasto: R$ "))
    
    
    
    
    
    dados = {
        "tipo": "saida", # Identifica que o dinheiro saiu
        "descricao": descricao,
        "valor": valor,
        "valor_em_conta": valoremconta, # Variável que armazena o valor do gasto para subtrair do saldo
        "data_hora": obter_data_hora_atual() # Puxa a hora exata do date.py
    }
    
    texto_json: str = json.dumps(dados, ensure_ascii=False)
    salvar_no_arquivo(texto_json)
    print(f"Gasto de R${valor:.2f} registrado com sucesso!")

