from entidades.paciente import get_pacientes
from entidades.médico import get_médicos

avaliações = []


def get_avaliações():
    return avaliações


def inserir_avaliação(avaliação):
    if avaliação not in avaliações:
        avaliações.append(avaliação)
    else:
        print("avaliação já cadastrada.")


def criar_avaliação(cpf_paciente, nome_médico, data):
    paciente = get_pacientes().get(cpf_paciente)
    médico = get_médicos().get(nome_médico)

    if paciente and médico:
        nova_avaliação = Avaliação(data, paciente, médico)
        inserir_avaliação(nova_avaliação)


class Avaliação:
    def __init__(self, data, paciente, médico):
        self.data = data
        self.paciente = paciente
        self.médico = médico

    def __str__(self):
        formato = "{:<11} {:<11} {:<13}"
        avaliação_formatado = formato.format(
            str(self.data), self.paciente.nome, self.médico.nome
        )
        return avaliação_formatado
