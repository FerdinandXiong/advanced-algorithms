import unittest
from rsa import genKey, extendedEuclid, encrypt, euclid

# when testing for large prime numbers, e is usually 65537
# since the lecture uses smaller examples, we'll choose e manually for the tests
class TestRSA(unittest.TestCase):
    def test_euclid(self):
        gcd = euclid(104, 24)
        self.assertEqual(gcd, 8)
    def test_key_generation(self):
        private_key = genKey(31, 17, 131)
        self.assertEqual(11, private_key)

    # def test_encryption_decryption(self):
    #     public_key, private_key = generate_keys(512)
    #     message = "Hello, RSA!"
    #     ciphertext = encrypt(message, public_key)
    #     plaintext = decrypt(ciphertext, private_key)
    #     self.assertEqual(plaintext, message)

    # def test_large_message(self):
    #     public_key, private_key = generate_keys(512)
    #     message = "A" * 50  # Large message
    #     ciphertext = encrypt(message, public_key)
    #     plaintext = decrypt(ciphertext, private_key)
    #     self.assertEqual(plaintext, message)

if __name__ == "__main__":
    unittest.main()
