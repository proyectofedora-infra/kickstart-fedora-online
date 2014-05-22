from flask import render_template, flash, redirect, request
from app import app
from form import liveForm 
# es para probar que le puse index2, despues hay que acomodarlo bien
@app.route('/index2', methods = ['GET', 'POST'])
def index():
    form = liveForm()
    # creo que el problema esta en el validate
    if form.validate_on_submit():
        chk=[]
        # no esta andando el request. antes si andaba, no se que toque en el tml o aca
        for value in form.check:
            value_chk = request.form.get(value[0])
            if value_chk <> None:
                chk.append(value_chk)

        X= request.form.get("X")
        print X
        print "#######",chk
    return render_template("index2.html",form = form)
