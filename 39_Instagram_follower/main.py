#region IMPORT

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

#endregion

#region INIT

CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
SIMILAR_ACCOUNT = "SIMILAR ACCOUNT"
USERNAME = "YOUR INSTAGRAM USERNAME"
PASSWORD = "YOUR INSTAGRAM PASSWORD"

#endregion

class InstaFollower:

    """<DOC

        Manages Instagram automation for following followers of a similar account.

            METHODS:
                        -__init__ -> None
                        -login -> None
                        -find_followers -> None
                        -follow -> None

    DOC?>"""

    def __init__(self, path) -> None:

        """<DOC

            Initialize the InstaFollower with the Chrome WebDriver.

                PARAMETERS:
                            path (str): The path to the Chrome WebDriver executable.

        DOC?>"""

        #region CODE
        
        self.driver = webdriver.Chrome(executable_path=path)

        #endregion
    
    def login(self) -> None:

        """<DOC

            Logs into Instagram with provided credentials.

        DOC?>"""

        #region CODE

        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

        #endregion

    def find_followers(self) -> None:

        """<DOC

            Finds and scrolls through the followers of a similar account.

        DOC?>"""

        #region CODE

        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

        #endregion

    def follow(self) -> None:

        """<DOC

            Follows all users listed in the followers modal.

        DOC?>"""

        #region CODE

        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

        #endregion

        
#region MAIN

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

#endregion 
