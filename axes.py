def axes():
    axes:int=int(input('\nquantos eixos o caminhão tem?\n1 para 5 eixos (uma vagão)\n2 para 7 eixos (dois vagões)\n3 para 9 eixos (dois vagões)\n'))

    match(axes):
        case 1:
            # um vagão
            stop=False
            return 41100

        case 2:
            # dois vagões
            stop=False
            return 57000

        case 3:
            # dois vagões
            stop=False
            return 74000

        case _:
            # erro
            stop=True
            print('\nação não valida\n')
            while stop is True:
                axes()
