from PadroesDeProjetos.AT4_Singleton_Builder_Prototype.PrototypeModelagemDocumentos.Contrato import Contrato


def sistema_documento():
    """"
        1) Criar um contrato base (o protótipo original).
        2) Cloná-lo para dois clientes diferentes.
        3) Modificar os clones.
        4) Verificar se o original permaneceu intacto.
    """
    # CONTRATO BASE
    contrato_base  = Contrato(
        titulo="Contrato de Aluguel BASE",
        corpo="Esse é o corpo do 'Contator de Aluguel'...",
        clausulas=["Cláusula 1: CL1", "Cláusula 2: CL2", "Cláusula 3: CL3"],
        rodape="Dudasss Inc"
    )
    # VERIFICANDO CONTRATO BASE
    print(f"{'-' * 40}")
    # print("CONTRATO BASE")
    print(contrato_base)
    print(f"{'-' * 40}")

    # CLONAR PARA DUAS CLIENTES DIFERENTES
    contrato_eduarda = contrato_base.clone()
    contrato_rafella = contrato_base.clone()

    # MODIFICAR OS CLONES 1
    contrato_eduarda.titulo = "Contrato de Aluguel - EDUARDA"
    contrato_eduarda.rodape = "Assinatura: Eduarda Samanta"
    contrato_eduarda.clausulas.append("Clausula 4: CL4")
    # print("CONTRATO EDUARDA")
    print(contrato_eduarda)
    print(f"{'-' * 40}")

    # MODIFICAR OS CLONES 2
    contrato_rafella.titulo = "Contrato de Aluguel - RAFAELLA"
    contrato_rafella.rodape = "Assinatura: Rafaella"
    contrato_rafella.clausulas.append("Clausula 5: CL5")
    # print("CONTRATO EDUARDA")
    print(contrato_rafella)
    print(f"{'-' * 40}")

    # VERIFICANDO CONTRATO BASE
    # print("CONTRATO BASE")
    print(contrato_base)
    print(f"{'-' * 40}")


if __name__ == "__main__":
    sistema_documento()
