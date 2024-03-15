import map_creation as mp
import get_info as gi
import draw_circle as dc
import aspose.words as aw

map = mp.create(48.1333,  -1.9667)


seismes = mp.seismes

info = gi.recup_info(seismes)

magnitude = info[0]
latitude = info[1]
longitude = info[2]

dc.circle(magnitude,latitude,longitude,map)



map.save("map.html")
def inserer_code_html(nom_fichier, nouveau_code_html, position):
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.readlines()

    # Insérer le nouveau code HTML à la position spécifiée
    contenu.insert(position, nouveau_code_html)

    with open(nom_fichier, 'w') as fichier:
        fichier.write(''.join(contenu))


# Code HTML à insérer
nouveau_code = """
<div class='btn'>
    <button> lol <button\>
</div>
"""

# Position où insérer le nouveau code HTML (lignes numérotées à partir de 0)

# Insérer le nouveau code HTML au fichier existant à la position spécifiée
inserer_code_html('map.html', nouveau_code, 40)
css_code = """
                .btn{background-color:rgb(115, 205, 228);width:100%}
"""
inserer_code_html('map.html', css_code, 35)
