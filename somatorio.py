#NiCoding / EP2 - Python: Produtório e Somatório
#Somatório

# 
# 1) Inserção de dados para cálculo na fórmula (i e n)
# 


i = int(input('Insira o valor de i: '))
n = int(input('Insira o valor de n: '))

# 
# 2) Estrutura de repetição 'WHILE' com variáveis Acumuladora e Contadora
# 

somatorio = 0
while i <= n: #enquanto o valor de i for menor ou igual a n, executa-se o bloco de código abaixo:
    somatorio = somatorio + i #variavel acumulando somas que começam de 0 até o valor de n
    i = i + 1 #variavel contando valores em constância de 1 número (x + 1, x2 + 1...)

print(f'O somatório de {n}, é {somatorio}') #impressão do resultado