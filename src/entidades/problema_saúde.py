problemas_saúde = {}


def get_problemas_saúde():
    return problemas_saúde


def inserir_problema_saúde(problema):
    if problema.título not in problemas_saúde.keys():
        problemas_saúde[problema.título] = problema
    else:
        print("Problema " + problema.título + " já cadastrado")


class ProblemaSaúde:
    def __init__(self, título, sintomas, tempo_recuperação, custo_mensal):
        self.título = título
        self.sintomas = sintomas
        self.tempo_recuperação = tempo_recuperação
        self.custo_mensal = custo_mensal

    def __str__(self):
        formato = "{:<11} {:<14} {:<9} {:<12}"
        return formato.format(
            self.título,
            self.sintomas,
            str(self.tempo_recuperação) + " dias",
            "R$ " + str(self.custo_mensal),
        )
