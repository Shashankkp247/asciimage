import project as proj
import pytest
from os.path import exists
import os

class Idk:
    img = 'test.jpg'

def test_parsr():
    args, pars = proj.parsr()
    assert args.img == False

def test_arg_check():
    hia = Idk
    assert proj.arg_check(hia) == True
    hia.img = 'fscoiety.dat'
    assert proj.arg_check(hia) == False

def test_text():
    tstxt = Idk
    #Success test
    txt, booln = proj.text('idk.jpg')
    assert booln == True
    assert txt == 'idk.txt'
    
    #Fail test
    ftxt, fbool = proj.text('fsociety.dat')
    assert fbool == False
    assert ftxt == None

def test_converter():
    proj.converter('idk.jpg', 'MEDIUM', 'idk.txt')
    file_exists = exists('idk.txt')
    assert file_exists == False

    proj.converter('naruto.jpg', 'MEDIUM', 'naruto.txt')
    cwd = os.getcwd()
    file_exists = exists(f"{cwd}/test")
    assert file_exists == True