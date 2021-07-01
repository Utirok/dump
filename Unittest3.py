import unittest
import os
import shutil

class Main(unittest.TestCase):

    def test_equality(self):
        with open('C:\\Program Files (x86)\\some_folder\\some_file.txt', 'r') as it:
            text = it.read()
            self.assertTrue(text == 'There\'s a lady who\'s sure all that glitters is gold \n And she\'s buying a stairway to heaven \n When she gets there she knows, if the stores are all closed With a word she can get what she came for \n Ooh, ooh, and she\'s buying a stairway to heaven')

    def setUp(self) -> None:
        self.path_to_file = 'C:\\Program Files (x86)\\some_folder'
        os.makedirs(self.path_to_file, exist_ok=True)
        with open('C:\\Program Files (x86)\\some_folder\\some_file.txt', 'w') as file:
            file.write('There\'s a lady who\'s sure all that glitters is gold \n And she\'s buying a stairway to heaven \n When she gets there she knows, if the stores are all closed With a word she can get what she came for \n Ooh, ooh, and she\'s buying a stairway to heaven')

    def tearDown(self) -> None:
        shutil.rmtree('C:\\Program Files (x86)\\some_folder')

if __name__ == '__main__':
    unittest.main();
