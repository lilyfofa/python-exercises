preco = float(input('Digite o preço das compras: '))
pagamento = int(input('Digite a forma de pagamento:\n(1) - à vista no dinheiro/cheque\n(2) - à vista no cartão\n(3) - 2x no cartão\n(4) 3x ou mais no cartão\nSua resposta: '))
dinheiro = preco * 0.9
vistacard = preco * 0.95
parcelado = preco* 1.2
if pagamento == 1:
    print(f'Como você pagará à vista no dinheiro/cheque, você recebeu um desconto de 10% e deverá pagar R${dinheiro:.2f} (era R${preco:.2f}).')
elif pagamento == 2:
    print(f'Como você pagará à vista no cartão, você recebeu um desconto de 5% e deverá pagar R${vistacard:.2f} (era R${preco:.2f}).')
elif pagamento == 3:
    print(f'Como você parcelará em 2x no cartão, pagará R${preco / 2:.2f} em cada mẽs, totalizando R%{preco:.2f}')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Como vocễ parcelará em {parcelas}x no cartão, você pagará R${parcelado / parcelas:.2f} em cada mẽs, totalizando R${parcelado:.2f}.')
