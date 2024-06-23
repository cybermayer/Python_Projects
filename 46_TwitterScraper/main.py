#region IMPORT

from twitter_bot import TwitterBot

#endregion

#region INIT

CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"

bot = TwitterBot(CHROME_DRIVER_PATH)

#endregion 

def take_input(message):

    """<DOC

        Takes user input for username, hashtag, or search query along with the number of images to download.

            PARAMS:
                    -message (str): The message to prompt the user for input.

            RETURN: tuple: A tuple containing the user input string and the number of images to download.
    
    DOC?>"""

    s = input(message)
    no_of_images = int(input("How many images do you want to download?: "))

    return (s, no_of_images)

#region MENU

print("===========================")
print("WELCOME TO IMAGE DOWNLOADER")
print("===========================")
print("1. By Username")
print("2. By Hashtag")
print("3. By Search")
choice = int(input("Enter ur choice: "))

#endregion

#region MAIN

if choice == 1:
    username, no_of_images = take_input("Enter username: ")
    bot.find_by_username(username, no_of_images=no_of_images)
elif choice == 2:
    hashtag, no_of_images = take_input("Enter hashtag: ")
    bot.find_by_hashtag(hashtag, no_of_images=no_of_images)
elif choice == 3:
    query, no_of_images = take_input("Enter search value: ")
    bot.find_by_search(query, no_of_images=no_of_images)
else:
    print("Invalid choice!")

bot.close()

#endregion
