import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_correct_login_with_otp(self):
        response = self.app.post('/login', data=dict(
            username='user1',
            password='password123',
            otp_code='123456'
        ))
        self.assertEqual(response.data.decode('utf-8'), "Inicio de sesión exitoso")

    def test_correct_login_without_otp(self):
        response = self.app.post('/login', data=dict(
            username='user2',
            password='qwerty456',
            otp_code=''
        ))
        self.assertEqual(response.data.decode('utf-8'), "Inicio de sesión exitoso")

    def test_incorrect_username(self):
        response = self.app.post('/login', data=dict(
            username='unknown_user',
            password='password123',
            otp_code='123456'
        ))
        self.assertEqual(response.data.decode('utf-8'), "Credenciales inválidas")

    def test_incorrect_password(self):
        response = self.app.post('/login', data=dict(
            username='user1',
            password='wrong_password',
            otp_code='123456'
        ))
        self.assertEqual(response.data.decode('utf-8'), "Credenciales inválidas")

    def test_incorrect_otp_code(self):
        response = self.app.post('/login', data=dict(
            username='user1',
            password='password123',
            otp_code='654321'
        ))
        self.assertEqual(response.data.decode('utf-8'), "Código OTP incorrecto")

if __name__ == '__main__':
    unittest.main()

