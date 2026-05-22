import sys

sys.path.append("..")

import json
from util.data import converte_str_para_data
from entidades.médico import Médico, inserir_médico, get_médicos
from entidades.problema_saúde import ProblemaSaúde, inserir_problema_saúde
from entidades.paciente import Paciente, inserir_paciente, get_pacientes
from entidades.avaliação import Avaliação, inserir_avaliação
from interfaces.interface_textual import loop_operações_projeto


def carregar_objetos_arquivo():
    arquivo_entrada = open(
        file="../../dados/arquivo_entrada.json", mode="r", encoding="utf-8"
    )

    arquivo_dict = json.load(arquivo_entrada)

    for m_dict in arquivo_dict["médicos"]:
        inserir_médico(
            Médico(
                nome=m_dict["nome"],
                anos_experiencia=m_dict["anos_experiencia"],
                especialidade=m_dict["especialidade"],
            )
        )

    for p_dict in arquivo_dict["problemas_saúde"]:
        inserir_problema_saúde(
            ProblemaSaúde(
                título=p_dict["título"],
                sintomas=p_dict["sintomas"],
                tempo_recuperação=p_dict["tempo_recuperação"],
                custo_mensal=p_dict["custo_mensal"],
            )
        )

    pacientes_dict = arquivo_dict["pacientes"]
    for cpf in pacientes_dict:
        p_dict = pacientes_dict[cpf]
        paciente = Paciente(cpf=cpf, nome=p_dict["nome"], cidade=p_dict["cidade"])
        inserir_paciente(paciente)
        paciente.inserir_problemas_saúde(chaves_problemas=p_dict["chaves_problemas"])

    avaliações_dict = arquivo_dict["avaliações"]
    for cpf_paciente in avaliações_dict:
        paciente = get_pacientes()[cpf_paciente]
        médicos_dict = avaliações_dict[cpf_paciente]
        for nome_médico in médicos_dict:
            médico = get_médicos()[nome_médico]
            dados_avaliação = médicos_dict[nome_médico]
            data_obj = converte_str_para_data(dados_avaliação["data"])
            avaliação = Avaliação(data=data_obj, paciente=paciente, médico=médico)
            inserir_avaliação(avaliação)

    arquivo_entrada.close()


if __name__ == "__main__":
    carregar_objetos_arquivo()
    loop_operações_projeto()
