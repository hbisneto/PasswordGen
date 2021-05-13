# PasswordGen (PasswordGen)

import random
import os
from datetime import date
from string import digits
from string import punctuation
from string import ascii_letters

AnoAtual = date.today().year
SoftwareName = "PasswordGen"
Version = "1.0.1"
CopyrightName = "Heitor Bisneto."
PassArray = []
NoteProcessor = []
SystemLocation = os.getcwd()
SaveFolder = SystemLocation + '/PasswordRepo/'
Extension = ['.txt']

FileName = str()
    
print("="*80)
print(f'[{SoftwareName}] - Em Execução...')
print("="*80)
print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if AnoAtual == 2021:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print()

def PrepararSistema():
    try:
        print("="*80)
        print(f'>> Verificação de arquivos do sistema {SoftwareName} <<')
        print("="*80)
        print(f'>> Verificando pasta: "{SaveFolder}"...')
        os.mkdir(SaveFolder)
        print(f'>> Pasta "{SaveFolder}" criada')
        print()
    except OSError:
        print(f'>> Status: Pasta "{SaveFolder}" configurada!')
        print()


def Menu():
    
    print("=" * 80)
    print('>> Menu <<')
    print("=" * 80)

    print("| 1. App() | >> Para abrir o app: Permite criar múltiplas senhas com o mesmo número de caracteres")
    print("| 2. QuickApp() | >> Para abrir o modo rápido: Cria uma senha")
    print("| 3. Save() | >> Para salvar senhas geradas: Salva as senhas geradas em um arquivo '.txt'")
    print("=" * 80)
    print(">> Nos dois primeiros módulos, o número de caracteres é escolhido pelo usuário. <<")
    print("=" * 80)
    MenuNumber = int(input(">> Digite o número da opção desejada: "))

    if MenuNumber == 1:
        App()
    elif MenuNumber == 2:
        QuickApp()
    elif MenuNumber == 3:
        Save()
    else:
        print(">> Opção inválida")

def App():
    print("=" * 80)
    print('>> Menu/App <<')
    print("=" * 80)
    QtPass = int(input(">> Digite a quantidade de senhas que deseja criar: "))
    PassLengh = int(input(">> Digite a quantidade de caracteres para a senha: "))
    Symbols = ascii_letters + digits + punctuation
    print()

    Counter = 0
    while Counter != QtPass:
        Counter += 1
        SecureFilter = random.SystemRandom()
        Password = "".join(SecureFilter.choice(Symbols)
                           for i in range(PassLengh))
        PassArray.append(Password)
        print(f'> Sua {Counter}º senha é: {Password}')
    print("=" * 80)
    print()

def QuickApp():
    print("=" * 80)
    print('>> Menu/QuickApp <<')
    print("=" * 80)
    PassLengh = int(input(">> Digite a quantidade de digitos para a senha: "))
    Symbols = ascii_letters + digits + punctuation
    print()

    SecureFilter = random.SystemRandom()
    Password = "".join(SecureFilter.choice(Symbols)
                       for i in range(PassLengh))
    PassArray.append(Password)
    print(f'> Sua nova senha é: {Password}')
    print("=" * 80)
    print()

def Save():
    FileName = str(input("Digite o nome do arquivo: "))
    print(">> Arquivo salvo com sucesso!")
    f = open(f'{SaveFolder}{FileName}.pwd', 'w')
    f.write(f'>> [{SoftwareName}] - Arquivo de senha\n\n')
    Count = 0
    for PassCodes in PassArray:
        Count += 1
        f = open(f'{SaveFolder}{FileName}.pwd', 'a')
        f.write(f'{Count} - {PassCodes}\n')
        f.close()
    PassArray.clear()

PrepararSistema() 
while True:
    Menu()
