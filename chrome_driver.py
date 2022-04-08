import info
from selenium import webdriver


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
        self.driver = webdriver.Chrome(options=options)


driverClass = ChromeDriver()



