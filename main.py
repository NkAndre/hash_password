import bcrypt

senha_texto = (input('Digite sua senha : '))
senha_bytes = senha_texto.encode('utf-8')

salt = bcrypt.gensalt()
senha_criptografada =bcrypt.hashpw(senha_bytes,salt)

#print(f'Hash Gerado : {senha.decode('utf-8')}')
print(f"Hash gerado: {senha_criptografada.decode('utf-8')}")