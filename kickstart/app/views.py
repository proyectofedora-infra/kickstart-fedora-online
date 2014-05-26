from flask import render_template, flash, redirect, request
from app import app
from form import liveForm 
# es para probar que le puse index2, despues hay que acomodarlo bien
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = liveForm()
    print "se apreto submit"
    print form.time_zone.data
    print form.select_locale.data
    print form.select_kyemap.data
    # el problema que habia era con los selectfield.
    # no se validan porque son todos utf8.
    # de todas formas no creo necesitar un form.validate
    #~ if form.validate_on_submit():
    print "estoy validando"
    chk=[]
    for value in form.check:
        value_chk = request.form.get(value[0])
        print value_chk
        if value_chk <> None:
            chk.append(value_chk)

    X= request.form.get("X")
    print X
    print "#######",chk
    return render_template("index.html",form = form)
