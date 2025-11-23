from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.FacadeCinemaOnline.Facade.CinemaFacade import \
    CinemaFacade


def main():
    user_dudasss = CinemaFacade()
    user_rafa = CinemaFacade()
    print(f"{'-' * 30}")
    user_dudasss.assistir_filme(
        usuario="Dudass",
        valor=25.00,
        filme="Star Wars: Episódio I - A Ameaça Fantasma 1999"
    )
    print(f"{'-'*30}")
    user_dudasss.assistir_filme(
        usuario="Dudass",
        valor=25.00,
        filme="Star Wars: The Clone Wars 2008"
    )
    print(f"{'-' * 30}")
    user_rafa.assistir_filme(
        usuario="Rafa",
        valor=18.00,
        filme="Capitão América: O Primeiro Vingador "
    )
    print(f"{'-' * 30}")


if __name__ == '__main__':
    main()
