def recup_info(seisme_info):
    co = []
    for i in range (len(seisme["coordinates"])):
        co.append((seisme[i][0],seisme[i][1]))
    return co
