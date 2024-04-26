from colorama import Fore

def print_directory(name, space, is_dir=True):
    color = Fore.BLUE if is_dir else Fore.GREEN
    symbol = '📂' if is_dir else '📄'
    print(f"{color}{'   ' * space}{symbol}{name} {Fore.RESET}")
