#NiCoding / EP2 - Python: Produtório e Somatório
#Produtório

# 
# 1) Inserção de dados para cálculo na fórmula (i e n)
# 


i = int(input('Insira o valor de i: '))
n = int(input('Insira o valor de n: '))

# 
# 2) Estrutura de repetição 'WHILE' com variáveis Acumuladora e Contadora
# 

produtorio = 1
while i <= n: #enquanto o valor de i for menor ou igual a n, executa-se o bloco de código abaixo:
    produtorio = produtorio * i #variavel acumulando multiplicações que começam de 1 até o valor de n
    i = i + 1 #variavel contando valores em constância de 1 número (x + 1, x2 + 1...)

print(f'O produtório de {n}, é {produtorio}') #impressão do resultado