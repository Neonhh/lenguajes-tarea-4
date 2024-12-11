import pytest
from funciones import clase_no_hereda, clase_hereda, describir, clasesDefinidas, existe

def setup_module(module):
    # Configuración inicial antes de las pruebas
    clasesDefinidas.clear()

def test_clase_hereda():
    clase_no_hereda('ClaseA', ['metodo1', 'metodo2'])
    assert 'ClaseA' in clasesDefinidas
    assert clasesDefinidas['ClaseA'].metodos == ['metodo1', 'metodo2']

    clase_hereda('ClaseB', 'ClaseA', ['metodo3'])
    assert 'ClaseB' in clasesDefinidas
    assert clasesDefinidas['ClaseB'].superclase == 'ClaseA'

def test_describir(capsys):
    clase_no_hereda('ClaseC', ['metodo1', 'metodo2'])
    describir('ClaseC')
    captured = capsys.readouterr()
    assert "metodo1 -> ClaseC :: metodo1" in captured.out
    assert "metodo2 -> ClaseC :: metodo2" in captured.out

def test_existe():
    clase_no_hereda('ClaseD', ['metodo1', 'metodo2'])
    assert existe('ClaseA') == True
    assert existe('ClaseD') == True
    assert existe('ClaseE') == False

def test_ciclo_herencia(capsys):
    clase_no_hereda('ClaseF', ['metodo1', 'metodo2'])
    clase_hereda('ClaseG', 'ClaseF', ['metodo3'])
    clase_hereda('ClaseH', 'ClaseG', ['metodo4'])
    clase_hereda('ClaseF', 'ClaseH', ['metodo5'])
    captured = capsys.readouterr()
    assert "Error: La clase ClaseF ya existe" in captured.out

def test_describir_herencia(capsys):
    describir('ClaseH')
    captured = capsys.readouterr()
    assert "metodo1 -> ClaseF :: metodo1" in captured.out
    assert "metodo2 -> ClaseF :: metodo2" in captured.out
    assert "metodo3 -> ClaseG :: metodo3" in captured.out
    assert "metodo4 -> ClaseH :: metodo4" in captured.out
    assert not "metodo5 -> ClaseF :: metodo5" in captured.out
    assert not "metodo1 -> ClaseG :: metodo1" in captured.out
    assert not "metodo3 -> ClaseH :: metodo3" in captured.out