import typer 
from conta import adicionar_fundos, adicionar_gasto
import conta
from date import obter_valor_em_conta

app = typer.Typer()


saldo = 0.0

def adicionar_fundos(valor, descricao):
    conta.json.dumps(valor, ensure_ascii=False)
    global saldo
    descricao = str(descricao)
    valor_numero = float(valor)
    saldo = saldo + valor_numero 
    print(f"✅ Depósito de R$ {valor_numero:.2f} adicionado!")


def adicionar_gasto(valor, descricao):
    conta.json.dumps(valor, ensure_ascii=False)
    
    global saldo
    
    descricao = str(descricao)
    
    valor_numero = float(valor)
    saldo = saldo - valor_numero 
    print(f"✅ Gasto de R$ {valor_numero:.2f} registrado!")

def obter_valor_em_conta():
    return saldo


def cli():
    print("Bem-vindo ao Gerenciador de Despesas CLI!")
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar dinheiro na conta")
        print("2. Registrar um gasto")
        print("3. Ver saldo atual (em breve)")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        

        if opcao == "1":
            adicionar_fundos(input("Digite o valor a ser adicionado: "), input("Digite a descrição do depósito: "))
        elif opcao == "2":
            adicionar_gasto(input("Digite o valor do gasto: "), input("Digite a descrição do gasto: "))
        elif opcao == "3":
            print(f"Saldo atual: R$ {obter_valor_em_conta():.2f}")
        elif opcao == "4":  
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    cli()
    pass