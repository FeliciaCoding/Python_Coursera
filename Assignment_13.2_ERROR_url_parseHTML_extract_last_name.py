import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Read URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
url = input('Enter URL:')
count = input('Enter count:')
position = input('Enter position:')
#posi = int(position)

html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html,'html.parser')

links = list()
counts = 0
tags = soup('a')
for tag in tags:
    #print(tag.get('href', None))
# >>http://py4e-data.dr-chuck.net/known_by_Aniqa.html
#   http://py4e-data.dr-chuck.net/known_by_Ogheneruno.html
#   http://py4e-data.dr-chuck.net/known_by_Owain.html
    counts = counts + 1
    if counts < count
    hrefs = tag.get('href', None)
    links.append(hrefs)

# print(links)
#>> ['http://py4e-data.dr-chuck.net/known_by_Aniqa.html', 'http://py4e-data.dr-chuck.net/known_by_Ogheneruno.html', 'http://py4e-data.dr-chuck.net/known_by_Montgomery.html', 'http://py4e-data.dr-chuck.net/known_by_Owain.html', 'http://py4e-data.dr-chuck.net/known_by_Haniyah.html', 'http://py4e-data.dr-chuck.net/known_by_Anona.html', 'http://py4e-data.dr-chuck.net/known_by_Edyn.html', 'http://py4e-data.dr-chuck.net/known_by_Dallace.html', 'http://py4e-data.dr-chuck.net/known_by_Zoe.html', 'http://py4e-data.dr-chuck.net/known_by_Kiarash.html', 'http://py4e-data.dr-chuck.net/known_by_Tracy.html', 'http://py4e-data.dr-chuck.net/known_by_Carmyle.html', 'http://py4e-data.dr-chuck.net/known_by_Zahraa.html', 'http://py4e-data.dr-chuck.net/known_by_Alanys.html', 'http://py4e-data.dr-chuck.net/known_by_Airidas.html', 'http://py4e-data.dr-chuck.net/known_by_Melisa.html', 'http://py4e-data.dr-chuck.net/known_by_Vivian.html', 'http://py4e-data.dr-chuck.net/known_by_Margaret.html', 'http://py4e-data.dr-chuck.net/known_by_Hajra.html', 'http://py4e-data.dr-chuck.net/known_by_Ajooni.html', 'http://py4e-data.dr-chuck.net/known_by_Alexanne.html', 'http://py4e-data.dr-chuck.net/known_by_Sudais.html', 'http://py4e-data.dr-chuck.net/known_by_Seb.html', 'http://py4e-data.dr-chuck.net/known_by_Christin.html', 'http://py4e-data.dr-chuck.net/known_by_Jaimie.html', 'http://py4e-data.dr-chuck.net/known_by_Jennah.html', 'http://py4e-data.dr-chuck.net/known_by_Landon.html', 'http://py4e-data.dr-chuck.net/known_by_Mea.html', 'http://py4e-data.dr-chuck.net/known_by_Cacie.html', 'http://py4e-data.dr-chuck.net/known_by_Colton.html', 'http://py4e-data.dr-chuck.net/known_by_Mitchel.html', 'http://py4e-data.dr-chuck.net/known_by_Chintu.html', 'http://py4e-data.dr-chuck.net/known_by_Hyden.html', 'http://py4e-data.dr-chuck.net/known_by_Chrystal.html', 'http://py4e-data.dr-chuck.net/known_by_Lincon.html', 'http://py4e-data.dr-chuck.net/known_by_Jaden.html', 'http://py4e-data.dr-chuck.net/known_by_Roma.html', 'http://py4e-data.dr-chuck.net/known_by_Manolo.html', 'http://py4e-data.dr-chuck.net/known_by_Clio.html', 'http://py4e-data.dr-chuck.net/known_by_Teos.html', 'http://py4e-data.dr-chuck.net/known_by_Rihonn.html', 'http://py4e-data.dr-chuck.net/known_by_Griffin.html', 'http://py4e-data.dr-chuck.net/known_by_Conley.html', 'http://py4e-data.dr-chuck.net/known_by_Xiao.html', 'http://py4e-data.dr-chuck.net/known_by_Dhyia.html', 'http://py4e-data.dr-chuck.net/known_by_Manahil.html', 'http://py4e-data.dr-chuck.net/known_by_Diona.html', 'http://py4e-data.dr-chuck.net/known_by_Dharam.html', 'http://py4e-data.dr-chuck.net/known_by_Danielle.html', 'http://py4e-data.dr-chuck.net/known_by_Rori.html', 'http://py4e-data.dr-chuck.net/known_by_Lang.html', 'http://py4e-data.dr-chuck.net/known_by_Sabila.html', 'http://py4e-data.dr-chuck.net/known_by_Zoha.html', 'http://py4e-data.dr-chuck.net/known_by_Jemma.html', 'http://py4e-data.dr-chuck.net/known_by_Silvana.html', 'http://py4e-data.dr-chuck.net/known_by_Asal.html', 'http://py4e-data.dr-chuck.net/known_by_Dillon.html', 'http://py4e-data.dr-chuck.net/known_by_CJ.html', 'http://py4e-data.dr-chuck.net/known_by_Joanna.html', 'http://py4e-data.dr-chuck.net/known_by_Atal.html', 'http://py4e-data.dr-chuck.net/known_by_Callun.html', 'http://py4e-data.dr-chuck.net/known_by_Anubhav.html', 'http://py4e-data.dr-chuck.net/known_by_Coray.html', 'http://py4e-data.dr-chuck.net/known_by_Graeme.html', 'http://py4e-data.dr-chuck.net/known_by_Chrissie.html', 'http://py4e-data.dr-chuck.net/known_by_Ayub.html', 'http://py4e-data.dr-chuck.net/known_by_Heather.html', 'http://py4e-data.dr-chuck.net/known_by_Katie.html', 'http://py4e-data.dr-chuck.net/known_by_Inaara.html', 'http://py4e-data.dr-chuck.net/known_by_Siddhant.html', 'http://py4e-data.dr-chuck.net/known_by_Salymat.html', 'http://py4e-data.dr-chuck.net/known_by_Shahd.html', 'http://py4e-data.dr-chuck.net/known_by_Anaya.html', 'http://py4e-data.dr-chuck.net/known_by_Kevaugh.html', 'http://py4e-data.dr-chuck.net/known_by_Thumbiko.html', 'http://py4e-data.dr-chuck.net/known_by_Xida.html', 'http://py4e-data.dr-chuck.net/known_by_Alaska.html', 'http://py4e-data.dr-chuck.net/known_by_Shonagh.html', 'http://py4e-data.dr-chuck.net/known_by_Kaiya.html', 'http://py4e-data.dr-chuck.net/known_by_Khadija.html', 'http://py4e-data.dr-chuck.net/known_by_Kieron.html', 'http://py4e-data.dr-chuck.net/known_by_Filip.html', 'http://py4e-data.dr-chuck.net/known_by_Dorothy.html', 'http://py4e-data.dr-chuck.net/known_by_Kallan.html', 'http://py4e-data.dr-chuck.net/known_by_Mena.html', 'http://py4e-data.dr-chuck.net/known_by_Abbie.html', 'http://py4e-data.dr-chuck.net/known_by_Amyleigh.html', 'http://py4e-data.dr-chuck.net/known_by_Annalise.html', 'http://py4e-data.dr-chuck.net/known_by_Carrich.html', 'http://py4e-data.dr-chuck.net/known_by_Rachel.html', 'http://py4e-data.dr-chuck.net/known_by_Etinosa.html', 'http://py4e-data.dr-chuck.net/known_by_Amie.html', 'http://py4e-data.dr-chuck.net/known_by_Lisa.html', 'http://py4e-data.dr-chuck.net/known_by_Liv.html', 'http://py4e-data.dr-chuck.net/known_by_Baylie.html', 'http://py4e-data.dr-chuck.net/known_by_Jubin.html', 'http://py4e-data.dr-chuck.net/known_by_Kacie.html', 'http://py4e-data.dr-chuck.net/known_by_Falyn.html', 'http://py4e-data.dr-chuck.net/known_by_Conli.html', 'http://py4e-data.dr-chuck.net/known_by_Cohen.html']
    counts = 0
    for link in links:
        link = links[posi]
        html = urllib.request.urlopen(link, context = ctx).read()

        counts = counts + 1

        if counts < count:
            continue
        break
print(links[position])
