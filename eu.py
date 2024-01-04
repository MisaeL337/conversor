print('-'*50)
print('BEM VINDO A NOSSA CALCULADORA DE CONVERÇÃO DE MOEDA')
print('-'*50)


print('PARA COMEÇAR, RESPONDA AS SEGUINTES PERGUNTAS: ')
while True:
    try:
        nome = input("Por favor, digite o seu nome para sabermos melhor sobre você: ").upper()
        dinheiro = input(f'Ola {nome}, como deseja converter o seu dinherio? em "dolar" ou  em "euro"?: ').lower()
        valor = float(input(f'ok {nome}, agora digite o valor em reais que deseja converter: ')) 
        calcule = 0
        calcule1 = 0
        if dinheiro == 'dolar':
            calcule = valor / 4.91
            print(f'pronto {nome}, {valor:.0f} reias é o equivalante a {calcule:.2f} dolares')
        elif dinheiro == 'euro':
            calcule1 = valor / 5.37
            print(f'pronto {nome}, {valor:.0f} reais é o equivalante a {calcule1:.2f} euros')   
        else:
            print(f'por favor {nome}, digite somente o nome da moeda que deseja converter, "dolar" ou "euro" ')        


        final = input(f'se deseja continuar {nome}, digite "sim" caso contrario, digite "nao" ').lower()
        if final == 'sim':
            continue        
        elif final == 'nao':
            break    
    except ValueError:
        print(f'por favor {nome}, digite somente números inteiros')
    finally:
        print(f'muito obrigado por usar nosso progama {nome}, até a proxima')


