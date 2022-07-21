# import platform
import getpass
# from datetime import datetime

# print(platform.node())
# print(platform.architecture())
# print(platform.system())
# print(platform.release())
# print(platform.processor())
# print(platform.node())
#
# print(datetime.now().year)

usuario=getpass.getuser()
senha=getpass.getpass("Digite sua senha: ")

if usuario == 'Pichau' and senha == 'Hello':
    print("Bem vindo a Dell")
else:
    print("Você não tem acesso")