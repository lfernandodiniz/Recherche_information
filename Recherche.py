
from flask import Flask, render_template, request, redirect, session, flash, url_for
import pandas as pd
import mysql.connector
from dao import TroubleDao
from models import User, Machine, Trouble_relation
app = Flask(__name__)
app.secret_key = "Equibras"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port = 3306,
    password="NEWPASSWORD",
    auth_plugin='mysql_native_password',
    database='troubleshooting'
)


user1 = User('luan', 'Luan Marques', '1234')
user2 = User('Nico', 'Nico Steppat', '7a1')
user3 = User('Flavio', 'Flavio', 'javascript')

users = {user1.id: user1,
            user2.id: user2,
            user3.id: user3}

machine1 = Machine('E61', 'Ramming')
machine2 = Machine("E60", "Potlining")
lista = [machine1, machine2]

trouble_dao = TroubleDao(db)

@app.route("/")
def index():


    return render_template('index.html', titulo='Machines',
                           lista=lista)

@app.route("/troubleshooting")
def troubleshooting():
    if(True):
        listar = trouble_dao.listar()
        for line in listar:
            print("troubleshooting lista: ", line.description_fault, line.description_cause,
                  line.description_resolution, line.description_reference, line.trouble_no)

    return render_template('troubleshooting.html', titulo='troubleshooting',
                           lista=listar)
#app.run(debug=False)

@app.route('/new')
def new():
    if 'user_logged' not in session or session['user_logged'] == None:

        return redirect(url_for("login", next=url_for('new')))
        #return redirect('/login?next=new') #anterior
    else:
        return render_template('new.html', titulo='New troubleshooting')



@app.route('/create', methods=['POST',])
def create():
    description_fault = request.form['fault']
    description_cause = request.form['cause']
    description_resolution = request.form['resolution_method']
    description_reference = request.form['references']

    trouble = Trouble_relation(description_fault, description_cause, description_resolution, description_reference)
    trouble_dao.salvar(trouble)


    #troubleshooting = Troubleshooting(fault, resolution_method, cause, references)
    #lista2.append(troubleshooting)
    return redirect (url_for('troubleshooting'))

@app.route('/edit/<int:trouble_no>')
def edit(trouble_no):
    if 'user_logged' not in session or session['user_logged'] == None:

        return redirect(url_for("login", next=url_for('edit', trouble_no=trouble_no)))
        #return redirect('/login?next=new') #anterior
    else:
        trouble = trouble_dao.buscar_por_trouble_no(trouble_no)

        return render_template('edit.html', titulo='Edit troubleshooting', trouble=trouble)

@app.route('/update', methods=['POST',])
def update():
    description_fault = request.form['fault']
    description_cause = request.form['cause']
    description_resolution = request.form['resolution_method']
    description_reference = request.form['references']
    former_description_fault = request.form['former_description_fault']
    print(former_description_fault)
    fault_no = trouble_dao.search_fault_no(former_description_fault)
    print(fault_no)
    trouble = Trouble_relation(description_fault, description_cause, description_resolution, description_reference, trouble_no=request.form['trouble_no'], fault_no=fault_no)
    print("antes de mandar salvar: ", trouble.description_fault, trouble.description_cause, trouble.description_resolution,
          trouble.description_reference, trouble.trouble_no)

    trouble_dao.salvar(trouble)

    print("depois de mandar salvar: ", trouble.description_fault, trouble.description_cause, trouble.description_resolution,
                               trouble.description_reference, trouble.trouble_no)


    #troubleshooting = Troubleshooting(fault, resolution_method, cause, references)
    #lista2.append(troubleshooting)
    return redirect(url_for('troubleshooting'))

@app.route('/delete/<int:trouble_no>')
def delete(trouble_no):
    trouble_dao.delete(trouble_no)
    flash('the troubleshooting was sucessfully removed!')
    return redirect(url_for('troubleshooting'))

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['user'] in users:
        user = users[request.form['user']]
        if user.pwd == request.form['pwd']:
            session['user_logged'] = user.id
            flash(user.name + ' successfully logged!')
            next_page = request.form['next']
            return redirect(next_page)
    else:
        flash(' not logged, try again')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['user_logged'] = None
    flash('any user logged!')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
