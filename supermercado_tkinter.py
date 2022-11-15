from tkinter import *

def deletar(widget):
    widget.destroy()

def texto(flag):
   
    label_quantidade = Label (root, text = 'Quantidade', font = ('Bahnschrift Light SemiCondensed', 22, 'bold'))
    label_quantidade.place (x = '100', y = '500')
    
    label_codigo = Label (root, text = 'Código', font = ('Bahnschrift Light SemiCondensed', 22, 'bold'))
    label_codigo.place(x='100', y = '430')
    
    entry_codigo = Entry (root, width = 20)
    entry_codigo.place (x='280', y='445')          
  
    entry_quantidade = Entry (root, width = 20)
    entry_quantidade.place (x='280', y='510')  

    if flag == 1:
        label_inserir = Label (root, text = '   Insira um produto: ', font = ('Bahnschrift Light SemiCondensed', 20, 'bold'))
        label_inserir.place(x='300', y='300')

      

    elif flag == 2:
        label_atualizar = Label (root, text = 'Atualize um produto: ', font = ('Bahnschrift Light SemiCondensed', 20, 'bold'))
        label_atualizar.place(x='300', y='300')

    else:
        label_quantidade.pack_forget()
        label_codigo.pack_forget()
        entry_quantidade.pack_forget()
        '''
        root.mainloop()
        label_deletar = Label (root, text = '  Delete um produto: ', font = ('Bahnschrift Light SemiCondensed', 20, 'bold'))
        label_deletar.place(x='300', y='300')
        '''
   
 
class Tabela:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='black', font=('Arial',16,'bold'))
               
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
                
        listbox = Listbox(root, font=('Arial', 9, 'bold'), width = 39)
        listbox.place(x='700', y='170')



        botao_inserir = Button(root, width='10', text= 'INSERIR', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : texto(1))        
        botao_inserir.grid(row=10,column=0)

        botao_atualizar = Button(root, width='10', text= 'ATUALIZAR', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : texto(2))        
        botao_atualizar.grid(row=10,column=1)

        botao_deletar = Button(root, width='10', text= 'DELETAR', font = ('Bahnschrift Light SemiCondensed', 10, 'bold'), command = lambda : texto(3) )        
        botao_deletar.grid(row=10,column=2)
        

maca = 10
banana = 14
alface = 4
leite = 7
queijo = 3


# take the data
lst = [('Índice','Nome','Preço','Estoque'),
       (1,'Maçã',6,maca),
       (2,'Banana',4,banana),
       (3,'Alface',5,alface),
       (4,'Leite',6,leite),
       (5,'Queijo',12,queijo)]
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = Tk()
t = Tabela(root)
root.mainloop()