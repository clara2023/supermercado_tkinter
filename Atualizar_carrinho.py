from tkinter import *

class Atualizar_carrinho:
    def __init__(self):
        pass
    
    def adicionar(self, carrinho, produtos, indice, estoque, root):
        flag = False
        for a in range(1,len(produtos)):            
            if indice == str(produtos[a][0]):
                flag = True
                preco = produtos[a][2]
                nome = produtos[a][1]
                break
            
        if flag == True:
            carrinho.append([nome,estoque,preco])
            mensagem = Label(root, text='Produto cadastrado com sucesso!',font= ('Bahnschrift Light SemiCondensed', 12, 'bold'), fg = 'green')
            mensagem.place(x = '150',y='480')  
        
        else:
            
            mensagem = Label(root, text='Produto não cadastrado!                 ',font= ('Bahnschrift Light SemiCondensed', 12, 'bold'), fg = 'red')
            mensagem.place(x = '150',y='480')
                
        print(carrinho)
        
        listbox = Listbox(root, font=('Arial', 9, 'bold'), width = 39)
        listbox.place(x='700', y='340')
        copia = list()
        for a in range(len(carrinho)):
            copia.append([])
        for b in range(len(carrinho)):
            copia[b].append(carrinho[b][0])
            copia[b].append(carrinho[b][1])

        print(f'carrinho {carrinho}')
        print(copia)

        for i in copia:
            listbox.insert(END, i)

        return carrinho



    def deletar(self, carrinho, nome,root):

        flag = False
        for a in range(len(carrinho)):            
            if nome == carrinho[a][0]:
                del carrinho[a]
                mensagem = Label(root, text='Produto deletado com sucesso!',font= ('Bahnschrift Light SemiCondensed', 12, 'bold'), fg = 'green')
                mensagem.place(x = '150',y='480')
                flag = True
                break
        if flag == False:
            mensagem = Label(root, text='Produto não cadastrado!                 ',font= ('Bahnschrift Light SemiCondensed', 12, 'bold'), fg = 'red')
            mensagem.place(x = '150',y='480')
        listbox = Listbox(root, font=('Arial', 9, 'bold'), width = 39)
        listbox.place(x='700', y='340')
        copia = list()
        for a in range(len(carrinho)):
            copia.append([])
        for b in range(len(carrinho)):
            copia[b].append(carrinho[b][0])
            copia[b].append(carrinho[b][1])

        print(f'carrinho {carrinho}')
        print(copia)

        for i in copia:
            listbox.insert(END, i)
        return carrinho



    def modificar(self, carrinho, nome, estoque,root):
        print(carrinho)
        flag = False
        for a in range (len(carrinho)):
            if nome in carrinho[a][0]:
                flag = True
                    
                if estoque == str(0): #se o valor desejado for zero, o item sera excluido
                    for a in range(len(carrinho)):            
                        if nome == carrinho[a][0]:
                            indice = a
                            del carrinho[a]
                            break                                          
                       
                else:
                    for a in range(len(carrinho)):            
                        if nome == carrinho[a][0]:
                            carrinho[a][1] = estoque
                            break
                print(carrinho)        

                mensagem = Label(root, text='Produto alterado com sucesso!',font= ('Bahnschrift Light SemiCondensed', 12, 'bold'), fg = 'green')
                mensagem.place(x = '150',y='480')  

        if flag == False:
            mensagem = Label(root, text='Produto não cadastrado!                    ',font= ('Bahnschrift Light SemiCondensed', 12, 'bold'), fg = 'red')
            mensagem.place(x = '150',y='480')

        listbox = Listbox(root, font=('Arial', 9, 'bold'), width = 39)
        listbox.place(x='700', y='340')
        copia = list()
        for a in range(len(carrinho)):
            copia.append([])
        for b in range(len(carrinho)):
            copia[b].append(carrinho[b][0])
            copia[b].append(carrinho[b][1])

        print(f'carrinho {carrinho}')
        print(copia)

        for i in copia:
            listbox.insert(END, i)

        return carrinho


