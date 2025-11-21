from rich.color import Color




def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
             return (f"""[bold red]⚠️ Invalid input format(expected: "[command] [username] [phone]"). 
                     Please check your command and try again.[/bold red]""")
        except KeyError:
            return (f"[bright yellow]⚠️ Contact not found [/bright yellow]")
        except IndexError as e:
            return (f"💥 Oops, something went wrong: {e}")

    return inner

