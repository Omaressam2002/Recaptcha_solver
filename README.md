# **Selenium CAPTCHA Interaction Task**

This project demonstrates a controlled automation task using **Selenium with Safari WebDriver**.
The objective is *not* to solve or bypass real CAPTCHA systems, but to interact with a custom test page provided for the assignment.

---

## **📌 Task Summary**

The script performs the following:

1. Opens a target URL containing a grid-based CAPTCHA-like interface.
2. Reads the textual instruction showing which object the CAPTCHA refers to.
3. Retrieves the **average brightness** value for each grid tile.
4. Clicks all tiles where the brightness value is **greater than 100**.

This assignment focuses on DOM automation and element filtering, not image recognition.

---

## **🧰 Technologies Used**

* **Python 3**
* **Selenium WebDriver**
* **Safari WebDriver** (macOS built-in)

> Ensure Safari’s *“Allow Remote Automation”* is enabled
> **Safari → Develop → Allow Remote Automation**

---

## **🚀 Running the Script**

```sh
python main.py
```

---

## **📎 Notes**

* This project is for educational and testing purposes only.
* No real CAPTCHA solving, bypassing, or security circumvention is attempted.
* Works only on macOS with Safari WebDriver enabled.

