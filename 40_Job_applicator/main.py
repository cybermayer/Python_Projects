from selenium import webdriver  
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException  

# Define constants for LinkedIn account login and phone number
ACCOUNT_EMAIL = "YOUR LOGIN EMAIL"
ACCOUNT_PASSWORD = "YOUR LOGIN PASSWORD"
PHONE = "YOUR PHONE NUMBER"

# Path to your Chrome WebDriver executable
chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(chrome_driver_path)  
driver.get("https://www.linkedin.com/jobs/search?keywords=Cyber%20Security&location=Greater%20London&geoId=102257491&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

time.sleep(2)

#Sign in click
sign_in_button = driver.find_element_by_link_text("Sign in")  
sign_in_button.click()

time.sleep(5)

#Credential submitting
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5) 

#Collecting the listed jobs
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable") 

# Iterate through each job listing, attempt to apply if possible
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    
    #Handling exceptions
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)  
        phone = driver.find_element_by_class_name("fb-single-line-text__input") 
        if phone.text == "":
            phone.send_keys(PHONE)  
        
        submit_button = driver.find_element_by_css_selector("footer button")
        
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            
            time.sleep(2) 
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()  
            print("Complex application, skipped.")  
            continue
            
        else:
            submit_button.click()  

        time.sleep(2)  
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5) 
driver.quit()
