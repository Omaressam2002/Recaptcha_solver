Selenium CAPTCHA Interaction Task
This project uses Selenium with Safari WebDriver to interact with a simple CAPTCHA-style grid.
The goal is not to solve reCAPTCHA, but to complete a controlled assignment page.
Overview
Open a given URL containing a CAPTCHA-like grid.
Read the instruction (object to detect).
Each grid cell has an average brightness value.
Click all cells with brightness > 100.
No real CAPTCHA solving or bypassing is involved.
Tech
Python
Selenium (Safari WebDriver)
How It Works
Launch Safari WebDriver.
Load the provided URL.
Loop through grid elements and read their brightness value.
Click every cell above the threshold (100).
End or submit depending on the assignment.
Run
python main.py
Notes
Safari’s WebDriver must be enabled in Safari > Develop menu.
This task is for learning and automation practice only.
