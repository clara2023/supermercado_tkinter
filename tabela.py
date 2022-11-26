from tkinter import *



class Tabela:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(len(produtos)):
            for j in range(4):
                 
                self.e = Entry(root, width=20, fg='black', font=('Arial',16,'bold'))
               
                self.e.grid(row=i, column=j)
                self.e.insert(END, produtos[i][j])
                



carrinho = []

# take the data
produtos = [['Índice','Nome','Preço','Estoque'],
            [1,'Maçã',6,10],
            [2,'Banana',4,14],
            [3,'Alface',5,4],
            [4,'Leite',6,7],
            [5,'Queijo',12,3]]

