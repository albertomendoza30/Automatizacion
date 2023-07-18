from flask import Flask, render_template, request
import pyotp

app = Flask(__name__)

# Usuarios de prueba (se deben reemplazar con usuarios reales en un entorno de producción)
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

    # Verificar si el usuario existe en la base de datos de prueba
    if username in users_database:
        # Generar un token OTP para el usuario
        totp = pyotp.TOTP(users_database[username]['otp_secret'])
        otp_code = totp.now()

        # Devolver el código OTP al cliente para las pruebas
        return otp_code

    # Si el usuario no existe, devolver un código de error
    return "Usuario no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)

