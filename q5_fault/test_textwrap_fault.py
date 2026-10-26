import unittest
from q5_fault import textwrap


class TestWrapBehavior(unittest.TestCase):
    # Behavior that already works and must keep working after the repair.
    def test_short_text_is_one_line(self):
        self.assertEqual(textwrap.wrap("aaa bbb", width=10), ["aaa bbb"])

    def test_text_too_long_is_split(self):
        self.assertEqual(textwrap.wrap("aaa bbb", width=6), ["aaa", "bbb"])

    def test_long_word_is_broken(self):
        self.assertEqual(textwrap.wrap("abcdefgh", width=3),
                         ["abc", "def", "gh"])

    def test_indent_counts_towards_width(self):
        self.assertEqual(
            textwrap.wrap("aaa bbb ccc", width=8, initial_indent="> "),
            ["> aaa", "bbb ccc"])

    # Reproduces the fault: a line exactly 'width' long must not be split.
    def test_exact_fit_is_one_line(self):
        self.assertEqual(textwrap.wrap("aaa bbb", width=7), ["aaa bbb"])

    def test_exact_fit_fill(self):
        self.assertEqual(textwrap.fill("aaa bbb ccc ddd", width=7),
                         "aaa bbb\nccc ddd")

    def test_shorten_exact_fit(self):
        # Example from the shorten() docstring.
        self.assertEqual(textwrap.shorten("Hello  world!", width=12),
                         "Hello world!")


if __name__ == "__main__":
    unittest.main()
