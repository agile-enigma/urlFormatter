import sys
import getopt
import urlFormatter


def main():
    help_menu = "\nBulk URL Formatter converts URLs to a format that is analytically useful."\
                "\nFor detailed information on usage and additional features see the README."\
                + "\n\nUsage: python3 url_formatter.py [OPTIONS]"\
                + "\n\nOptions:"\
                + "\n\t--help/-h: display this help menu"\
                + "\n\t--unshorten/-u: unshorten shortened URLs"\
                + "\n\t--clean/-c: clean URLs\n"

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "uch", ["unshorten", "clean", "help"])

        u = False
        c = False
        h = False
        for opt, arg in opts:
            if opt in ["-u", "--unshorten"]:
                u = True
            if opt in ["-c", "--clean"]:
                c = True
            if opt in ["-h", "--help"]:
                h = True

        if h is True:
            print(help_menu)
        else:
            raw_links = []
            raw_links_path = input("\nPlease enter path to raw links file: ")
            identifier = input("\nPlease enter an identifier for the output filename: ")

            with open(raw_links_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    raw_links.append(line.replace("\n", ""))
            # if options u and c are provided, first run unshorten() and then clean()
            if u is True and c is True:
                formatter_obj = formatter(raw_links)
                formatter_obj.unshorten()
                cleaned_links = formatter_obj.clean()
                with open(identifier + "_cleaned_unshortened_links.txt", "w") as file:
                    for link in cleaned_links:
                        file.write(link + "\n")
            elif u is True:
                formatter_obj = formatter(raw_links)
                expanded_links = formatter_obj.unshorten()
                with open(identifier + "_unshortened_links.txt", "w") as file:
                    for link in expanded_links:
                        file.write(link + "\n")
            elif c is True:
                formatter_obj = formatter(raw_links)
                cleaned_links = formatter_obj.clean()
                with open(identifier + "_cleaned_links.txt", "w") as file:
                    for link in cleaned_links:
                        file.write(link + "\n")
    except Exception as error:
        print(error)


main()
