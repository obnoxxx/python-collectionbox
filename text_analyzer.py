# This module, text_analyzer, contains the core implementation of the text_analyzer program.
# It consists of multiple classes and the main() function and is intended to be imported
# both for testing and for the actual application wrapper, text_analyzer.


import argparse
import sys
from collectionbox import Chain


class TextAnalysisApplication:
    """
    The main application class reads the text, performs analysis, and prints the report.
    """

    def __init__(self, config):
        self._config = config

    def run(self):
        source = TextSource(self._config.filename)
        text = Text(source)
        analysis = Analysis(text)
        print(analysis.report())
        # pass


class TextSource:

    def __init__(self, filename: str | None = None):
        self._filename = filename
        self._filehandle = None

    def _open(self):
        if self._filename is None or self._filename == "" or self._filename == "-":
            self._filehandle = sys.stdin
        else:
            self._filehandle = open(self._filename, "r")
            # return self._filehandle

    def read(self) -> str:
        if self._filehandle == None:
            self._open()
        return self._filehandle.read()


class Text:
    def __init__(self, source: TextSource):
        self._content = source.read()

    def __len__(self):
        return len(self._content)

    @property
    def content(self):
        return self._content


class Analysis:
    def __init__(self, text: Text):

        self._text = text
        self._line_count = len(self._text.content.splitlines())
        self._word_count = len(self._text.content.split())
        self._character_count = len(self._text)

        # Calculate character frequencies
        self._characters = Chain()
        self._different_characters = Chain()

        for char in self._text.content:
            char_obj = Character(char)
            self._characters.add(char_obj)
            if self._different_characters.count(char_obj) == 0:
                self._different_characters.add(char_obj)

    def report(self) -> str:
        report = (
            f"num words: {self._word_count}\n"
            f"num lines: {self._line_count}\n"
            f"num chars: {self._character_count}\n"
            f"num different chars: {len(self._different_characters)}\n\n"
            f"character frequencies:\n"
            f"{'-' * 40}\n"
            f"{'Character':<15} {'Count':>10}\n"
            f"{'-' * 40}\n"
        )

        # Sort by frequency (descending)
        sorted_chars = sorted(
            self._different_characters,
            key=lambda c: self._characters.count(c),
            reverse=True,
        )

        for char_obj in sorted_chars:
            display_char = char_obj.display()
            count = self._characters.count(char_obj)
            report += f"{display_char:<15} {count:>10}\n"

        report += f"{'-' * 40}\n"
        return report


class ApplicationConfiguration:
    """
    The class ApplicationConfiguration holds the configuration for the TextAnalysisApplication
    """

    __slots__ = ("filename", "case_sensitive", "_args")

    def __init__(self):
        # Initialize with default settings
        self.filename = None
        self.case_sensitive = False
        self._args = None

    def fill_from_args(self, args):
        # fill settings from passed args (e. g. from command line parsing)
        # store all args for future flexibility.
        self._args = args
        # initialize config with passed arguments/values
        self.filename = self._args.filename
        self.case_sensitive = self._args.case_sensitive
        pass


class Character:
    """
    class representing a character with flyweight pattern
    """

    __slots__ = "_char"
    _instances = {}  # Class-level cache

    def __new__(cls, value: str):
        cls._validate_value(value)
        if value not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[value] = instance
        return cls._instances[value]

    def __init__(self, value: str):
        self._validate_value(value)
        if not hasattr(self, "_char"):
            self._char = value

    @staticmethod
    def _validate_value(value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Character value must be a string")
        if len(value) != 1:
            raise ValueError("Character value must be exactly one character")

    @property
    def value(self):
        return self._char

    def display(self) -> str:
        """
        Display special characters with their representation
        """
        if self._char == " ":
            display_char = "<space>"
        elif self._char == "\n":
            display_char = "<newline>"
        elif self._char == "\t":
            display_char = "<tab>"
        else:
            display_char = self._char

        return display_char


# if __name__ == "__main__":


def main():

    arg_parser = argparse.ArgumentParser(
        prog="text_analyzer",
        description="perform lexical analysis (count words, characters, and character frequencies) of text input",
        epilog="The program prints a report of the analysis to standard output.",
    )
    arg_parser.add_argument(
        "-f",
        "--filename",
        help="name of file to read text from (instead of reading from stdin)",
    )  # , type=str, dest=filename)
    arg_parser.add_argument(
        "-c",
        "--case-sensitive",
        action="store_true",
        dest="case_sensitive",
        help="perform case-sensitive character frequency analysis",
    )
    args = arg_parser.parse_args()
    config = ApplicationConfiguration()
    config.fill_from_args(args)
    app = TextAnalysisApplication(config)
    app.run()


if __name__ == "__main__":
    main()
