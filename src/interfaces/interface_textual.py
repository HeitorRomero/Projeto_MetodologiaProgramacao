from util.gerais import (
    imprimir_objetos,
    ordenar_objetos_por_um_atributo,
    ordenar_objetos_por_dois_atributos,
)
from entidades.médico import get_médicos
from entidades.paciente import get_pacientes
from entidades.avaliação import get_avaliações
from entidades.problema_saúde import get_problemas_saúde


def ler_int_positivo(dado):
    try:
        string = input("- " + dado + ": ")
        if len(string) == 0:
            return None
        if len(string) > 0:
            int_positivo = int(string)
            if int_positivo > 0:
                return int_positivo
    except ValueError:
        pass
    print("Erro na leitura/conversão do inteiro positivo: " + dado)
    return None


def ler_sair_loop(loop):
    try:
        sair = input("\n- sair do loop de " + loop + " [S]: ")
        if sair.upper() == "S":
            return True
        else:
            return False
    except IOError:
        pass
    return False


def imprimir_títulos(cabeçalho, títulos, arquivo=None):
    print("\n" + cabeçalho)
    if arquivo is not None:
        arquivo.write("\n" + cabeçalho + "\n")
    for índice, título in enumerate(títulos):
        formato = "{:<4} {}"
        string = formato.format(f"{(índice + 1):2d} -", título)
        print(string)
        string += "\n"
        if arquivo is not None:
            arquivo.write(string)


def loop_operações_projeto():
    arquivo_saída = open(
        file="../../dados/arquivo_saída.txt", mode="w", encoding="utf-8"
    )
    sair_loop = False
    while not sair_loop:
        operações_str = (
            "\nSistema de Avaliações Médicas"
            + "\n1 - Médicos"
            + "\n2 - Pacientes"
            + "\n3 - Avaliações"
            + "\n4 - Problemas de Saúde"
            + "\n5 - Operações de um Paciente"
        )
        print(operações_str)
        arquivo_saída.write(operações_str + "\n")

        questão = "número da operação do Projeto a ser executada"
        operação = ler_int_positivo(questão)
        if operação is None:
            break

        questão_resposta = questão + ": " + str(operação) + "\n"
        arquivo_saída.write(questão_resposta)

        if operação == 1:
            imprimir_objetos(
                "Médicos: nome, experiência, especialidade",
                get_médicos().values(),
                arquivo_saída,
            )
        elif operação == 2:
            imprimir_objetos(
                "Pacientes: cpf, nome, cidade", get_pacientes().values(), arquivo_saída
            )
        elif operação == 3:
            imprimir_objetos(
                "Avaliações: data, paciente, médico", get_avaliações(), arquivo_saída
            )
        elif operação == 4:
            imprimir_objetos(
                "ProblemasSaúde: título, sintomas, tempo, custo",
                get_problemas_saúde().values(),
                arquivo_saída,
            )
        elif operação == 5:
            loop_títulos_pacientes(arquivo_saída)

        sair_loop = ler_sair_loop("operações do Projeto")
    arquivo_saída.close()


def loop_títulos_pacientes(arquivo_saída):
    sair_loop = False
    cpfs = list(get_pacientes().keys())
    títulos = [get_pacientes()[cpf].título() for cpf in cpfs]

    while not sair_loop:
        imprimir_títulos("Selecionar o Paciente", títulos, arquivo_saída)
        questão = "número do Paciente a ser executado"
        índice = ler_int_positivo(questão)
        if índice is None:
            break

        questão_resposta = questão + ": " + str(índice) + "\n"
        arquivo_saída.write(questão_resposta)

        if 1 <= índice <= len(cpfs):
            paciente = get_pacientes()[cpfs[índice - 1]]
            loop_operações_paciente(paciente, arquivo_saída)

        sair_loop = ler_sair_loop("títulos dos Pacientes")


def loop_operações_paciente(paciente, arquivo_saída):
    sair_loop = False
    problemas = list(paciente.problemas_saúde.values())

    while not sair_loop:
        operações = (
            "\nPaciente: "
            + paciente.título()
            + "\n1 - Problemas de Saúde do Paciente"
            + "\n2 - Problemas: ordenação crescente por custo mensal"
            + "\n3 - Problemas: ordenação decrescente por tempo de recuperação"
            + "\n4 - Problemas: ordenação decrescente por tempo e custo"
        )
        print(operações)
        arquivo_saída.write(operações + "\n")

        questão = "número da operação do Paciente a ser executada"
        operação = ler_int_positivo(questão)
        if operação is None:
            break

        questão_resposta = questão + ": " + str(operação) + "\n"
        arquivo_saída.write(questão_resposta)

        if operação == 1:
            imprimir_objetos(
                "Problemas de Saúde do Paciente: título, sintomas, tempo, custo",
                problemas,
                arquivo_saída,
            )
        elif operação == 2:
            imprimir_objetos(
                "Problemas de Saúde: ordenação crescente por custo",
                ordenar_objetos_por_um_atributo(
                    problemas, lambda item: item.custo_mensal, False
                ),
                arquivo_saída,
            )
        elif operação == 3:
            imprimir_objetos(
                "Problemas de Saúde: ordenação decrescente por tempo",
                ordenar_objetos_por_um_atributo(
                    problemas, lambda item: item.tempo_recuperação, True
                ),
                arquivo_saída,
            )
        elif operação == 4:
            imprimir_objetos(
                "Problemas de Saúde: ordenação decrescente por tempo e custo",
                ordenar_objetos_por_dois_atributos(
                    problemas,
                    lambda item: item.tempo_recuperação,
                    lambda item: item.custo_mensal,
                    True,
                ),
                arquivo_saída,
            )

        sair_loop = ler_sair_loop("operações do Paciente")
