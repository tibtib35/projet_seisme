def recup_info(seismes):
    return seismes["mag"], seismes["geometry"].x,seismes["geometry"].y


def recup_date():
    date_1 = input("Entrez la date de départ (format = an-m-j):")
    date_2 = input("Entrez la date de fin (format = an-m-j): ")
    return (str(date_1), str(date_2))
