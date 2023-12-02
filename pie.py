import os
import random
import time
from getpass import getpass

try:
    from core.exceptions import FileNotFoundError
except ImportError:
    FileNotFoundError = IOError

class System:
    def __init__(self):
        self.commands = {}
        self.register_command("checker_login", self.checker_login)
        self.register_command("command", self.command)
        self.register_command("check_username_password", self.check_username_password)

    def register_command(self, name, func):
        self.commands[name] = func

    def command(self):
        command = input(f"{Fore.CYAN}>{Fore.RESET} ")
        try:
            func = self.commands[command]
        except KeyError:
            print(f"{Fore.RED}UNKNOWN COMMAND{Fore.RESET}")
        else:
            func()

    def checker_login(self):
        try:
            with open("login.txt", "r") as f:
                data = f.readlines()
        except FileNotFoundError:
            print(f"{Fore.RED}FILE 'login.txt' NOT FOUND{Fore.RESET}")
            self.checker_login()
            return

        clear_text()
        print(f"{Fore.LIGHTYELLOW_EX}         __..---..__\n{Fore.YELLOW}     ,-=' {Fore.RED}/ | \\{Fore.YELLOW} `=-.\n{Fore.LIGHTWHITE_EX}    :--..___________..--;\n{Fore.WHITE}     \.,_____________,./ \n{Fore.RED}   ╔═╗╔═╗╔═╗╦╔═╔═╗╔╦╗┌─┐┬┌─┐\n{Fore.LIGHTRED_EX}   ╚═╗║ ║║  ╠╩╗║╣  ║ ├─┘│├┤ \n{Fore.WHITE}   ╚═╝╚═╝╚═╝╩ ╩╚═╝ ╩o┴  ┴└─┘{Fore.RESET}")
        print(f"{Fore.YELLOW}USER - ROOT {Fore.LIGHTYELLOW_EX}PASSWORD - ROOT{Fore.RESET}")
        time.sleep(0.5)
        username = input(f"{Fore.CYAN}USERNAME {Fore.WHITE}${Fore.RESET}")
        time.sleep(0.5)
        password = getpass(f"{Fore.BLUE}PASSWORD {Fore.WHITE}${Fore.RESET}")
        time.sleep(0.5)
        print(F"{Fore.BLUE}LOGIN TO PANEL {Fore.WHITE}({Fore.LIGHTBLUE_EX}TRYING LOGIN WITH {username}@{password}{Fore.WHITE}) . . .{Fore.RESET}")
        time.sleep(int(random.randint(1,3)))
        if self.check_username_password(username, password):
            print(f"{Fore.CYAN}PANEL LOADING . . .{Fore.RESET}")
            time.sleep(1)
            clear_text()
            self.command()
        else:
            print(f"{Fore.RED}FAILED {Fore.YELLOW}WRONG USERNAME OR PASSWORD{Fore.RESET}")
            time.sleep(1)
            clear_text()
            self.checker_login()

    def check_username_password(self, username, password):
        try:
            with open("login.txt", "r") as f:
                data = f.readlines()
        except FileNotFoundError:
            print(f"{Fore.RED}FILE 'login.txt' NOT FOUND{Fore.RESET}")
            return False

        for line in data:
            user, passwd = line.strip().split(":")
            if user == username and passwd == password:
                return True
        return False

system = System()
system.checker_login()
