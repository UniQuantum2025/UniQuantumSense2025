from cryptography.fernet import Fernet
import unittest

class TestEncryption(unittest.TestCase):
    def setUp(self):

        # Generate a key for encryption
        self.key = Fernet.generate_key()

        # Create a Fernet instance with the generated key
        self.fernet = Fernet(self.key)

    def test_encryption_decryption(self):

        # Data to be encrypted
        data = b"Sensitive data"

        # Encrypt the data
        encrypted = self.fernet.encrypt(data)

        # Decrypt the data
        decrypted = self.fernet.decrypt(encrypted)

        # Assert that the decrypted data matches the original data
        self.assertEqual(data, decrypted, "Decryption did not return the original data")

    def test_invalid_decryption(self):

        # Assert that decrypting invalid data raises an exception
        with self.assertRaises(Exception, msg="Decryption should fail for invalid data"):
            self.fernet.decrypt(b"invalid_encrypted_data")

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()                  