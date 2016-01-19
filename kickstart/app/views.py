from flask import render_template, flash, redirect, request, url_for, session
from app import app
from form import ksForm
from KSP import KSP
import json
KSparser = KSP()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ksForm()
    KSparser.start()
    form_action = url_for('index')
    if request.method == 'POST' and form.validate_on_submit():
        #session['desktop_env'] = request.form['X']
        #print request.form['X']
        KSparser.load( request.form['X'])#session['desktop_env'])
        return redirect(url_for('config'))
    return render_template("index.html", form_action=form_action,form=form)


@app.route('/grouplist', methods=['GET', 'POST'])
def grouplist():
    form = ksForm()
    form_action = url_for('grouplist')
    value_chk_gen = request.form.get("gen")
    if request.method == 'POST' and form.is_submitted():
        value_chk_atr = request.form.get("atr")    
        value_chk_gen = request.form.get("gen")    
        print value_chk_atr
        if value_chk_atr == 'True':
            return redirect(url_for('index'))
        if value_chk_gen == 'True':   
            if request.method == 'POST' and form.is_submitted():
                chk = []
                for value in form.check_group:
                    value_chk = request.form.get(value)
                    print value_chk
                    if value_chk != None:
                        form.chk_res[value_chk] = True
                    else:
                        form.chk_res[value_chk] = None 
                for v in form.chk_res.keys():
                    print v
                    if form.chk_res[v] is True:
                        KSparser.add_pkg(v.encode('ascii'))
                        print v
            return redirect(url_for('ks'))
    return render_template("grouplist.html", form_action=form_action, form=form)




@app.route('/config', methods=['GET', 'POST'])
def config():
    form = ksForm()
    form_action = url_for('config')
    if request.method == 'POST' and form.is_submitted():
        session['time_zone'] = form.time_zone.data
        session['select_locale'] = form.select_locale.data
        session['select_keymap'] = form.select_kyemap.data
        k_time = form.time_zone.data
        k_lang = form.select_locale.data
        k_key = form.select_kyemap.data
        # tengo que hacer un diccionario para resolver el teclado y el lang
        # porque el .txt tiene mas info de la que corresponde
        #KSparser.lang_time_key(k_key,k_lang,k_time)

        return redirect(url_for('grouplist'))
    return render_template("config.html", form_action=form_action, form=form)


#@app.route('/grouplist', methods=['GET', 'POST'])
#def grouplist():
#    form = ksForm()
#    form_action = url_for('grouplist')
#    if request.method == 'POST' and form.is_submitted():
#        value_chk_atr = request.form.get("atr")    
#        value_chk_gen = request.form.get("gen")    
#        print value_chk_atr
#        if value_chk_atr == 'True':
#            print "-----------"
#            return redirect(url_for('config'))
#        if value_chk_gen == 'True':
#            a = 0
#            chk = []
#            for value in form.check:
#                value_chk = request.form.get(value[0])
#                if value_chk != None:
#                    form.chk_res[value_chk] = True
#            for v in form.chk_res.keys():
#                if form.chk_res[v] is True:
#                    KSparser.add_pkg(v.encode('ascii'))
#            return redirect(url_for('ks'))
#    return render_template("grouplist.html", form_action=form_action, form=form)

@app.route('/ks', methods=['GET', 'POST'])
def ks():
    form = ksForm()
    archivo=open("pruebaks.ks","w")
    Txt=KSparser.print_screen()
    print Txt
    ascii_txt=Txt.encode("ascii")
    archivo.writelines(ascii_txt)
    archivo.close()
    value_chk_ini = request.form.get("ini")   
    if form.is_submitted():
        #print "KS - submit"
        
        #print value_chk_ini
        if value_chk_ini == "True":
            print request.form['ks']
            #print "check_ks"
            return redirect('/')
    return render_template("ks.html", form=form, txt=ascii_txt)
