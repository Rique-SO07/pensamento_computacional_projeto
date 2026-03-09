'''
CRUD

Hamburgueria

Este sistema irá gerenciar os pedidos de forma ágil e oferecer uma experiência única
para o atendimento da Hamburgueria.
Henrique 
'''

print("\n=== Sistema da hamburgueria ===")
print("1. Cadastro") #Opção de entrar com o Google
print("1.1 Login") #
print("2. Esqueceu a senha") #Criar nova senha (6 digitos)
print("3. Menu") #Opção de lanches e combos de lanches
print("4. Carrinho")
print("5. Opções") #Vai retirar alguma coisa?
print("6. Finalizar pedido") 
print("7. Cupom\promoção") #Aplicação de 5% de desconto - (Como fazer isso depois?)
print("8. Chat da loja") #Suporte da loja 
print("9. Feedback") #Avaliar a loja de 0-5 e caixa de comentários
print("0. Sair")

carrinho = []
total_conta = 0

while True: #While criará o loop que rodará infinitamente até haver um break
    escolha = input("\nEscolha uma opção:")

    if escolha == '1':
        print('Realizar o cadastro')
        #Código para cadastrar o cliente
    
    elif escolha == '2':
        print('Esqueceu a senha?')

    elif escolha == '3':
        # Sub-menu com opções do cardápio
        while True:
            print("\n=== Menu ===")
            print("1. Lanches")
            print("2. Combos")
            print("3. Bebidas")
            print("4. Voltar ao menu principal")
            
            sub_escolha = input("Escolha uma opção do menu: ")
            
            if sub_escolha == '1':
                print("Lanches disponíveis:")
                print("- X-Burguer - R$ 15,00")
                print("- X-Salada - R$ 18,00")
                print("- X-Bacon - R$ 20,00")

            
            elif sub_escolha == '2':
                print("Combos disponíveis:")
                print("- Combo Família - R$ 45,00")
                print("- Combo Duplo - R$ 30,00")
                print("- Combo Kid - R$ 20,00")
            
            elif sub_escolha == '3':
                print("Bebidas disponíveis:")
                print("- Refrigerante - R$ 5,00")
                print("- Suco - R$ 7,00")
                print("- Água - R$ 3,00")
            
            elif sub_escolha == '4':
                print("Voltando ao menu principal...")
                break
            
            else:
                print("Opção inválida. Tente novamente.")
                #Aqui consegui aprofundar minhas opções, colocando um outro While True


    elif escolha == '4':
       print('Aqui fica registrados os pedidos')


    elif escolha == '5':
       print('Precisa retirar algo?')

    elif escolha == '6':
       print('Finalizar pedido')

    elif escolha == '7':
       print('Veja nossos cupons!')
       input("Deseja aplicar nosso cupom de 5% ?")
       print("Aplicando cupom de 5%...")
       total_conta = total_conta *0.95
       print(f"Novo total: R$ {total_conta:.2f}")

    elif escolha == '8':
       print('\n=== Entre em contato ===')
       mensagem = input ("Como podemos ajudar? Digite sua dúvida: ")


       message_suporte.append(mensagem)

       print("\n[Sistema]: Mensagem enviada com sucesso!")
       print("[Sistema]: Um atendente entrará em contato em breve. Protocolo: #12345")




    elif escolha == '9':
       print('Diga-nos o que achou?')

       carrinho =[]
       total_conta = 0 
       message_suporte = []
       avaliacoes = []
       
       while True:
        nota = input ("De 0 a 5, Qual nota você nos avalia?")
        if nota in ['0','1', '2','3','4','5']:
           break
        print("Por favor, digite uma nota válida (0 a 5).")

        comentario = input("Deixe seu comentário (opcional): ")

       feedback_cliente = {
          "nota": nota,
          "comentario": comentario
       }
       avaliacoes.append(feedback_cliente)

       print("\nObrigado pelo seu feedback! Isso nos ajuda muito!")



    elif escolha == '0':
     print('Saindo do sistema. Até logo!')
     break #O break faz com que o loop continue até clicar no zero que é a "pausa".

else:
   print('Opção inválida. Por favor, tente novamente.')



   
      