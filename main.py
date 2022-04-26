import os
import time
import traceback
import threading
import ConnectBot
import pathlib

global title
title = """
   ___                                   _      ___         _   
  / __\  ___   _ __   _ __    ___   ___ | |_   / __\  ___  | |_ 
 / /    / _ \ | '_ \ | '_ \  / _ \ / __|| __| /__\// / _ \ | __|
/ /___ | (_) || | | || | | ||  __/| (__ | |_ / \/  \| (_) || |_ 
\____/  \___/ |_| |_||_| |_| \___| \___| \__|\_____/ \___/  \__|                                                                                                                                                                    
 Release v0.0.1           Written by Mitch Naake, Butler College
 26th Apr, 2022            https://github.com/Mitch0S/ConnectBot
 """

# print(ConnectBot.Botting().General().OAUTH().get_oauth(username="mitch.naake", password="Jedda2022***"))
# ConnectBot.Exploits.accounts().lock_account_bulk(usernames=usernames)

class ConnectBotCLI:
    def __init__(self):
        os.system("clear")
        self.cli().main()

    class cli:
        def main(self):
            while True:
                print(title)

                self.CheckLoginStatus().do_login()

                self.command = input("Command:\n> ")
                self.command_list = self.command.split(" ")

                if self.command_list[0].lower() not in ['lock_account', 'feedutil', 'botutil']:
                    input(f"[?] Error: Unknown command, '{self.command_list[0]}' [PRESS ENTER]")
                    self.clear_cli()

                ### `BLOCK_USER` COMMAND ###
                if self.command_list[0].lower() == 'lock_account':
                    try:
                        if self.command_list[1].lower() == '--bulk':
                            try:
                                with open(pathlib.PosixPath("ConnectBot/"+self.command_list[2]).resolve()) as username_file:
                                    username_file = username_file.readlines()
                                    usernames = []
                                    for username in username_file:
                                        usernames.append(username.strip())
                                    try:
                                        if self.command_list[3] == '--loop':
                                            try:
                                                loop_time = float(self.command_list[4])
                                            except:
                                                loop_time = 60
                                            ConnectBot.Exploits.Accounts().lock_account_bulk(usernames=usernames, loop=True, loop_time=loop_time)

                                    except:
                                        ConnectBot.Exploits.Accounts().lock_account_bulk(usernames=usernames)
                                        self.clear_cli()
                            except FileNotFoundError:
                                input("[?] Error: The file you specified could not be found [PRESS ENTER]")
                                self.clear_cli()
                        else:
                            try:
                                ConnectBot.Exploits.Accounts().lock_account(username=self.command_list[1])
                            except IndexError:
                                input(f"[!] Error: You must specify a Connect username [PRESS ENTER]")

                    except IndexError:
                        input("[?] Error: Invalid Syntax. [PRESS ENTER]")
                        self.clear_cli()

                if self.command_list[0].lower() == 'feedutil':
                    if '--get_feed' in self.command_list:
                        try:
                            quantity = self.command_list[self.command_list.index("--get_feed")+1]
                            access_token = self.command_list[self.command_list.index("--token")+1]
                            ConnectBot.Botting.Feed().get_feed(quantity=quantity, access_token=access_token)
                            input('[!] Success! Retrieved feed successfully [PRESS ENTER')
                            self.clear_cli()
                        except:
                            traceback.print_exc()

                if self.command_list[0].lower() == 'botutil':
                    if '--bot_notice' in self.command_list:
                        try:
                            threads = int(self.command_list[self.command_list.index("--threads") + 1])
                            views_per_thread = int(self.command_list[self.command_list.index("--views") + 1]) / threads
                            access_token = open(pathlib.PosixPath("ConnectBot/auth.token"), "r+").read()
                            item_event = self.command_list[self.command_list.index("--item_event") + 1]

                            viewbot_threads = []
                            for thread in range(threads):
                                new_thread = threading.Thread(target=ConnectBot.Botting.ViewBot().do_item_event, kwargs={'views': views_per_thread, 'access_token': access_token, 'item_event': item_event})
                                viewbot_threads.append(new_thread)
                                new_thread.start()
                            print(f"[*] Started {threads} threads @ {views_per_thread} views (Total: {int(self.command_list[self.command_list.index('--views') + 1])})")

                            threads_running = True
                            while threads_running:
                                threads_finished = 0
                                for viewbot_thread in viewbot_threads:
                                    if not viewbot_thread.is_alive():
                                        threads_finished += 1
                                if threads_finished == len(viewbot_threads):
                                    threads_running = False
                            input("[*] Successfully botted the notice's views [PRESS ENTER]")
                            self.clear_cli()

                        except:
                            traceback.print_exc()


        class CheckLoginStatus:
            def get_login_status(self):
                pass

            def do_login(self):
                try:
                    with open(pathlib.PosixPath("ConnectBot/auth.token"), "r+") as token_file:
                        try:
                            check_token = ConnectBot.Botting.Feed().get_feed_json(access_token=token_file.read(), quantity=1)
                            if check_token['status'] == "ok":
                                logged_in = True
                            else:
                                input("[!] Your previous session has expired, you need to login again... [PRESS ENTER]")
                                logged_in = False
                        except:
                            print("[!] An unknown error has occurred, please contact Mitch :)")
                        while not logged_in:
                            os.system("clear")
                            print(title)
                            print("[*] Enter your Connect username and password below to log into ConnectBot!")
                            username = str(input("Username: "))
                            password = str(input("Password: "))
                            response = ConnectBot.Botting.Auth().get_oauth(username=username, password=password)
                            if response["status"] == 'ok':
                                with open(pathlib.PosixPath("ConnectBot/auth.token"), "w+") as write_token_file:
                                    write_token_file.write(response['token'])
                                    write_token_file.close()
                                logged_in = True
                                input("[*] Login success! [PRESS ENTER] to continue!")
                                os.system("clear")
                                ConnectBotCLI()
                            else:
                                input("[!] Error: Unable to login, username or password were incorrect. Try again. [PRESS ENTER]")

                except FileNotFoundError:
                    with open(pathlib.PosixPath("ConnectBot/auth.token"), "w+") as create_token_file:
                        create_token_file.close()
                        self.do_login()


        def clear_cli(self):
            os.system("clear")



"""
access_token='8ec05896-a803-4df7-bc52-97b0fa04a56c',
    quantity=2
    ItemEvent:3850171426
    
botutil --bot_notice --token 8ec05896-a803-4df7-bc52-97b0fa04a56c --views 10000 --threads 100 --item_event ItemEvent:3850171426

"""
ConnectBotCLI()