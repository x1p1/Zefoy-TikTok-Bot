try:
    import fade, os, platform, requests, selenium, time, webbrowser, ctypes
    from seleniumbase import BaseCase
    from colorama import Fore, init, Style
except ImportError:
    print("You do not have all the required modules. Please install all of them before retrying.")
    time.sleep(3)
    os._exit(1)

class Bot():
    def __init__(self):
            self.version = "0.0.1"
            self.banner = """
    ▄▄▄█████▓ ██▓ ██ ▄█▀▄▄▄█████▓ ▒█████   ██ ▄█▀
    ▓  ██▒ ▓▒▓██▒ ██▄█▒ ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ 
    ▒ ▓██░ ▒░▒██▒▓███▄░ ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ 
    ░ ▓██▓ ░ ░██░▓██ █▄ ░ ▓██▓ ░ ▒██   ██░▓██ █▄ 
    ▒██▒ ░ ░██░▒██▒ █▄  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄
    ▒ ░░   ░▓  ▒ ▒▒ ▓▒  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
        ░     ▒ ░░ ░▒ ▒░    ░      ░ ▒ ▒░ ░ ░▒ ▒░
    ░       ▒ ░░ ░░ ░   ░      ░ ░ ░ ▒  ░ ░░ ░ 
            ░  ░  ░                ░ ░  ░  ░   
                                                
                ▄▄▄▄    ▒█████  ▄▄▄█████▓                   
                ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒                   
                ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░                   
                ▒██░█▀  ▒██   ██░░ ▓██▓ ░                    
                ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░                    
                ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░                      
                ▒░▒   ░   ░ ▒ ▒░     ░                       
                ░    ░ ░ ░ ░ ▒    ░                         
                ░          ░ ░                              
                    ░                                      """
            self.url = "https://zefoy.com"
            self.fade = fade.greenblue(self.banner)
            self.driver = selenium.webdriver.Chrome()
            
            if platform.system() == "Windows":
                self.clear = "cls"
            else:
                self.clear = "clear"
            
            self.color = Fore.LIGHTBLUE_EX
            self.color2 = Fore.LIGHTYELLOW_EX
            self.color3 = Fore.LIGHTGREEN_EX
            self.color4 = Fore.LIGHTRED_EX
            self.sent = 0

            self.xpath_captcha = {
                "captcha_box": "/html/body/div[5]/div[2]/form/div/div",
                "captcha_input": "/html/body/div[5]/div[2]/form/div/div/div/input",
                "captcha_submit": "/html/body/div[5]/div[2]/form/div/div/div/div/button",
            }
            self.xpaths_menu = {
                "menu": "/html/body/div[6]/div/div[2]/div/div",
                "comments_hearts": "/html/body/div[6]/div/div[2]/div/div/div[4]/div/button",
                "views": "/html/body/div[6]/div/div[2]/div/div/div[5]/div/button",
                "shares": "/html/body/div[6]/div/div[2]/div/div/div[6]/div/button",
                "favorites": "/html/body/div[6]/div/div[2]/div/div/div[7]/div/button",
            }

    def menu(self):
        os.system(self.clear)
        self.change_title("TikTok Bot - Main Menu | GitHub: @cyclothymia")
        print(self.fade)
        time.sleep(1)
        self.driver.get(self.url)

        print("\n" + self.color + "Waiting on Zefoy website to load ")
        print(self.color + "if you get a 502 error, that means your country is blocked or your VPN is on.")
        self.wait_for_xpath(self.xpath_captcha["captcha_box"])
        print()
        print(self.color + "Site loaded, enter the CAPTCHA to continue.")
        captcha_input = input("\n" + self.color + "Captcha Answer: ")

        element = self.driver.find_element("xpath", self.xpath_captcha["captcha_input"])
        element.clear()
        element.send_keys(captcha_input)
        self.driver.find_element("xpath", self.xpath_captcha["captcha_submit"]).click()
        self.wait_for_xpath(self.xpaths_menu["menu"])

        os.system(self.clear)
        print(self.color + self.fade)
        print()

        print(self.color3 + "1. Comments Hearts")
        print(self.color3 + "2. Views")
        print(self.color3 + "3. Shares")
        print(self.color3 + "4. Favorites")
        print(self.color3 + "5. Exit")
        print()

        option = input(self.color + "Select your option: ")
        if option == "1":
            div = "9"
            self.driver.find_element("xpath", self.xpaths_menu["comments_hearts"]).click()
        elif option == "2":
            div = "10"
            self.driver.find_element("xpath", self.xpaths_menu["views"]).click()
        elif option == "3":
            div = "11"
            self.driver.find_element("xpath", self.xpaths_menu["shares"]).click()
        elif option == "4":
            div = "12"
            self.driver.find_element("xpath", self.xpaths_menu["favorites"]).click()
        else:
            print("\n" + self.fade + "Closing program...")
            os._exit(1)

        input_box = f"/html/body/div[{div}]/div/form/div/input"
        search_box = f"/html/body/div[{div}]/div/form/div/div/button"
        vid_info = input("\n" + self.color + "Enter the Username or Video URL: ")
        self.send_req(search_box, input_box, vid_info, div)

    def send_req(self, search_box, main_xpath, vid_info, div):
        wait_time = 150
        element = self.driver.find_element("xpath", main_xpath)
        element.clear()
        element.send_keys(vid_info)
        time.sleep(3)

        send_button = f"/html/body/div[{div}]/div/div/div[1]/div/form/button/i"
        self.driver.find_element("xpath", send_button).click()
        self.send += 1

        print(self.color3 + f"Sent {self.sent} times. Waiting {wait_time} seconds before resending..." + Style.RESET_ALL)
        time.sleep(wait_time)
        self.send_req(search_box, main_xpath, vid_info, div)

    def change_title(self, arg):
        if self.clear == "cls":
            ctypes.windll.kernel32.SetConsoleTitleW(arg)

    def wait_for_xpath(self, xpath):
        while True:
            try:
                f = self.driver.find_element('xpath', xpath)
                return True
            except selenium.common.exceptions.NoSuchElementException:
                pass

if __name__ == "__main__":
    obj = Bot()
    obj.menu()
    input()