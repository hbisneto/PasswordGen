# PasswordGen

O PasswordGen é um gerador de senhas.

## Principais Recursos:

* **Número de senhas:**
<br> Possibilidade de criar multiplas senhas com o número de digitos escolhido pelo usuário

* **Modo Rápido:**
<br> Possibilidade de criar uma única senha com o número de caracteres escolhido pelo usuário

* **Salvar Como Documento:**
<br> Salva as senhas geradas em um arquivo de texto.

## Log de Atualização

```
Versão 1.0:
- Versão de lançamento do Script
```

```
Versão 1.0.1:
>> Final da fase de testes do recurso "Salvar Como Documento"
>> Reimplementação do recurso "Salvar Como Documento"
O recurso salva o documento em um arquivo ".pwd"
>> Implementação da função "PrepararSistema()"
Função cria a pasta "PasswordRepo" onde serão salvos os documentos
>> Remoção de variáveis duplicadas no código
>> Reorganização do código fonte
>> O sistema não verifica mais se o arquivo já existe. No momento do salvamento, se o arquivo de senhas já existir, ela será substituido pelo novo arquivo salvo. [Improvement]
>> Agora, após o termino da execução de cada módulo, o sistema executa o Menu.
```