import math

h_min_ch = int(input("Informe a hora da entrada(0-23h): "))

if 0 <= h_min_ch <= 23:
    min_ch = int(input("Informe os minutos no momento da entrada(0-60): "))

    if 0 <= min_ch <= 59:
        print("---------------------------------------------")
        print(f"Horário de Chegada: {h_min_ch}h:{min_ch}")
        print("---------------------------------------------")
        hora_chegada = h_min_ch * 60 + min_ch
        h_min_part = int(input("Informe a hora da partida(0-23h): "))

        if 0 <= h_min_part <= 23:
            min_part = int(input("Informe os minutos no momento da partida(0-60): "))

            if 0 <= min_part <= 59:
                print("---------------------------------------------")
                print(f"Horário de Partida: {h_min_part}h:{min_part}")
                print("---------------------------------------------")
                hora_partida = h_min_part * 60 + min_part

                if hora_partida > hora_chegada:
                    hora_pagmt = (hora_partida - hora_chegada)
                    h = hora_pagmt // 60
                    min = hora_pagmt % 60

                    if 0 <= hora_pagmt < 60:
                        x = 1
                        print(f"""
                        Tempo de permanência: {h}h:{min} min 
                        Total R$ {x}
                        """)

                    elif 60 <= hora_pagmt < 120:
                        x = 2
                        print(f"""
                            Tempo de permanência: {h}h:{min} min 
                            Total R$ {x}
                            """)
                    elif 120 <= hora_pagmt < 180:
                        x = 3.4
                        print(f"""
                            Tempo de permanência: {h}h:{min} min 
                            Total R$ {x}
                            """)
                    elif 180 <= hora_pagmt < 240:
                        x = 4.8
                        print(f"""
                            Tempo de permanência: {h}h:{min} min 
                            Total R$ {x}
                            """)
                    elif 240 <= hora_pagmt < 300:
                        x = 6.8
                        print(f"""
                            Tempo de permanência: {h}h:{min} min 
                            Total R$ {x}
                            """)
                    elif hora_pagmt >= 300:
                        x = 6.8 + ((math.ceil(min / 60) + h) - 5) * 2
                        print(f"""
                            Tempo de permanência: {h}h:{min} min 
                            Total R$ {x}
                            """)
                    else:
                        print("Valor Inválido")

                else:
                    hora_pagmt = (1440 - hora_chegada) + hora_partida
                    h = hora_pagmt // 60
                    min = hora_pagmt % 60
                    print(f"{h}h:{min} min ")
                    print(f"Quantidade de minutos : {hora_pagmt}")
            else:
                print("Valor Inválido")
        else:
            print("Valor Inválido")
    else:
        print("Valor Inválido")
else:
    print("Valor Inválido")
