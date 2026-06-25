#Operadores Lógicos 
#and (e) or (ou) not (não)
#quando se utiliza and todas as frases precisam ser verdadeiras
#se qualquer valor acabar for considerado falso 
#a expressão inteira será avaliada naquele valor 
#São consideradas FalsY (não False)
#0 0.0 ''(string vazia) e False 
#Também existe o tipo None (Nenhum) que é 
#usado para representar um não valor ele basiscamente não existe 
entrada = input ('{E}ntrar {S}air:')
senha_digitada = input ('Senha:')
senha_permitida = '123456'
if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
    print('Entrar')
else: 
    print('Sair')
