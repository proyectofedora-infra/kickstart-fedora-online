from flask import render_template, flash, redirect, request
from app import app
from form import liveForm 
# es para probar que le puse index2, despues hay que acomodarlo bien]
@app.route('/index', methods = ['GET', 'POST'])

def index():
    a=0
    chk=[]
    form = liveForm()
    print form.time_zone.data
    print form.select_locale.data
    print form.select_kyemap.data
    # el problema que habia era con los selectfield.
    # no se validan porque son todos utf8.
    # de todas formas no creo necesitar un form.validate
    #~ if form.validate_on_submit():

    # otro problema es que las variales se no se borran con 
    # cada llamada a la funcion, se mantinen como instancias separadas

    # lo que hago ahora es guardar los resultados en un diccionario
    # y despues iterar sobre el diccionario y cambiar su valor None por
    # True en funcion del request.form.get(value[0])
    # de esa forma no tengo problemas de valores repetidos
    
    # itero sobre los checkbox
    for value in form.check:
        value_chk = request.form.get(value[0])
        if value_chk <> None:
            # cambio el valor None del dicc
            form.chk_res[value_chk]=True
    for v in form.chk_res.keys():
        if form.chk_res[v]==True:
            print v
    return render_template("index.html",form = form)
