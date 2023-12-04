while True:
    try:
        dinheiro = input('você quer converter o seu dinheiro em "dolar" ou  em "euro"?')
        valor = float(input('ok, agora digite o valor em reais que deseja converter: '))   
        calcule = 0
        calcule1 = 0
        if dinheiro == 'dolar':
            calcule = valor / 4.91
            print(f'pronto, {valor} reias é o equivalante a {calcule:.2f} dolares')
        elif dinheiro == 'euro':
            calcule1 = valor / 5.37
            print(f'pronto, {valor} reais é o equivalante a {calcule1:.2f} euros')         

        final = input(f'se deseja continuar digite "sim" caso contrario, digite "nao"')
        if final == 'sim':
            continue        
        elif final == 'nao':
            break        
    finally:
        print('muito obrigado por usar nosso progama')
