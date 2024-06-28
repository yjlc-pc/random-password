import password as ps


def start():
    print("Welcome to create a new password.")
    print("Author:Yin Jinaglecheng")
    print("Github repository URL:https://github.com/yjlc-pc/random-password")
    output(ask_questions())


def ask_questions():
    while True:
        try:
            byte = ps.ask_number("How long password do you want have?(default:8)", 8)
            letters_byte = ps.ask_number(f"How long letters do you want have?(default:random))", "random")
            numbers_byte = ps.ask_number(f"How long numbers do you want have?(default:random)", "random")
            symbols_byte = ps.ask_number(f"How long symbols do you want have?(default:random)",
                                         "random")
        except ValueError:
            print("Please reenter.")
            continue
        else:
            return {"byte": byte, "letter": letters_byte, "number": numbers_byte, "symbol": symbols_byte}


def output(answer: dict):
    if answer["letter"] == "random" and answer["number"] == "random" and answer["symbol"] == "random":
        password_str = ps.create_password(answer["byte"], answer["letter"], answer["number"], answer["symbol"])
    else:
        password_str = ps.create_password(answer["byte"], answer["letter"], answer["number"], answer["symbol"])
    print(f"your password is {password_str}")


if __name__ == '__main__':
    start()
