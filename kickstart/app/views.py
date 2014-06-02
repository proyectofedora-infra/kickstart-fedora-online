from flask import render_template, flash, redirect, request, url_for, session
from app import app
from form import ksForm
from KSP import KSP

KSparser = KSP()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ksForm()
    form_action = url_for('index')
    if request.method == 'POST' and form.validate_on_submit():
        session['desktop_env'] = request.form['X']
        KSparser.load(session['desktop_env'])
        return redirect(url_for('config'))
    return render_template("index.html", form_action=form_action,form=form)


@app.route('/config', methods=['GET', 'POST'])
def config():
    form = ksForm()
    form_action = url_for('config')
    if request.method == 'POST' and form.validate_on_submit():
        session['time_zone'] = form.time_zone.data
        session['select_locale'] = form.select_locale.data
        session['select_keymap'] = form.select_kyemap.data
        print form.time_zone.data
        print form.select_locale.data
        print form.select_kyemap.data
        return redirect(url_for('grouplist'))
    return render_template("config.html", form_action=form_action, form=form)


@app.route('/grouplist', methods=['GET', 'POST'])
def grouplist():
    form = ksForm()
    if form.is_submitted():
        value_chk_atr = request.form.get("atr")    
        value_chk_gen = request.form.get("gen")    
        if value_chk_atr is "True":
            return redirect(url_for('config'))
        if value_chk_gen is "True":
            a = 0
            chk = []
            for value in form.check:
                value_chk = request.form.get(value[0])
                if value_chk != None:
                    form.chk_res[value_chk] = True
            for v in form.chk_res.keys():
                if form.chk_res[v] is True:
                    KSparser.add_pkg(v)
                    return redirect(url_for('ks'))
    return render_template("grouplist.html", form=form)

@app.route('/ks', methods=['GET', 'POST'])
def ks():
    form = ksForm()
    Txt=KSparser.print_screen()
    value_chk_ini = request.form.get("ini")   
    if form.is_submitted():
        print "KS - submit"
        if value_chk_ini is "True":
            print "check_ks"
            return redirect('/')
    return render_template("ks.html", form=form, txt=Txt)
