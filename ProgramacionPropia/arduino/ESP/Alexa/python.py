for i in range(1, 255):
    por = i/255
    if por > 0 and por < 0.1:
        print("0",por)
    elif por >= 0.1 and por < 0.2:
        print("1",por)
    elif por >= 0.2 and por < 0.3:
        print("2",por)
    elif por >= 0.3 and por < 0.4:
        print("3",por)
    elif por >= 0.4 and por < 0.5:
        print("4",por)
    elif por >= 0.5 and por < 0.6:
        print("5",por)
    elif por >= 0.6 and por < 0.7:
        print("6",por)
    elif por >= 0.7 and por < 0.8:
        print("7",por)
    elif por >= 0.8 and por < 0.9:
        print("8",por)
    elif por >= 0.9 and por < 1:
        print("9",por)
    else:
        print("Apagado")