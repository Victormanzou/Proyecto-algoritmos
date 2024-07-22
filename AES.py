from cryptography.fernet import Fernet

def generar_clave():
    return Fernet.generate_key()
    
def encriptar_texto(texto, clave):
    f = Fernet(clave)
    texto_encriptado = f.encrypt(texto.encode())
    return texto_encriptado
 
def desencriptar_texto(texto_encriptado,clave):
    f = Fernet(clave)
    texto_desencriptado = f.decrypt(texto_encriptado).decode()
    return texto_desencriptado
    
clave_secreta = generar_clave()
texto_original = "contraseña aes"
texto_encriptado = encriptar_texto(texto_original, clave_secreta)
print(f'texto original: {texto_original}')
print(f'texto encriptado: {texto_encriptado}')