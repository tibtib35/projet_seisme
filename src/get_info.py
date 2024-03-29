def recup_info(seismes):
    '''
    Prend en paramètres des séismes et renvoie leur magnitude, latitude et longitude.
    '''
    return seismes["mag"], seismes["geometry"].x,seismes["geometry"].y


def recup_date():
    '''
    Renvoie des inputs permettant au client de rentrer la date de début et de fin des séismes
    '''
    date_1 = input("Entrez la date de départ (format = aaaa-mm-jj): ") #input qui demande la date de début
    date_2 = input("Entrez la date de fin (format = aaaa-mm-jj): ") #input qui demande la date de fin
    if len(date_1) != 10 or type(date_1) != str or date_1[4] != '-' or date_1[7] != '-' : # permet de controler le format de la réponse du client 
        raise NameError('Wrong format, try again')
    elif len(date_2) != 10 or type(date_2) != str or date_2[4] != '-' or date_2[7] != '-' : # permet de controler le format de la réponse du client 
        raise NameError('Wrong format, try again')
    return (str(date_1), str(date_2))

def recup_mag():
    '''
    Renvoie des inputs permettant au client de rentrer la magnitude minimum des séismes affichés
    '''
    mag = int(input("Entrez la magnitude minimum des seismes affichés (entre 0 et 9 compris): ")) #input qui demande la magnitude minimum des séismes affichés
    if type(mag) != int or mag > 9 or mag < 0 : # permet de controler le format de la réponse du client 
        raise NameError('Wrong format, try again')
    return str(mag)
