import argparse
import re

__version__ = "0.1.0"


def main():
    parser = argparse.ArgumentParser(
        description="""
    Edits a bib file in-place to contain at most one author / editor,
    and replaces all other authors / editors with "and others".
    """
    )

    parser.add_argument("file", metavar="FILE", type=argparse.FileType("r+"))
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    args = parser.parse_args()
    file = args.file
    content = file.read()

    content = re.sub(
        r"((?:author|editor) *=.*?)(?= and )(.*)(},)", r"\1 and others\3", content
    )

    file.seek(0)
    file.write(content)
    file.truncate()


if __name__ == "__main__":
    main()
