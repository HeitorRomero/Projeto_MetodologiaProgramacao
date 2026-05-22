from entidades.problema_saúde import get_problemas_saúde

pacientes = {}


def get_pacientes():
    return pacientes


def inserir_paciente(paciente):
    if paciente.cpf not in pacientes.keys():
        pacientes[paciente.cpf] = paciente
    else:
        print("Paciente " + paciente.nome + " já cadastrado")


class Paciente:
    def __init__(self, cpf, nome, cidade):
        self.cpf = cpf
        self.nome = nome
        self.cidade = cidade
        self.problemas_saúde = {}

    def inserir_problemas_saúde(self, chaves_problemas):
        for chave in chaves_problemas:
            if chave in get_problemas_saúde().keys():
                self.problemas_saúde[chave] = get_problemas_saúde()[chave]
            else:
                print("Problema " + chave + " não encontrado")

    def título(self):
        return self.nome + " (CPF: " + self.cpf + ")"

    def __str__(self):
        formato = "{:<16} {:<11} {:<14}"
        return formato.format(self.cpf, self.nome, self.cidade)
