from PadroesDeProjetos.AT6_Proxy_Composite_Decorator.StreamingDeVideos.Classes.VideoReal import VideoReal
from PadroesDeProjetos.AT6_Proxy_Composite_Decorator.StreamingDeVideos.Interface.VideoInterface import VideoInterface


class ProxyVideo(VideoInterface):
    def __init__(self, nome_filme: str, usuario: dict):
        self.nome_filme = nome_filme
        self.usuario = usuario
        self._video_real = None

    def exibir(self) -> None:
        if not self.usuario.get('autenticado'):
            print(f"Acesso negado ao filme '{self.nome_filme}'. Usuário não autenticado.")
            return

        if self._video_real is None:
            print("[Proxy] Criando objeto VideoReal pela primeira vez...")
            self._video_real = VideoReal(self.nome_filme)

        self._video_real.exibir()
