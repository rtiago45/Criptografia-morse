MORSE_DICIONARIO = { ' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}


def Txt_to_Morse():
    txt = input('Escreva o texto a ser convertido para Morse: ')
    codigo = [MORSE_DICIONARIO[i.upper()] + ' ' for i in txt if i.upper() in MORSE_DICIONARIO.keys()]
    morse=''.join(codigo)
    print(morse)


def Morse_to_Txt():
    txt = input('Digite em Morse para ser convertido para texto: ')
    codigo = [k for i in txt.split() for k,v in MORSE_DICIONARIO.items() if i==v]
    novotxt =''.join(codigo)
    print(novotxt)


print('''\n1 - Converter texto para morse \n2 - Converter Morse para texto\n3 - Sair\n ''')

while True:
    try:
        selecionar = int(input('Faça sua escolha: '))
        if selecionar == 1:
            print(Txt_to_Morse())
            break
        elif selecionar == 2:
            print(Morse_to_Txt())
            break
        elif selecionar == 3:
            print('Saindo')
            break
        else:
            print('Escolha errada, tente novamente')
    except:
        print('TESTE ANA !')