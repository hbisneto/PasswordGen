import random
import os
from datetime import date
from string import digits
from string import punctuation
from string import ascii_letters

AnoAtual = date.today().year
SoftwareName = "PasswordGen"
Version = "1.0"
CopyrightName = "Heitor Bisneto."
PassArray = []
NoteProcessor = []
SystemLocation = os.getcwd()
SaveFolder = SystemLocation + '/Saved/'
NotesFolder = SystemLocation + '/Saved/'
Extension = ['.txt']

NomeNota = str()
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
    Menu()

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
    Menu()

def SystemPrepare():
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

def SalvarNota():
    Count = 0
    NewLine = "\n"
    
    print("="*80)
    print(f'>> Salvar Nota: <<')
    print("="*80)
    NomeNota = str(input(">> Nome da Nota: "))
    print("="*80)
    print(f'>> Extensão do arquivo: <<')
    print("="*80)

    for Format in Extension:
        Count += 1
        print(f'{Count} {Format}')
    print("="*80)
    Opc = int(input(">> Escolha a extensão da Nota: "))

    if Extension[Opc - 1] == ".rtf":
        NotaExport = f'{NotesFolder}{NomeNota}{Extension[Opc-1]}'
        NomeNota = f'{NomeNota}{Extension[Opc-1]}'
        
        RTFLib.FileName = NotaExport
        RTFLib.NomeNota = NomeNota
        RTFLib.SaveRTF()
    else:
        try:
            f = open(f'{NotesFolder}{NomeNota}{Extension[Opc-1]}', 'x')
            print(f'>> Nota salva como "{NomeNota}{Extension[Opc-1]}"')
            for Writer in NoteProcessor:
                f.write(Writer + NewLine)
            print('>> Digite "App()" para executar o programa novamente')

        except:
            print("="*80)
            print(f'>> Arquivo já existente: <<')
            print('>> Gostaria de sobreescrever?')
            print("="*80)
            print('1. Sim')
            print('2. Não')
            print("="*80)
            Confirm = int(input(f'>> Digite o número da opção: '))

            if Confirm == 1:
                f = open(f'{NotesFolder}{NomeNota}{Extension[Opc-1]}', 'w')
                print(f'>> Nota salva como "{NomeNota}{Extension[Opc-1]}"')
                for Writer in NoteProcessor:
                    f.write(Writer + NewLine)
                print('>> Digite "App()" para executar o programa novamente')
            else:
                print(">> A Nota não foi salva!")
                App()

def Save():
    NewLine = "\n"
    
    print("="*80)
    print(f'[MyNotes] - Exportar para RTF Document...')
    print("="*80)

    NewFile = str(input("Insira um nome: "))
    
    try:
        f = open(f'{NotesFolder}{NewFile}.txt', 'x')
        print(f'>> Nota salva como "{NomeNota}"')
        f.write(f'>> PasswordGen: Abaixo a lista de senhas geradas <<\n\n')
        for Writer in CreateNote.NoteProcessor:
            f.write(f'{Writer}\{NewLine}')
        f = open(f'{FileName}', 'a')
        f.write("}")
        print('>> Digite "App()" para executar o programa novamente')

    except:
        print("="*80)
        print(f'>> Arquivo já existente: <<')
        print('>> Gostaria de sobreescrever?')
        print("="*80)
        print('1. Sim')
        print('2. Não')
        print("="*80)
        Confirm = int(input(f'>> Digite o número da opção: '))

        if Confirm == 1:
            f = open(f'{NotesFolder}{FileName}', 'w')
            print(f'>> Nota salva como "{NomeNota}"')
            f.write(f'>> PasswordGen: Abaixo a lista de senhas geradas <<\n\n')
            for Writer in CreateNote.NoteProcessor:
                f.write(f'{Writer}\{NewLine}')
            f = open(f'{FileName}', 'a')
            f.write("}")
            print('>> Digite "App()" para executar o programa novamente')
        else:
            print(">> A Nota não foi salva!")
            App()
            
    Menu()

def Menu():
    
    print("=" * 80)
    print('>> Menu <<')
    print("=" * 80)

    print("| 1. App() | >> Para abrir o app: Permite criar múltiplas senhas com o mesmo número de caracteres")
    print("| 2. QuickApp() | >> Para abrir o modo rápido: Cria uma senha")
    print("| 3. Save() | >> Para salvar senhas geradas: Salva as senhas geradas em um arquivo '.txt'")
    print("=" * 80)
    print(">> Nos dois módulos, o número de caracteres é escolhido pelo usuário. <<")
    print("=" * 80)

    MenuNumber = int(input(">> Digite o número da opção desejada: "))

    if MenuNumber == 1:
        App()
    elif MenuNumber == 2:
        QuickApp()
    elif MenuNumber == 3:
        Save()
        #SalvarNota()
    else:
        print(">> Opção inválida")

Menu()
