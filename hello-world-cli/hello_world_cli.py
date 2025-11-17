import argparse

class HelloCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Hello World CLI"
        )

        self.parser.add_argument(
            "name",
            nargs="?",
            default="World",
            help="Name to greet (default: World)"
        )

    def run(self):
        args = self.parser.parse_args()
        self.say_hello(args.name)

    def say_hello(self, name: str):
        print(f"\nHello, {name}!")

def main():
    cli = HelloCLI()
    cli.run()

if __name__=="__main__":
    main()