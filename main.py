class Pessoa:
    pnome = ""
    pidade = ""

    def __init__(self, nome, idade):
        print("Nova pessoa:\n" + str(nome) + " " + str(idade) + " ano(s)");
        self.pnome = nome;
        self.pidade = str(idade)


pessoas = [];


def funcaoConfirma():
    confirma = input("Confirmar? 's' ou 'n'\n");
    if confirma == "s":
        return True;
    elif confirma == "n":
        return False;
    else:
        funcaoConfirma();


def lerComandos():
    comando = input("Digite um comando:\n1 - Cadastrar Pessoa\n2 - Ver Pessoas\n3 - Deletar Pessoa\n4 - Sair\n");
    comando = int(comando)
    if comando == 1:
        comandoCadastrar()
    elif comando == 2:
        comandoVer()
    elif comando == 3:
        comandoDeletar()
    elif comando == 4:
        exit(0)
    elif comando == 5:
        count = int(input("Quantidade:\n"))
        while (len(pessoas) < count):
            pessoas.append(pessoas[0]);
        lerComandos();
    else:
        print("Comando inválido!")


def comandoCadastrar():
    print("Cadastrar Pessoa")
    nome = input("Digite o Nome:\n")
    idade = input("Digita a Idade:\n")
    print("Deseja cadastrar a pessoa " + nome + " com " + idade + " ano(s)?");
    if (funcaoConfirma()):
        pessoas.append(Pessoa(nome, idade));
        print("Cadastrado com sucesso")
        lerComandos();
    else:
        comandoCadastrar();


def comandoVer():
    print("Ver Pessoas\n");
    print(str(len(pessoas)) + " pessoas cadastradas:\n");
    for pessoa in pessoas:
        index = pessoas.index(pessoa)
        print("Pessoa [" + str(index) + "] - Nome: " + pessoa.pnome + " | Idade: " + pessoa.pidade)
    lerComandos()


def comandoDeletar():
    print("Deletar")
    index = int(input("Digite o índice:\n"));
    if (index + 1) > len(pessoas):
        print("Índice não encontrado");
        lerComandos();
    del (pessoas[index])
    lerComandos()


def main():
    lerComandos()


if __name__ == '__main__':
    main()
