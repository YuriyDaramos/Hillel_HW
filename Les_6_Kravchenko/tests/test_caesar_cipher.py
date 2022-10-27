import unittest
from Les_6_Kravchenko.caesar_cipher import encode_caesar
from Les_6_Kravchenko.caesar_cipher import decode_caesar


class TestCaesar(unittest.TestCase):

    def test_encode_and_decode(self):
        encoded = encode_caesar("TEXT" * 5, 5)
        self.assertEqual(decode_caesar(encoded, 5), "TEXT" * 5)
