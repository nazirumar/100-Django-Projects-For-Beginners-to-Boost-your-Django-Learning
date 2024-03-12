from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to send a message to a contact
def send_whatsapp_messages(contact, messages):
    # Path to the WebDriver
    driver = webdriver.Chrome()

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    
    connected = False

    # Wait until connected
    while not connected:
        try:
            # Locate the search box
            search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
            
            connected = True
        except:
            time.sleep(1)  # Wait for 1 second if not connected yet

    # Once connected, proceed with sending messages
    try:
        search_box.click()
        search_box.send_keys(contact)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        # Locate the message input box and send messages one by one with a delay
        for message in messages:
            message_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
            message_box.click()
            message_box.send_keys(message)
            message_box.send_keys(Keys.ENTER)
            time.sleep(2)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the browser
        time.sleep(10)
        driver.quit()

# Example usage
contact_name = "F-wife"
messages = [
    
    "sweetyna",
    'myLove',
    # Add the rest of the messages here
]

send_whatsapp_messages(contact_name, messages)

