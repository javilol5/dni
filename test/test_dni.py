import pytest
from src.dni import Dni


def test_get_numero():

    assert Dni('39489829W').get_numero() == 39489829
    assert Dni('39468391T').get_numero() == 39468391
    assert Dni('54659645F').get_numero() == 54659645
    assert Dni('44104739P').get_numero() == 44104739
    assert Dni('77545629W').get_numero() == 77545629
    assert Dni('17463021H').get_numero() == 17463021
    assert Dni('77422360J').get_numero() == 77422360
    assert Dni('35658562Y').get_numero() == 35658562
    assert Dni('39498277D').get_numero() == 39498277
    assert Dni('39494177A').get_numero() == 39494177
    assert Dni('53820151J').get_numero() == 53820151
    assert Dni('53975865V').get_numero() == 53975865
    assert Dni('35638220L').get_numero() == 35638220
    assert Dni('39496803F').get_numero() == 39496803
    assert Dni('39465565A').get_numero() == 39465565
    assert Dni('35639739C').get_numero() == 35639739
    assert Dni('39492958A').get_numero() == 39492958
    assert Dni('53973018E').get_numero() == 53973018
    assert Dni('17463502Q').get_numero() == 17463502
    assert Dni('39515907K').get_numero() == 39515907
    assert Dni('53975775L').get_numero() == 53975775
    assert Dni('17463400Y').get_numero() == 17463400
    assert Dni('39462352X').get_numero() == 39462352
    assert Dni('35674062G').get_numero() == 35674062
    assert Dni('39512621R').get_numero() == 39512621
    assert Dni('39491701B').get_numero() == 39491701
    assert Dni('15491178B').get_numero() == 15491178
    assert Dni('53192906R').get_numero() == 53192906
    assert Dni('54471408W').get_numero() == 54471408
    assert Dni('53975712W').get_numero() == 53975712

def test_get_letra():

    assert Dni('39489829W').get_letra() == 'W'
    assert Dni('39468391T').get_letra() == 'T'
    assert Dni('54659645F').get_letra() == 'F'
    assert Dni('44104739P').get_letra() == 'P'
    assert Dni('77545629W').get_letra() == 'W'
    assert Dni('17463021H').get_letra() == 'H'
    assert Dni('77422360J').get_letra() == 'J'
    assert Dni('35658562Y').get_letra() == 'Y'
    assert Dni('39498277D').get_letra() == 'D'
    assert Dni('39494177A').get_letra() == 'A'
    assert Dni('53820151J').get_letra() == 'J'
    assert Dni('53975865V').get_letra() == 'V'
    assert Dni('35638220L').get_letra() == 'L'
    assert Dni('39496803F').get_letra() == 'F'
    assert Dni('39465565A').get_letra() == 'A'
    assert Dni('35639739C').get_letra() == 'C'
    assert Dni('39492958A').get_letra() == 'A'
    assert Dni('53973018E').get_letra() == 'E'
    assert Dni('17463502Q').get_letra() == 'Q'
    assert Dni('39515907K').get_letra() == 'K'
    assert Dni('53975775L').get_letra() == 'L'
    assert Dni('17463400Y').get_letra() == 'Y'
    assert Dni('39462352X').get_letra() == 'X'
    assert Dni('35674062G').get_letra() == 'G'
    assert Dni('39512621R').get_letra() == 'R'
    assert Dni('39491701B').get_letra() == 'B'
    assert Dni('15491178B').get_letra() == 'B'
    assert Dni('53192906R').get_letra() == 'R'
    assert Dni('54471408W').get_letra() == 'W'
    assert Dni('53975712W').get_letra() == 'W'

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

