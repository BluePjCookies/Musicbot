class Formatter:
    def __init__(self):
        self.format_dict = {
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "purple": "\033[35m",
            "cyan ": "\033[36m",
            "white": "\033[37m",
            "blackb": "\033[40m",
            "redb": "\033[41m",
            "greenb": "\033[42m",
            "yellowb": "\033[43m",
            "blueb": "\033[44m",
            "purpleb": "\033[45m",
            "cyanb": "\033[46m",
            "whiteb": "\033[47m",
            "bold": "\033[1m",
            "boff": "\033[22m",
            "italics": "\033[3m",
            "ioff": "\033[23m",
            "underline": "\033[4m",
            "uoff": "\033[24m",
            "linebreak": "\n" + "-" * 40 + "\n",
            "reset": "\033[0m",
        }

        self.enable = True

        # THEMES can be placed here

    def enable(self):
        self.enable = True

    def disable(self):
        self.enable = False

    def __call__(self, *commands):
        if self.enable:
            sentence = ""
            reset = "\033[0m"
            for item in commands:
                if isinstance(item, str):
                    if item.lower() not in self.format_dict.keys():
                        sentence += item
                    else:
                        sentence += self.format_dict[item.lower()]
                else:
                    sentence = f"{sentence}{item}"
            print(sentence + reset)

            return sentence + reset
        else:
            return None
fprint = Formatter()