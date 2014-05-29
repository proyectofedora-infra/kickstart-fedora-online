from flask import render_template, flash, redirect, request
from app import app
from form import ksForm
from KSP import KSP

KSparser=KSP()

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = ksForm()
    if form.is_submitted():
        value_chk = request.form.get("sig")    
        if value_chk=="True":
            return redirect('/config')
    return render_template("index.html",form = form)


@app.route('/config', methods = ['GET', 'POST'])
def config():
    form = ksForm()
    if form.is_submitted():
        print form.time_zone.data
        print form.select_locale.data
        print form.select_kyemap.data
        value_chk = request.form.get("sig") 
        value_chk_atr = request.form.get("atr")    
        if value_chk_atr=="True":
            return redirect('/')
        if value_chk=="True":
            return redirect('/grouplist')

    return render_template("config.html",form = form)


@app.route('/grouplist', methods = ['GET', 'POST'])
def grouplist():
    form = ksForm()
    if form.is_submitted():
        value_chk_atr = request.form.get("atr")    
        value_chk_gen = request.form.get("gen")    
        if value_chk_atr=="True":
            return redirect('/config')
        if value_chk_gen=="True":
            a=0
            chk=[]
            for value in form.check:
                value_chk = request.form.get(value[0])
                if value_chk <> None:
                    form.chk_res[value_chk]=True
            for v in form.chk_res.keys():
                if form.chk_res[v]==True:
                    KSparser.add_pkg(v)
            KSparser.print_screen()
    return render_template("grouplist.html",form = form)

