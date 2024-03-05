from flask import render_template, request, redirect, url_for, Flask
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonm09"
)

# Ruta para la página principal
@app.route('/')
def pagina_principal():
    return render_template('paginaPrincipal.html')

# Ruta para la página de registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        email = request.form['email']
        contraseña = request.form['password']
        cursor = db.cursor()
        sql_insert = "INSERT INTO nombres_y_correos (email, contraseña) VALUES (%s, %s)"
        cursor.execute(sql_insert, (email, contraseña))
        db.commit()
        return redirect(url_for('login'))  # Redirige al login después del registro
    return render_template('registro.html')

# Ruta para la página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        contraseña = request.form['password']
        cursor = db.cursor()
        sql = "SELECT * FROM nombres_y_correos WHERE email = %s AND contraseña = %s"
        cursor.execute(sql, (email, contraseña))
        usuario = cursor.fetchone()
        if usuario:
            return redirect(url_for('encuesta'))
        else:
            return "Credenciales incorrectas. Inténtalo de nuevo o regístrate si eres un nuevo usuario."
    return render_template('login.html')

# Ruta para la página de encuesta
@app.route('/encuesta')
def encuesta():
    return render_template('encuesta.html')



if __name__ == '__main__':
    app.run(debug=True)
