from flask import Flask, render_template, request
import pyotp

app = Flask(__name__)

# Base de datos simulada (se debe reemplazar con una real en un entorno de producción)
users_database = {
    "user1": {
        "password": "password123",
        "otp_secret": pyotp.random_base32()
    },
    "user2": {
        "password": "qwerty456",
        "otp_secret": pyotp.random_base32()
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    otp_code = request.form['otp_code']

    if username in users_database and users_database[username]['password'] == password:
        totp = pyotp.TOTP(users_database[username]['otp_secret'])
        if totp.verify(otp_code):
            return "Inicio de sesión exitoso"
        else:
            return "Código OTP incorrecto"
    else:
        return "Credenciales inválidas"

if __name__ == '__main__':
    app.run(debug=True)

