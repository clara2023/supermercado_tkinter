from Atualizar_carrinho import *
from tkinter import *
from tabela import *
#import botoes 



def pressiona_botao_carrinho(botao_carrinho):
    botao_carrinho.destroy()
    
    botao_inserir = Button(root, width='10', text= 'INSERIR', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : inserir_prod_carrinho())        
    botao_inserir.place(x=100,y=550)

    botao_atualizar = Button(root, width='10', text= 'ATUALIZAR', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : alterar_prod_carrinho())        
    botao_atualizar.place(x=300,y=550)

    botao_deletar = Button(root, width='10', text= 'DELETAR', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : deletar_prod_carrinho() )        
    botao_deletar.place(x=500,y=550)
    root.mainloop()

    
    
def inserir_prod_carrinho():
    #produtos, nome, preco, estoque
    x = Atualizar_carrinho()

    label = Label(root, text='                                                  ',font= ('Bahnschrift Light SemiCondensed', 15, 'bold'))
    label.place(x = '150',y='480')

    label_indice = Label(root, text='Índice',font= ('Bahnschrift Light SemiCondensed', 15, 'bold'))
    label_indice.place(x = '100',y='300')
    
    label_quantidade = Label (root, text = 'Quantidade', font = ('Bahnschrift Light SemiCondensed', 15, 'bold'))
    label_quantidade.place (x = '100', y = '400')

    
    entry_indice = Entry (root, width = 20)
    entry_indice.place (x='250', y='300')   
    
    entry_quantidade = Entry (root, width = 20)
    entry_quantidade.place (x='250', y='400')          
 
    
    botao_adicionar_item = Button(root, width='10', text= 'ADICIONAR', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : x.adicionar(carrinho, produtos, entry_indice.get(), entry_quantidade.get(),root))        
    botao_adicionar_item.place(x=400,y=350)
    print(produtos)




def alterar_prod_carrinho():
    #produtos, nome, preco, estoque
    x = Atualizar_carrinho()

    label = Label(root, text='                                                   ',font= ('Bahnschrift Light SemiCondensed', 15, 'bold'))
    label.place(x = '150',y='480')

    label_nome = Label(root, text='Nome',font= ('Bahnschrift Light SemiCondensed', 15, 'bold'))
    label_nome.place(x = '100',y='300')
    
    label_quantidade = Label (root, text = 'Quantidade', font = ('Bahnschrift Light SemiCondensed', 15, 'bold'))
    label_quantidade.place (x = '100', y = '400')

    
    entry_nome = Entry (root, width = 20)
    entry_nome.place (x='250', y='300')   
    
    entry_quantidade = Entry (root, width = 20)
    entry_quantidade.place (x='250', y='400')          
 
    
    botao_adicionar_item = Button(root, width='10', text= 'MODIFICAR', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : x.modificar(carrinho, entry_nome.get(), entry_quantidade.get(),root))        
    botao_adicionar_item.place(x=400,y=350)
    print(produtos)




def deletar_prod_carrinho():
    label = Label (root, text = '                         ', font = ('Bahnschrift Light SemiCondensed', 15, 'bold'))
    label.place (x = '100', y = '400')
    
    label2 = Label (root, text = '                                         ')
    label2.place (x='250', y='400') 

    #produtos, nome, preco, estoque
    x = Atualizar_carrinho()

    label = Label(root, text='                                                   ',font= ('Bahnschrift Light SemiCondensed', 15, 'bold'))
    label.place(x = '150',y='480')

    label_nome = Label(root, text='Nome',font= ('Bahnschrift Light SemiCondensed', 15, 'bold'))
    label_nome.place(x = '100',y='300')

    
    entry_nome = Entry (root, width = 20)
    entry_nome.place (x='250', y='300')   

    
    botao_adicionar_item = Button(root, width='10', text= 'DELETAR', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : x.deletar(carrinho, entry_nome.get(),root))        
    botao_adicionar_item.place(x=400,y=350)
    print(produtos)



root = Tk()
t = Tabela(root)


botao_carrinho = Button(root, width='10', text= 'CARRINHO', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : pressiona_botao_carrinho(botao_carrinho))        
botao_carrinho.place(x=300,y=550)

listbox = Listbox(root, font=('Arial', 9, 'bold'), width = 39)
listbox.place(x='700', y='170')

root.mainloop()
