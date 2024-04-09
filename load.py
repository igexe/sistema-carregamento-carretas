from axes import axes as ax

def load():
    peso_lona:float=0
    peso_max:float=ax()
    peso_caminhao:float=float(input('\ndigite o peso do caminhão\n'))

    if int(input('\nas carretas serão carregadas com lona?\n1 para sim\n2 para não\n'))==1:
        peso_lona=float(input('\ndigite o peso da lona\n'))

    if peso_max>41100:
        peso_max-=((peso_lona*2)+peso_caminhao)
        print('\ncada vagão sera carregado com: '+str(peso_max/2))
        return 0
    
    peso_max-=(peso_lona+peso_caminhao)
    print('\no vagão sera carregado com: '+str(peso_max))
