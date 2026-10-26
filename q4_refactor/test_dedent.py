import random
import textwrap as stdlib_textwrap
import unittest
from q4_refactor import textwrap


class TestDedentCharacterization(unittest.TestCase):
    # Behavior captured from the unmodified CPython 3.13 dedent().
    CASES = [
        ("", ""),
        ("hello", "hello"),
        ("  hello\n  world", "hello\nworld"),
        ("    a\n  b\n      c", "  a\nb\n    c"),
        ("\ta\n\tb", "a\nb"),
        ("  a\n\tb", "  a\n\tb"),             # tabs and spaces never match
        ("  \ta\n  \t  b", "a\n  b"),
        ("  a\n\n  b", "a\n\nb"),
        ("  a\n    \n  b", "a\n\nb"),          # blank lines normalized
        ("  a\n \n  b\n", "a\n\nb\n"),
        ("\n  a\n  b\n", "\na\nb\n"),
        ("  a  \n  b", "a  \nb"),              # trailing whitespace kept
        ("   a\n  b\n    c", " a\nb\n  c"),
    ]

    def test_known_cases(self):
        for text, expected in self.CASES:
            with self.subTest(text=text):
                self.assertEqual(textwrap.dedent(text), expected)

    def test_matches_stdlib_on_random_input(self):
        rng = random.Random(4)
        pieces = [" ", "  ", "\t", "x", "yz", "\n", " \n", "\t\n"]
        for _ in range(2000):
            text = "".join(rng.choice(pieces) for _ in range(rng.randint(0, 20)))
            with self.subTest(text=text):
                self.assertEqual(textwrap.dedent(text),
                                 stdlib_textwrap.dedent(text))


if __name__ == "__main__":
    unittest.main()
