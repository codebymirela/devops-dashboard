from flask import Flask, render_template, session, redirect, url_for, request
import psutil
import platform

app = Flask(__name__)
app.secret_key = 'chave_segura_mirela' 

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('lg') == "mirela" and request.form.get('se') == "3001":
            session['Logado'] = True
            return redirect(url_for('menu'))
    return render_template('index.html')

@app.route('/menu')
def menu():
    if not session.get('Logado'):
        return redirect(url_for('login'))
    return render_template('menu.html')

@app.route('/status')
def status():
    if not session.get('Logado'):
        return redirect(url_for('login'))
    
    info = {
        "cpu": psutil.cpu_percent(interval=1),
        "memoria": psutil.virtual_memory().percent,
        "so": platform.system(),
        "versao": platform.release(),
        "discos": psutil.disk_usage('/').percent
    }
    return render_template('status.html', dados=info)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)