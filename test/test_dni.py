import pytest
from src.dni import Dni
from test.lista_test_dni import lista_dni

@pytest.mark.parametrize("dni", lista_dni)
def test_get_numero(dni):

    assert Dni(dni).get_numero() == int(dni[:-1])

def test_get_letra(dni):

    assert Dni(dni).get_letra() == str(dni[-1])

def test_asignar_letra():
    
    assert Dni('39489829').asignar_letra() == '39489829W'
    assert Dni('39468391').asignar_letra() == '39468391T'
    assert Dni('54659645').asignar_letra() == '54659645F'
    assert Dni('44104739').asignar_letra() == '44104739P'
    assert Dni('77545629').asignar_letra() == '77545629W'
    assert Dni('17463021').asignar_letra() == '17463021H'
    assert Dni('77422360').asignar_letra() == '77422360J'
    assert Dni('35658562').asignar_letra() == '35658562Y'
    assert Dni('39498277').asignar_letra() == '39498277D'
    assert Dni('39494177').asignar_letra() == '39494177A'
    assert Dni('53820151').asignar_letra() == '53820151J'
    assert Dni('53975865').asignar_letra() == '53975865V'
    assert Dni('35638220').asignar_letra() == '35638220L'
    assert Dni('39496803').asignar_letra() == '39496803F'
    assert Dni('39465565').asignar_letra() == '39465565A'
    assert Dni('35639739').asignar_letra() == '35639739C'
    assert Dni('39492958').asignar_letra() == '39492958A'
    assert Dni('53973018').asignar_letra() == '53973018E'
    assert Dni('17463502').asignar_letra() == '17463502Q'
    assert Dni('39515907').asignar_letra() == '39515907K'
    assert Dni('53975775').asignar_letra() == '53975775L'
    assert Dni('17463400').asignar_letra() == '17463400Y'
    assert Dni('39462352').asignar_letra() == '39462352X'
    assert Dni('35674062').asignar_letra() == '35674062G'
    assert Dni('39512621').asignar_letra() == '39512621R'
    assert Dni('39491701').asignar_letra() == '39491701B'
    assert Dni('15491178').asignar_letra() == '15491178B'
    assert Dni('53192906').asignar_letra() == '53192906R'
    assert Dni('54471408').asignar_letra() == '54471408W'
    assert Dni('53975712').asignar_letra() == '53975712W'

def test_comprobar_letra(): #TRWAGMYFPDXBNJZSQVHLCKE
    assert Dni('39468391T').comprobar_letra() == True
    assert Dni('53192906R').comprobar_letra() == True
    assert Dni('39489829W').comprobar_letra() == True
    assert Dni('39494177A').comprobar_letra() == True
    assert Dni('35674062G').comprobar_letra() == True
    assert Dni('12345669M').comprobar_letra() == True
    assert Dni('17463400Y').comprobar_letra() == True
    assert Dni('54659645F').comprobar_letra() == True
    assert Dni('44104739P').comprobar_letra() == True
    assert Dni('39498277D').comprobar_letra() == True
    assert Dni('39462352X').comprobar_letra() == True
    assert Dni('15491178B').comprobar_letra() == True
    assert Dni('12345676N').comprobar_letra() == True
    assert Dni('77422360J').comprobar_letra() == True
    assert Dni('12345678Z').comprobar_letra() == True
    assert Dni('12345679S').comprobar_letra() == True
    assert Dni('17463502Q').comprobar_letra() == True
    assert Dni('53975865V').comprobar_letra() == True
    assert Dni('17463021H').comprobar_letra() == True
    assert Dni('35638220L').comprobar_letra() == True
    assert Dni('35639739C').comprobar_letra() == True
    assert Dni('39137695K').comprobar_letra() == True
    assert Dni('53973018E').comprobar_letra() == True
    

    assert Dni('39489829T').comprobar_letra() == False
    assert Dni('39137695R').comprobar_letra() == False
    assert Dni('54659645W').comprobar_letra() == False
    assert Dni('44104739A').comprobar_letra() == False
    assert Dni('77545629G').comprobar_letra() == False
    assert Dni('17463021M').comprobar_letra() == False
    assert Dni('77422360Y').comprobar_letra() == False
    assert Dni('39498277F').comprobar_letra() == False
    assert Dni('39494177P').comprobar_letra() == False
    assert Dni('53820151D').comprobar_letra() == False
    assert Dni('53975865X').comprobar_letra() == False
    assert Dni('35638220B').comprobar_letra() == False
    assert Dni('39496803N').comprobar_letra() == False
    assert Dni('39465565J').comprobar_letra() == False
    assert Dni('35639739Z').comprobar_letra() == False
    assert Dni('39492958S').comprobar_letra() == False
    assert Dni('53973018Q').comprobar_letra() == False
    assert Dni('17463502V').comprobar_letra() == False
    assert Dni('39515907H').comprobar_letra() == False
    assert Dni('17463400L').comprobar_letra() == False
    assert Dni('39462352C').comprobar_letra() == False
    assert Dni('35674062K').comprobar_letra() == False
    assert Dni('39512621E').comprobar_letra() == False


def test_creacion_dni():
    creacion_dni = Dni().creacion_dni()
    assert len(creacion_dni) == 9

