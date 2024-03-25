def recup_info(seismes):
    return seismes["mag"], seismes["geometry"].x,seismes["geometry"].y


def recup_date():
    date_1 = input("Entrez la date de départ (format = aaaa-mm-jj): ")
    date_2 = input("Entrez la date de fin (format = aaaa-mm-jj): ")
    if len(date_1) != 10 or type(date_1) != str or date_1[4] != '-' or date_1[7] != '-' :
        raise NameError('Wrong format, try again')
    elif len(date_2) != 10 or type(date_2) != str or date_2[4] != '-' or date_2[7] != '-' :
        raise NameError('Wrong format, try again')
    return (str(date_1), str(date_2))

def recup_mag():
    mag = int(input("Entrez la magnitude minimum des seismes affichés (entre 0 et 9 compris): "))
    if type(mag) != int or mag > 9 or mag < 0 :
        raise NameError('Wrong format, try again')
    return str(mag)
