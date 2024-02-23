def recup_info(seisme_info):
    co = []
    for i in range (len(seisme["geometry"])):
        co.append((seisme[i].x,seisme[i].y))
    return co
