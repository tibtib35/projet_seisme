def recup_info(seisme_info):
    co = []
    for i in range (len(seisme["geometry"])):
        co.append((seisme["geometry"].x,seisme["geometry"].y))
    return co
