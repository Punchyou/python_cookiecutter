import argparse


def greet(name=None):
    """
    Returns a greeting message.

    Parameters:
    ----------
    name: str
        The name of the person to greet.

    Returns:
    -------
    str: A greeting message.
    """
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"


def main():
    parser = argparse.ArgumentParser(
        description="A simple Python project template."
    )
    parser.add_argument("--name", type=str, help="Your name")
    args = parser.parse_args()

    print(greet(args.name))


if __name__ == "__main__":
    main()
