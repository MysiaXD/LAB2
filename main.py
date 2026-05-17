import io
import re


class TextProcessor:
    def __init__(self, text: str):
        # ініц буф текст
        self.buffer = io.StringIO(text)

    def _get_sentences(self, text: str) -> list[str]:
        # розб текст реч
        return [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]

    def _get_words(self, sentence: str) -> list[str]:
        # отр сл реч
        return re.findall(r'\b\w+\b', sentence.lower())

    def find_unique_word(self) -> str | None:
        # чит дан буф
        raw_text = self.buffer.getvalue()

        if not raw_text.strip():
            raise ValueError("текст порожній")

        # форм спис реч
        sentences = self._get_sentences(raw_text)

        if len(sentences) < 2:
            raise ValueError("треба >1 реч")

        # сл перш реч
        first_words = self._get_words(sentences[0])

        # збір інш сл
        other_words = set()
        for s in sentences[1:]:
            other_words.update(self._get_words(s))

        for w in first_words:
            if w not in other_words:
                return w

        return None


if __name__ == "__main__":
    # вх тест текст
    sample_text = "Якесь перше речення з унікальним словом. А це вже друге речення. І третє речення тут."

    try:
        # ств об кл
        processor = TextProcessor(sample_text)

        # вик мет пош
        result = processor.find_unique_word()

        if result:
            print(f"знайдене слово: {result}")
        else:
            print("такого слова немає")

    except ValueError as e:
        print(f"помилка даних: {e}")
    except Exception as e:
        print(f"непередбачувана помилка: {e}")