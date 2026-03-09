'''
Definição de um dicionário (base de dados usando tabela)

'''


preco_chocolate = {
'Chocolate ao leite': 20.90,
'Chocolate meio amargo': 18.00,
'Chocolate amargo': 23.50

}
#Defini qual chocolate quero procurar 
chocolate_choosed = 'Chocolate ao leite'

#fazemos a busca direto usando o método .get()
#O .get() tenta encontrar o chocolate; se não achar, mostra 'Chocolate não encontrado'
resultado = preco_chocolate.get(chocolate_choosed, 'Chocolate não encontrado')

#Exibimos os resultado 
print(f"O preço da {chocolate_choosed} é R$ {resultado}")