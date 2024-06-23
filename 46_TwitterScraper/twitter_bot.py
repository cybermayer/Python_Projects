#region IMPORT

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlopen, Request
from selenium.webdriver.chrome.options import Options
import time
import os

#endregion

class TwitterBot:

    """<DOC

        A Twitter bot to find and download images based on hashtags, usernames, or search queries.

            METHODS:
                        - __init__ -> None
                        - find_by_hashtag -> None
                        - find_by_username -> None
                        - find_by_search -> None
                        - close -> None

    DOC?>"""

    def __init__(self, driver_path) -> None:

        """<DOC

            Initializes the TwitterBot with the specified Chrome driver path.

                PARAMETERS:
                            -driver_path (str): Path to the Chrome driver executable.

        DOC?>"""

        #region CODE

        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.headers = {

            'User-Agent': 'YOUR USER AGENT'
        }

        #endregion

    def find_by_hashtag(self, hashtag, no_of_images=10) -> None:

        """<DOC

            Finds images based on a hashtag on Twitter.

                PARAMETERS:
                            -hashtag (str): The hashtag to search for.
                            -no_of_images (int): Number of images to find (default is 10).

        DOC?>"""

        #region CODE

        url = f"https://twitter.com/hashtag/{hashtag}"
        self.__find_images_by_url(url, no_of_images)

        #endregion CODE

    def find_by_username(self, username, no_of_images=10) -> None:

        """<DOC

            Finds images based on a username on Twitter.

                PARAMETERS:
                            -username (str): The username to search for.
                            -no_of_images (int): Number of images to find (default is 10).

        DOC?>"""

        #region CODE

        url = f"https://twitter.com/{username}"
        self.__find_images_by_url(url, no_of_images)

        #endregion CODE

    def find_by_search(self, query, no_of_images=10) -> None:
    
        """<DOC

            Finds images based on a search query on Twitter.

                PARAMETERS:
                            -query (str): The search query.
                            -no_of_images (int): Number of images to find (default is 10).

        DOC?>"""

        #region CODE

        url = f"https://twitter.com/search?q={query}"
        self.__find_images_by_url(url, no_of_images)

        #endregion CODE

    def __find_images_by_url(self, url, no_of_images) -> None:

        """<DOC

            Private method to find images from a given URL on Twitter.

                PARAMETERS:
                            -url (str): The URL to search for images.
                            -no_of_images (int): Number of images to find.

        DOC?>"""

        #region CODE

        self.driver.get(url)
        time.sleep(16)
        image_links = set()
        while no_of_images > len(image_links):
            img_tags = self.driver.find_elements_by_css_selector('[aria-label="Image"] img')

            for element in img_tags:
                link = element.get_attribute('src').split('&name')[0]
                image_links.add(link)

            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            print(f"{len(image_links)} images found.")

        print("Downloading Started.")
        self.__create_directory()
        for link in image_links:
            self.__download_image(link)

        #endregion CODE

    def __create_directory(self, dir_name='Images') -> None:

        """<DOC

            Private method to create a directory for saving downloaded images.

                PARAMETERS:

                            -dir_name (str): Name of the directory (default is 'Images').

        DOC?>"""

        #region CODE

        if not os.path.isdir('Images'):
            os.mkdir("Images")

        #endregion CODE

    def __download_image(self, url) -> None:

        """<DOC

            Private method to download an image from a given URL.

                PARAMETERS:
                            -url (str): The URL of the image to download.

        DOC?>"""

        #region CODE

        file_name = os.path.basename(url).replace('?format=', '.')
        local_file = open(os.path.join("Images", file_name), 'wb')
        req = Request(url=url, headers=self.headers)
        with urlopen(req) as response:
            local_file.write(response.read())
        print(f"{file_name} is downloaded.")

        #endregion CODE

    def close(self):

        """<DOC

            Closes the Chrome driver instance.

        DOC?>"""

        #region CODE

        self.driver.close()

        #endregion CODE
