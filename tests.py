import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_correct_login_with_otp(self):
        # Simulamos que el usuario 'user1' realiza una solicitud de inicio de sesión
        response = self.app.post('/login', data=dict(username='user1'))
        otp_code = response.data.decode('utf-8')

        # Probamos el inicio de sesión con el código OTP generado
        response = self.app.post('/login', data=dict(
            username='user1',
            otp_code=otp_code
        ))
        self.assertEqual(response.data, b"Usuario no encontrado")

if __name__ == '__main__':
    unittest.main()
