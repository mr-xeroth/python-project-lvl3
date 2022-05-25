import os


from page_loader.modules.download import download


def parse_cli_args():
    """
    returns (url, folder)
    """
    parser = argparse.ArgumentParser(description='page-loader')
    parser.add_argument('url', type=str, default=None)
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--folder', type=str, default="./")

    # if len(sys.argv) == 1:
    #     parser.print_help(sys.stderr)
    #     sys.exit(0)

    args = parser.parse_args(sys.argv[1:])

    return args.url, args.folder



def main():
    #file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
    #file_path = download('http://pixabay.com', '/var/tmp')
    file_path = download('http://ru.dec.io', '/var/tmp')
    print(file_path)


if __name__ == '__main__':
    main()