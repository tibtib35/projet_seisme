import map_creation as mp
import get_info as gi
import draw_circle as dc

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
    contenu.insert(position, nouveau_code_html)
    with open(nom_fichier, 'w') as fichier:
        fichier.write(''.join(contenu))

nouveau_code = """
<div class='btn'>
    <button> lol <button\>
</div>
"""

inserer_code_html('map.html', nouveau_code, 40)
css_code = """
                .btn{background-color:rgb(115, 205, 228);width:100%}
"""
inserer_code_html('map.html', css_code, 35)
