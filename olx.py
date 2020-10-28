class Main:
        def __init__(self):
                try:
                        shutil.rmtree("lib/__pycache__")
                        shutil.rmtree("war/__pycache__")
                except: pass
                os.system('cls' if os.name == 'nt' else 'clear')
                self.menu()

        def menu(self):
                print(f"""{c}.....................SpamSms(OLX)....................

{c}# Coded by   : Mr.Tcg Cyber
{c}# My Team    : L C I
{c}# Contact    : +6283813844572

{c}...................................................
            copyright ©2020 | 28-10-2020
{c}===================================================
{k}[{c}1{k}] {u} SPAM {c}Olx
{k}[{c}0{k}] {r} Exit
""")
                pil = int(input(f'{p}dimasaryo_17 {c}==> {k}'))
                if pil == 1:
                        nom = input(f'{r}\nEx : {o}89510512xxx\n{k}[*] {c}Nomor  : {k}')
                        Thread(olx(self, nom)).start()
                elif pil == 0:
                        sleep(1)
                        exit("")
                else:
                        print(f"{k}[!] Pilih Yang Bener Cok")
                        self.menu()

if __name__ == '__main__':
        try:
                        import os,sys,shutil
                        from time import sleep
                        from threading import *
                        from war.war import *
                        from lib.a import *
                        from lib.b import *
                        from lib.c import *
                        from lib.d import *
                        from lib.e import *
                        from lib.f import *
                        from lib.g import *
                        from lib.h import *
                        from lib.i import *
                        from lib.j import *
                        Thread(target=Main).start()
        except IOError: pass
