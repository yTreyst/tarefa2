def calcular_imc(peso, altura):
    """
    Função que calcula o Índice de Massa Corpórea (IMC)
    
    peso: peso em quilogramas (kg)
    altura: altura em metros (m)
    """
    imc = peso / altura ** 2
    return imc

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = calcular_imc(peso, altura)
print("Seu IMC é: {:.2f}".format(imc))