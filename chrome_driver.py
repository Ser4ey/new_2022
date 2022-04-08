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
        self.driver = webdriver.Chrome(options=options)

    def login_in_bet365(self, login=info.user_name, password=info.password):
        self.driver.get('https://www.bet365.com/')
        time.sleep(7)

        # Cookies
        try:
            self.driver.find_element_by_class_name('ccm-CookieConsentPopup_Accept ').click()
        except:
            print('Нет cookies')


        self.driver.find_element_by_class_name('hm-MainHeaderRHSLoggedOutWide_LoginContainer')

        print(f'Вход в аккаунт: {login}')
        time.sleep(1.5)
        # вход в аккаунт bet365ru
        try:
            self.driver.find_element_by_class_name('hm-MainHeaderRHSLoggedOutWide_LoginContainer').click()
        except:
            return f'Не удалось войти в аккаунт {login}!'

        self.driver.find_element_by_class_name('lms-StandardLogin_Username').send_keys(login)
        time.sleep(0.7)
        self.driver.find_element_by_class_name('lms-StandardLogin_Password').send_keys(password)
        time.sleep(0.7)

        self.driver.find_element_by_class_name('lms-LoginButton').click()
        time.sleep(3)

        # закрываем новое окно 4 дек 2021
        try:
            time.sleep(3)
            print('Close window!')
            frame = self.driver.find_element_by_class_name('lp-UserNotificationsPopup_Frame ')
            self.driver.switch_to.frame(frame)
            self.driver.find_element_by_class_name('accept-button').click()
        except Exception as er:
            print(er)
            pass
        finally:
            self.driver.switch_to.default_content()

        # закрываем окно с почтой
        try:
            time.sleep(3)
            frame = self.driver.find_element_by_class_name('lp-UserNotificationsPopup_Frame')
            self.driver.switch_to.frame(frame)
            self.driver.find_element_by_id('RemindMeLater').click()
        except Exception as er:
            pass
        finally:
            self.driver.switch_to.default_content()

        try:
            time.sleep(3)
            self.driver.find_element_by_class_name('pm-MessageOverlayCloseButton ').click()
        except:
            pass

        print(f'Вы успешно вошли в аккаунт {login}')
        return 'Успешный вход в аккаунт'


driverClass = ChromeDriver()
driverClass.login_in_bet365()

needed_driver = driverClass.driver



