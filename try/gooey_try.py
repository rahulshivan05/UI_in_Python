from gooey import Gooey, GooeyParser


@Gooey(program_name="My GUI Program")
def main():
    parser = GooeyParser(description="Demo with Gooey!")
    parser.add_argument('File', widget="FileChooser")
    parser.add_argument('Date', widget="DateChooser")
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
