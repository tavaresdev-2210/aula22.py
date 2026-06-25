entrada = input ('{E}ntrar {S}air:')
senha_digitada = input ('Senha:')
senha_permitida = '123456'
if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
    print('Entrar')
else: 
    print('Sair')
#nesta aula aprendemos a diferença entre 'E' e o 'e' se o cliente 
#utilizar a letra minúscula conseguir entrar no sistema, se não 
#tiver o 'or' ele não entra 
