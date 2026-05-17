from unittest import TestCase
from main import TextProcessor


class TestTextProcessor(TestCase):

    def test_find_unique_word_success(self):
        text = "Якесь унікальне слово тут. А тут немає. І тут немає."

        processor = TextProcessor(text)

        self.assertEqual(processor.find_unique_word(), "якесь")

    def test_no_unique_word(self):
        text = "Слово один. Слово два. Один два."

        processor = TextProcessor(text)

        self.assertIsNone(processor.find_unique_word())

    def test_empty_text_error(self):
        # порож текст
        text = "   "

        processor = TextProcessor(text)

        # пер вик пом
        with self.assertRaises(ValueError):
            processor.find_unique_word()

    def test_one_sentence_error(self):
        text = "Тільки одне речення."

        processor = TextProcessor(text)

        # пер вик пом
        with self.assertRaises(ValueError):
            processor.find_unique_word()