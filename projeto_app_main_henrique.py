'''
CRUD

Hamburgueria

Este sistema irá gerenciar os pedidos de forma ágil e oferecer uma experiência única
para o atendimento da Hamburgueria.
Henrique 
'''

print("\n=== Sistema da hamburgueria ===")
print("1. Cadastro") #Opção de entrar com o Google
print("1.1 Login") #Após o cadastro, o cliente só terá o login (email e telefone)
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
#Variaveis do carrinho (para adicionar)


while True: #While criará o loop que rodará infinitamente até haver um break
    escolha = input("\n === Escolha uma opção: === \n")

    
    if escolha == '1':
        print('Realizar o cadastro')
        #Código para cadastrar o cliente

    elif escolha == '1.1':
       print('Efetuar o Login')
       #Cód. para realizar o login    
    
    elif escolha == '2':
        print('Esqueceu a senha?')

    elif escolha == '3':
        # Sub-menu com opções do cardápio
        while True:
            print("\n=== Menu ===")
            print("1. Lanches")
            print("2. Combos")
            print("3. Bebidas")
            print("4. Sobremesas")
            print("5. Voltar ao menu principal")

            
            sub_escolha = input("\nEscolha uma opção do menu: ")
            

            if sub_escolha == '1':
                print("\nLanches disponíveis:")
                print("[1] X-Burguer - R$ 15,00")
                print("[2] X-Salada - R$ 18,00")
                print("[3] X-Bacon - R$ 20,00")

                escolha_lanche = input ('\nAdicionar ao Carrinho (Digite o número ou 0 para voltar): ') 
            
                if escolha_lanche == '1':
                   carrinho.append("X-Burguer")
                   total_conta += 15.00
                   print('\nX-Burguer adicionado ao carrinho!')

                elif escolha_lanche =='2':
                   carrinho.append("X-Salada")
                   total_conta += 18.00
                   print('\nX-Salada adicionado ao carrinho!')

                elif escolha_lanche =='3':
                   carrinho.append("X-Bacon")
                   total_conta += 20.00
                   print('\nX-Bacon adicionado ao carrinho!')

                elif escolha_lanche == '0':
                   print('\nVoltando ao menu...')
                   break
                   
            elif sub_escolha == '2':
                print("\n Combos disponíveis: ")
                print("[1] Combo Família - R$ 45,00")
                print("[2] Combo Duplo - R$ 30,00")
                print("[3] Combo Kid - R$ 20,00")

                escolha_combo = input ("\nSelecione o seu combo: ")

                if escolha_combo =='1':
                   carrinho.append("Combo Família")
                   total_conta += 45.00
                   print('\nCombo Familía adicionado ao carrinho!')

                elif escolha_combo == '2':
                   carrinho.append("combo Duplo")
                   total_conta += 30.00
                   print("\nCombo Duplo adicionado ao carrinho!")

                elif escolha_combo == '3':
                   carrinho.append("Combo Kid")
                   total_conta += 20.00
                   print("\nCombo Kid adicionado ao carrinho!")

                elif escolha_combo == '0':
                   print("\nVoltando ao menu...")
                   break


            
            elif sub_escolha == '3':
                print("\nBebidas disponíveis:")
                print("[1] Refrigerante - R$ 5,00")
                print("[2] Suco - R$ 7,00")
                print("[3] Água - R$ 3,00")

                escolha_bebida = input ("\nEscolha sua bebida: ")

                if escolha_bebida == '1':
                   carrinho.append("Refrigerante")
                   total_conta += 5.00
                   print("\nRefrigerante adicionado ao carrinho!")

                elif escolha_bebida == '2':
                   carrinho.append("Suco")
                   total_conta += 7.00
                   print("\nSuco adicionado ao carrinho!")

                elif escolha_bebida == '3':
                   carrinho.append("Água")
                   total_conta += 3.00
                   print("\nÁgua adicionada ao carrinho!")

                elif escolha_bebida == '0':
                   print("\nVoltando ao menu...")  
    
            elif sub_escolha == '4':
               print('\nSobremesas disponíveis:')
               print('[1] Geladinho de Amendoim - R$ 10,00')
               print('[2] Geladinho de Pudim - R$ 12,00')
               print('[3] Geladinho de Maracujá - R$ 10,00')
               print('[4] Geladinho de Morango - R$ 12,00')
               print('[5] Bolo de ninho no pote - R$ 10,00')

               escolha_dessert = input ("\nEscolha sua sobremesa:")

               if escolha_dessert == '1':
                  carrinho.append("Geladinho A")
                  total_conta += 10.00
                  print("\nGeladinho de Amendoim adicionado ao carrinho!")

               elif escolha_dessert == '2':
                  carrinho.append("Geladinho P")
                  total_conta += 12.00
                  print("\nGeladinho de Pudim adicionado ao carrinho!")

               elif escolha_dessert == '3':
                  carrinho.append("Geladinho MA")
                  total_conta += 10.00
                  print("\nGeladinho de Maracujá adicionado ao carrinho!")

               elif escolha_dessert == '4':
                  carrinho.append("Geladinho MO")
                  total_conta += 12.00
                  print("\nGeladinho de Morango adicionado ao carrinho!")

               elif escolha_dessert == '5':
                  carrinho.append("Bolo")
                  total_conta += 10.00
                  print("\nBolo de ninho adicionado ao carrinho!")

               elif escolha_dessert == '0':
                  print('\nVoltando ao menu...')
                  break   




            elif sub_escolha == '5':
                print("\nVoltando ao menu principal...")
                break
            
            else:
                print("\nOpção inválida. Tente novamente.")
                #Aqui consegui aprofundar minhas opções, colocando um outro While True


    elif escolha == '4':
       print('\n === Aqui fica registrados os pedidos ===')
       if not carrinho:
           print("\nO carrinho está vazio...")
       else:
           for item in carrinho:
               print(f"- {item}")
               print(f"\nTotal atual: R$ {total_conta:.2f}")

    elif escolha == '5':
       print('Precisa retirar algo?')

    elif escolha == '6':
       print('Finalizar pedido')

    elif escolha == '7':
       print('\nVeja nossos cupons!')
       input("Você tem um cupom de 5%. Deseja adicioná-lo?")
       print('Aplicando cupom de 5% de desconto...')
       total_conta = total_conta * 0.95
       print(f"Novo total: R$ {total_conta:.2f}")
       #Código para aplicar 5% de desconto nos itens que estão no carrinho.

    elif escolha == '8':
       print('\n === Entre em contato ===')
       mensagem = input ("Como podemos ajudar? Digite sua dúvida: ")

       message_suporte.append(mensagem)
       print("\n[Sistema]: Mensagem enviada com sucesso!")
       print("\n[Sistema]: Um atendente entrará em contato em breve. Protocolo: #12345")
       #Código para criar um mini chat de interação com o cliente.


    elif escolha == '9':
       print('Diga-nos o que achou?')

       carrinho = []
       total_conta = []
       message_suporte = []
       avaliacoes = []

       while True:
          nota = input ("De 0 a 5, Qual nota você nos avalia?")
          if nota in ['0','1','2','3','4','5']:
             break
          
          comentario = input("Deixe seu comentário (opcional): ")

          feedback_client = {
             "nota": nota,
             "comentario": comentario
          }
          avaliacoes.append(feedback_client)
          break

          print("\n Obrigado pelo seu feedback! Isso nos ajuda muito!")
          #Utilizando um dicionário, consegui criar um mini sistema de feedback. 



    elif escolha == '0':
     print('Saindo do sistema. Até logo!')
     break #O break quebra o loop, quando clicar no zero, ele para.

else:
   print('Opção inválida. Por favor, tente novamente.')
