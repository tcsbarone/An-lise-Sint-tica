from beautifultable import BeautifulTable
import copy

print("*****************************************")
print("****Bem vindo ao Analisador Sintático****")
print("*****************************************")

table = BeautifulTable()
table.column_headers = ["PILHA", "CADEIA", "REGRA"]

print("\n")
a = input("Digite aqui a sua PILHA!! --> ")
pilha = a.split()

print("\n")
b = input("Digite aqui a sua CADEIA!! --> ")
cadeia = b.split()

pilha_copia = pilha.copy()
cadeia_copia = cadeia.copy()

topo_pilha = pilha[-1]
topo_cadeia = cadeia[0]

tabela = {
        'E': {"id":['T','S'],
              "num":['T','S'],
              "+":[],
              "-":[],
              "*":[],
              "/":[],
              "(":['T','S'],
              ")":[],
              "$":[]},
        'T': {"id":['F','G'],
              "num":['F','G'],
              "+":[],
              "-":[],
              "*":[],
              "/":[],
              "(":['F','G'],
              ")":[],
              "$":[]},
        'S': {"id":[],
              "num":[],
              "+":['+','T','S'],
              "-":['-','T','S'],
              "*":[],
              "/":[],
              "(":[],
              ")":['y'],
              "$":['y']},
        'G': {"id":[],
              "num":[],
              "+":['y'],
              "-":['y'],
              "*":['*','F','G'],
              "/":['/','F','G'],
              "(":[],
              ")":['y'],
              "$":['y']},
        'F': {"id":['id'],
              "num":['num'],
              "+":[],
              "-":[],
              "*":[],
              "/":[],
              "(":['(E)'],
              ")":[],
              "$":[]},
        }
topo_pilha = pilha[-1]
topo_cadeia = cadeia[0]

table.append_row([pilha,cadeia, tabela[topo_pilha][topo_cadeia]])

while(cadeia_copia != []):

    pc = copy.copy(pilha_copia)
    cc = copy.copy(cadeia_copia)

    if(cadeia_copia == ['$'] and pilha_copia == ['$','y']):
        pilha_copia.pop(-1)
        table.append_row([pilha_copia,cc,'====SUCESSO===='])
        break
    
    topo_pilha = pilha_copia[-1]
    topo_cadeia = cadeia_copia[0]

    if(topo_pilha == 'y'):
        pilha_copia.pop(-1)
        topo_pilha = pilha_copia[-1]
    
    if((topo_pilha == 'E') or
       (topo_pilha == 'T') or
       (topo_pilha == 'S') or
       (topo_pilha == 'G') or
       (topo_pilha == 'F') or
       (topo_pilha == '$')):
        if(topo_pilha == topo_cadeia):
            cadeia_copia.pop(0)
            table.append_row([pc,cc,'====RECONHECE===='])
            pilha_copia.pop(-1)
        else:
            if(tabela[topo_pilha][topo_cadeia]):
                print(pilha_copia)
                pilha_copia.pop(-1)
                pilha_copia += reversed(tabela[topo_pilha][topo_cadeia])
                table.append_row([pc,cc,tabela[topo_pilha][topo_cadeia]])
            else:
                print("Querido Robô, não dá para prosseguir aqui! :(")
                break
    else:
        if(topo_pilha == topo_cadeia):
            pilha_copia.pop(-1)
            cadeia_copia.pop(0)
            table.append_row([pc,cc,'====RECONHECE===='])
        else:
            print("Querido Robô, também não dá para prosseguir aqui! :(")
            break
        

print(table)
