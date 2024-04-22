import os
#Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo_mensal):
    os.system('cls')
#Estrutura Condicional para verifica o consumo médio mensal 
    if consumo_mensal <= 10:
        print("Plano Essencial Fibra - 50Mbps")
    
    elif consumo_mensal <= 20: 
        print("Plano Prata Fibra - 100Mbps")
    
    else:
        print("Plano Premium Fibra - 300Mbps")
#Retorno do plano de internet adequado:
    return consumo_mensal

#Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Informe seu consumo mensal de dados em GB: "))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano(consumo)
print(f"Consumo Mnesal de Dados: {consumo} GB")

#escolher o plano de internet com base no consumo mensal de dados
print("========= Escolher plano =========")
plano = """
1 = Plano Essencial Fibra - 50Mbps
2 = Plano Prata Fibra - 100Mbps
3 = Plano Premium Fibra - 300Mbps
4 = Sair

==================================
==> """
while True:
    opcao = input(plano)

    if opcao == '1':
        print("\nVocê escolheu o Plano Essencial Fibra - 50Mbps. Parabéns!")
        break
    
    elif opcao == '2':
        print("\nVocê escolheu o Plano Prata Fibra - 100Mbps. Parabéns!")
        break
    
    elif opcao == '3':
        print("Você escolheu o Plano Premium Fibra - 300Mbps. Parabéns!")
        break
    
    elif opcao == '4':
        break  
print("Agradecemos por visitar nosso site e por sua aquisição. Volte sempre!")
