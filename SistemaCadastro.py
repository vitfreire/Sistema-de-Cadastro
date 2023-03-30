Nome = []
Matricula = []
Idade = []
Curso = []
 


def Menu():
    print("Olá, seja bem-vindo a Faculdade Nacional")
    print("1 - Cadastrar aluno")
    print("2 - Lista de Alunos Ativos")
    print("3 - Sair")
    retorno_resposta = input("Escolha uma opção:") 
    resposta(retorno_resposta)

def resposta(retorno_resposta):
    if retorno_resposta == "1":
        Matricula_cadastro()
    elif retorno_resposta == "2":
        Matriculas_existentes()
    elif retorno_resposta == "3":
        print("Programa encerrado, até logo")
    else:
        print("Opção Inválida")
        Menu()

def Matricula_cadastro():
    nome_aluno = input("Digite o nome completo do aluno:" )
    matricula_aluno = input("Digite a matricula do aluno:")
    idade_aluno = input("Digite a idade do aluno:")
    Curso_aluno = input("Digite o curso do aluno:")
    Nome.append(nome_aluno)
    Matricula.append(matricula_aluno)
    Idade.append(idade_aluno)
    Curso.append(Curso_aluno)
    print("\nAluno matriculado!\n") 
    Menu()

def Matriculas_existentes():
    if Matricula == []:
        print("\nNenhuma matricula encontrada")
        Menu()
    else:
        contador = 0
        print("#######################")
        print("\nMatriculas existentes")
        print("#######################")
        for e1 in Matricula:
            nome_X = Nome[contador]
            Curso_X = Curso[contador]
            idade_X = Idade[contador]
            dados_existentes = "\nMatricula: " + \
                str(e1)+"\nNome:" + str(nome_X) + \
                "\nCurso: " + str(Curso_X) + \
                "\nIdade: " + str(idade_X) + "\n"
            print(dados_existentes)
            contador = contador + 1
            print("----------------------")
        Menu()


Menu()