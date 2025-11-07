import sys
import argparse
from urllib.parse import urlparse
import webbrowser


def main():

    parser = argparse.ArgumentParser(description="Open links in browser")
    parser.add_argument("links", nargs="+", help="URLs to open")
    parser.add_argument("--http", action="store_true",
                        help="use http for autocompletion")

    args = parser.parse_args()

    for link in args.links:
        parsed = urlparse(link)
        if not parsed.scheme:
            protocol = "http" if args.http else "https"
            link = f"{protocol}://{link}"
        webbrowser.open(link)
        print(f"Opened {link}")

if __name__ == "__main__":
    sys.exit(main())