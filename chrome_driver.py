import info
from selenium import webdriver
import time

class ChromeDriver:
    def __init__(self,
                 user_data_dir=info.path_to_chrome_user_dir,
                 profile_directory=info.chrome_profile_name,
                 ):
        self.user_data_dir = user_data_dir
        self.profile_directory = profile_directory

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument(f'user-data-dir={self.user_data_dir}')
        options.add_argument(f"profile-directory={self.profile_directory}")
        # options.add_argument(f"--incognito")
        self.driver = webdriver.Chrome(options=options)

    def login_in_bet365(self, login=info.user_name, password=info.password):
        self.driver.get('https://www.bet365.com/')
        print(f'Login: {login}')
        print(f'Password: {password}')
        input('Войдите в аккаунт и нажмите Enter:')
        return


driverClass = ChromeDriver()
driverClass.login_in_bet365()

needed_driver = driverClass.driver



