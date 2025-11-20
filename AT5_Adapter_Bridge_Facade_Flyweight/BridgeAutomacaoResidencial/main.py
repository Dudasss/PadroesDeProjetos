from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.ClassesControle.AplicativoMovel import \
    AplicativoMovel
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.ClassesControle.ControleRemoto import \
    ControleRemoto
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.ClassesControle.PainelControle import \
    PainelControle
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.ClassesDispositivos.Camera import \
    Camera
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.ClassesDispositivos.Lampada import \
    Lampada
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.BridgeAutomacaoResidencial.ClassesDispositivos.Ventilador import \
    Ventilador


def main():
    # instanciando meus dispositivos
    lampada = Lampada()
    ventilador = Ventilador()
    camera = Camera()

    # Ligando minha lampada pelo Controle Remoto
    controle_lampada = ControleRemoto(lampada)
    controle_lampada.ativar()
    print("\n")
    # Ligando meu ventilador pelo App
    controle_ventilador = AplicativoMovel(ventilador)
    controle_ventilador.ativar()
    print("\n")
    # Ligando minha camera pelo Painel de Controle
    controle_camera = PainelControle(camera)
    controle_camera.ativar()
    print("\n")


if __name__ == "__main__":
    main()
