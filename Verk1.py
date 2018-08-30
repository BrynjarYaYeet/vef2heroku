#from bottle import route, run
from sys import argv
import bottle
from bottle import *


@route('/')
def index():
    return """
    <h2>Verkefni 1</h2>
    <p><a href="/simi">Bull#1</a></p>
    <p><a href="/99">Bull#2</a></p>
    <p><a href="/svalt">Bull#3</a></p>
    """
@route("/simi")
def jolli():
    return "Þurfti að svara símanum og leyfa ÖLLUM bekknum að heyra – Kennarinn bjóst ekki við þessu! – MYNDBAND"

@route("/99")
def jolli():
    return "99% geta EKKI séð númerið á myndinni – Skiljanlegt miðað við hvernig það er falið!"

@route("/svalt")
def jolli():
    return "Þetta fólk kann að gera SVALAN desktop – Svona á aðkoman að tölvunni að vera! – MYNDIR"




#run(host='localhost', port=8010)

run(host='0.0.0.0', port=argv[1])
