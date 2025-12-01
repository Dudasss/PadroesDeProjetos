from PadroesDeProjetos.AT6_Proxy_Composite_Decorator.StreamingDeVideos.Interface.VideoInterface import VideoInterface


class VideoReal(VideoInterface):
    def __init__(self, nome_filme: str):
        self.nome_filme = nome_filme
        self._carregar_do_disco()

    def _carregar_do_disco(self):
        print(f"Carregando arquivo de vídeo '{self.nome_filme}' do servidor... (Isso custa recursos)")

    def exibir(self) -> None:
        print(f"Reproduzindo o filme: '{self.nome_filme}'")


