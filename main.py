import bcrypt

senha_texto = (input('Digite sua senha : '))
senha_bytes = senha_texto.encode('utf-8')

salt = bcrypt.gensalt()
senha_criptografada =bcrypt.hashpw(senha_bytes,salt)

#print(f'Hash Gerado : {senha.decode('utf-8')}')
print(f"Hash gerado: {senha_criptografada.decode('utf-8')}")

print('\n--- Simulção de Login --- ')

senha_teste = input('Digite sua senha novamente para logar:').encode('utf-8')

if bcrypt.checkpw(senha_teste,senha_criptografada):
    print('Sucesso : Senha Correta!')
else:
    print('Erro : Senha Incorreta')