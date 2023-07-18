import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Bienvenido</h1>', response.data)

    def test_correct_login_with_otp(self):
        response = self.app.post('/login', data=dict(
            username='user1',
            password='password123',
            otp_code='123456'
        ))
        self.assertIn(b"Inicio de sesión exitoso", response.data)

    def test_correct_login_without_otp(self):
        response = self.app.post('/login', data=dict(
            username='user2',
            password='qwerty456',
            otp_code=''
        ))
        self.assertIn(b"Inicio de sesión exitoso", response.data)

    def test_incorrect_username(self):
        response = self.app.post('/login', data=dict(
            username='invalid_user',
            password='password123',
            otp_code='123456'
        ))
        self.assertIn(b"Credenciales inválidas", response.data)

    def test_incorrect_password(self):
        response = self.app.post('/login', data=dict(
            username='user1',
            password='wrong_password',
            otp_code='123456'
        ))
        self.assertIn(b"Credenciales inválidas", response.data)

    def test_incorrect_otp_code(self):
        response = self.app.post('/login', data=dict(
            username='user1',
            password='password123',
            otp_code='654321'  # OTP incorrecto
        ))
        self.assertIn(b"Código OTP incorrecto", response.data)


if __name__ == '__main__':
    unittest.main()


