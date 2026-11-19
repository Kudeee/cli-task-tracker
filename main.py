from cli import commands, parser


def main():

    if isinstance(parser.parse_command(), SystemExit):
        return parser.parse_command()

    command, args = parser.parse_command()  # pyright: ignore[reportGeneralTypeIssues]

    return commands.handle_command(command, args)


if __name__ == "__main__":
    print(main())
