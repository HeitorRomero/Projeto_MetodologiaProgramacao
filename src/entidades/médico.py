médicos = {}


def get_médicos():
    return médicos


def inserir_médico(médico):
    nome_médico = médico.nome

    if nome_médico not in médicos.keys():
        médicos[nome_médico] = médico
    else:
        print("Médico " + nome_médico + " já tem cadastro no sistema")


class Médico:

    def __init__(self, nome, anos_experiencia, especialidade):
        self.nome = nome
        self.anos_experiência = anos_experiencia
        self.especialidade = (
            especialidade
            if especialidade in ("cardiologia", "pneumologia")
            else "indefinida"
        )

    def __str__(self):
        formato = "{:<9} {:<9} {:<13}"
        médico_formatado = formato.format(
            self.nome, str(self.anos_experiência) + " anos", self.especialidade
        )
        return médico_formatado
