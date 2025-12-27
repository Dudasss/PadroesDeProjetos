from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Classes.ControleRemoto import ControleRemoto
from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Classes.DesligarLuz import DesligarLuz
from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Classes.LigarLuz import LigarLuz
from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Classes.LigarVentilador import LigarVentilador
from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Classes.Luz import Luz
from PadroesDeProjetos.AT8_State_Command_Observer.SistemaControleRemoto.Classes.Ventilador import Ventilador


def SistemaControleRemoto():
    # Instanciando os Receptores
    sala_luz = Luz()
    teto_ventilador = Ventilador()

    # Criando os Comandos Concretos
    luz_on = LigarLuz(sala_luz)
    luz_off = DesligarLuz(sala_luz)
    vent_on = LigarVentilador(teto_ventilador)

    # Instanciando o controle remoto (invoker)
    controle = ControleRemoto()

    print("--- Executando Comandos ---")
    controle.executar_comando(luz_on)  # Luz ligado
    controle.executar_comando(vent_on)  # Ventilador ligado
    controle.executar_comando(luz_off)  # Luz desligado

    print("\n--- Desfazendo Ações (Undo) ---")
    controle.desfazer_ultimo_comando()  # Reverte Luz off -> Luz ligado
    controle.desfazer_ultimo_comando()  # Reverte Vent on -> Ventilador desligado


if __name__ == "__main__":
    SistemaControleRemoto()
