import unittest
from Les_6_Kravchenko.vigenere_cipher import encode_vigenere
from Les_6_Kravchenko.vigenere_cipher import decode_vigenere


class TestVigenere(unittest.TestCase):

    def test_encode_and_decode(self):
        encoded = encode_vigenere("TEXT" * 5, "KEY")
        self.assertEqual(decode_vigenere(encoded, "KEY"), "TEXT" * 5)
