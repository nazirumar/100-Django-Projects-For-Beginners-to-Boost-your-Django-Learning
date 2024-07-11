import pywhatkit as kit
import schedule
import time
import pyautogui
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def send_good_morning():
    try:
        # Replace '+1234567890' with your girlfriend's phone number including country code
        phone_number = '+1234567890'
        message = 'Good Morning!'
        # Send message at a specific time (use a time a few minutes ahead for testing)
        kit.sendwhatmsg(phone_number, message, 2, 0, wait_time=2)
        logging.info(f"Good Morning message sent to {phone_number}")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")

# Schedule the message to be sent every day at 8:00 AM
schedule.every().day.at("01:48").do(send_good_morning)

def main():
    logging.info("WhatsApp Good Morning automation script started")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
