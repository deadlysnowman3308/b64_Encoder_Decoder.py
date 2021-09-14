import base64, os
from colorama import Fore, Style
from colorama.initialise import init
import time
from colorama.ansi import Back
import gc

gc.collect()

start_time = time.time()
def logo():
    BR = "\033[1;91m"      
    BG = "\033[1;32m"            
    _Off = "\033[0m" 
    blue_deep = "\033[1;94m"
    print(r"""      
         {}______________________________________________________ {}      
                           
                      {} _    /\  __   _  _                    
                      | |__|/\|/ /_ | || |                   
                      | '_ \  | '_ \| || |_                  
                      | |_) | | (_) |__   _|                 
                      |_.__/   \___/   |_|                   
             {}  
             {}___                             _              
            (  _`\                          ( )             
            | | ) |   __     ___    _      _| |   __   _ __ 
            | | | ) /'__`\ /'___) /'_`\  /'_` | /'__`\( '__)
            | |_) |(  ___/( (___ ( (_) )( (_| |(  ___/| |   
            (____/'`\____)`\____)`\___/'`\__,_)`\____)(_)  {}
              
         {}______________________________________________________ {}     
         
               """.format(blue_deep,_Off,BR, _Off, BG, _Off, blue_deep, _Off))
     
def file_check():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()
    user_InpuT = str(input(Fore.CYAN + Style.BRIGHT  + "\n\n\t[?] Type your file location / name --> " + Fore.YELLOW))
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()
    new_string = remove(user_InpuT)
    #path = os.path.abspath(new_string)
    path = str(new_string.strip())
    file_name = os.path.splitext(os.path.basename(path))[0].split(".")[0]
    main(path, file_name)
    file_size(path)
    
def remove(user_InpuT):
    characters_to_remove = "'" + '"' + "&"
    new_string = user_InpuT.replace('"', "")
    for character in characters_to_remove:
        new_string = new_string.replace(character, "").strip()
    return new_string

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(path):
    if os.path.isfile(path):
        file_info = os.stat(path)
        return convert_bytes(file_info.st_size)
    main(path)

def main(path, file_name):
    init()
    blue_deep = "\033[91;7m"
    _Off = "\033[0m"
    image = open(f"{path}", 'rb') #open binary file in read mode
    image_read = image.read()
    image_64_decode = base64.decodebytes(image_read)
    print(Fore.YELLOW + f"{image_64_decode}".strip()+ Style.RESET_ALL)
    with open(f"_{file_name}_b64_decoded.txt", "wb") as nothing:
        nothing.write(image_64_decode.strip())
    a = "{}_{}".format(blue_deep, _Off)*130
    end = round(time.time() - start_time ,2)    
    print("\n"+a+ "\n\n"+Fore.CYAN +Style.BRIGHT+"[!] Decrypted data saved in -->  "+Fore.GREEN +Back.BLACK+f"_{file_name}_b64_decoded.txt"+"\n"+Fore.RED+Style.BRIGHT+"\n[!] Main File Size --> " +Fore.MAGENTA+file_size(path)+Style.RESET_ALL+"\n"+"\n[*] Total time elapsed:>  ", end ,"sec"+ "\n\n"+a)
    input("\nPress enter for exit")
if __name__ =="__main__":
    file_check()