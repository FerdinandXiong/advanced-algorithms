import unittest
import sys
import os

# Add the algorithms directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.rsa import gen_private_Key, gen_public_key, extendedEuclid, encrypt, decrypt, euclid, text_to_int, int_to_text

# when testing for large prime numbers, e is usually 65537
# since the lecture uses smaller examples, we'll choose e manually for the tests
class TestRSA(unittest.TestCase):
    def test_euclid(self):
        gcd = euclid(104, 24)
        self.assertEqual(gcd, 8)
    
    def test_key_generation(self):
        private_key = gen_private_Key(31, 17, 131)
        self.assertEqual((11, 527), private_key)

    def test_encryption_decryption(self):
        public_key = gen_public_key(7919, 6841, 65537)
        private_key = gen_private_Key(7919, 6841, 65537)
        print(public_key)
        print(private_key)
        message = "H w"
        ciphertext = encrypt(text_to_int(message), public_key)
        print(f"encrypt(message) = ciphertext = {ciphertext}")
        plaintext = int_to_text(decrypt(ciphertext, private_key))
        print(f"decrypt(ciphertext) = plaintext = {plaintext}")
        self.assertEqual(plaintext, message)

if __name__ == "__main__":
    unittest.main()
