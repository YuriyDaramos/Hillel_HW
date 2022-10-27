import unittest
from censor import censor_text


class TestCensor(unittest.TestCase):

    def test_single_word(self):
        self.assertEqual(censor_text("Qwerty", ["qwerty"]), "Q*****")

    def test_single_word_in_text(self):
        self.assertEqual(censor_text("Qwerty -- bad word", ["qwerty"]), "Q***** -- bad word")

    def test_word_part(self):
        self.assertEqual(censor_text("QwertyQwerty", ["qwerty"]), "QwertyQwerty")

    def test_add_punct_marks(self):
        self.assertEqual(censor_text("Qwerty,", ["qwerty"]), "Q*****,")

    def test_different_textcase(self):
        self.assertEqual(censor_text("Qwerty and qwerty -- bad words", ["qwerty"]), "Q***** and q***** -- bad words")

    def test_meme_blood_and_concrete(self):
        text = "You motherfucker, come on, you little ass... fuck with me, eh?! You fucking little asshole, " \
               "dickhead, cocksucker... You fuckin’ — come on, come fuck with me! I’ll get your ass, you jerk! Oh, " \
               "you fuckhead, motherfucker! Fuck all you and your family! Come on, you cocksucker, slime bucket, " \
               "shitface, turdball! Come on, you scum sucker, you fucking with me?! Come on, you asshole! "
        blacklist = ["Motherfucker", "ass", "fuck", "fucking", "asshole", "dickhead", "cocksucker", "fuckin", "jerk",
                     "fuckhead", "shitface", "turdball", "Sucker"]
        censored_text = "You m***********, come on, you little a**... f*** with me, eh?! You f****** little a******, " \
                        "d*******, c*********... You f*****’ — come on, come f*** with me! I’ll get your a**, " \
                        "you j***! Oh, you f*******, m***********! F*** all you and your family! Come on, " \
                        "you c*********, slime bucket, s*******, t*******! Come on, you scum s*****, you f****** " \
                        "with me?! Come on, you a******! "
        self.assertEqual(censor_text(text, blacklist), censored_text)
