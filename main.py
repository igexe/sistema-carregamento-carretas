from load import load

while True:
    action:int=int(input('\n1 para carrgar um caminhão\n0 para parar o programa\n'))

    match(action):
        case 0:
            print('\nadeus\n')
            break

        case 1:
            load()

        case _:
            print('\nação desconhecida por favor escolha uma das seguintes opções\n')
