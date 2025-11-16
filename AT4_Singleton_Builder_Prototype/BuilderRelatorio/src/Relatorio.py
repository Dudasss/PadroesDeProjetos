class Relatorio:
    def __init__(self, formato):
        self.formato = formato
        self.titulo = None
        self.corpo = None
        self.graficos = None
        self.rodape = None
        # print(f"Iniciando novo relatório formato {self.formato}.")

    def __str__(self):
        partes = [f"Relatório gerado em {self.formato.upper()}"]
        if self.titulo:
            partes.append(self.titulo)
        if self.corpo:
            partes.append(self.corpo)
        if self.graficos:
            partes.append(self.graficos)
        if self.rodape:
            partes.append(self.rodape)

        return "\n" + "\n".join(partes) + "\n"
