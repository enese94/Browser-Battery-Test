# Browser Battery Consumption Test Script

This Python script automates a series of web browsing actions to simulate typical user behavior and facilitate the testing of browser battery consumption. It opens a specified browser, navigates to a predefined list of websites, performs scrolling actions, and then closes each tab, repeating the process indefinitely or until manually interrupted.

## Purpose

The primary goal of this script is to provide a consistent and repeatable method for evaluating the battery efficiency of different web browsers under controlled conditions. By simulating user interaction through automated website navigation and scrolling, the script helps identify potential differences in power usage between browsers.

## Features

* **Automated Web Browsing:** Opens a web browser and navigates through a list of user-defined websites.
* **Simulated User Interaction:** Mimics user scrolling behavior with random scroll amounts to replicate realistic browsing patterns.
* **Indefinite Execution:** Runs continuously, allowing for long-term battery consumption testing.
* **Error Handling:** Includes robust error handling to prevent unexpected script termination.
* **Customizable Browser Path:** Allows users to specify the path to their browser executable, enabling the testing of various browsers.
* **Tab Management:** Automatically closes each website tab after use to prevent browser clutter and maintain consistent testing conditions.
* **Randomized Scrolling:** Incorporates randomized scrolling to emulate more realistic user interaction.

## Usage

1.  **Prerequisites:**
    * Install Python 3.x.
    * Install the `pyautogui` library: `pip install pyautogui`
2.  **Configuration:**
    * Modify the `browser_path` variable in the script to the correct path of your browser executable (e.g., Chrome, Firefox, Vivaldi).
    * Customize the `website_list` with the URLs of the websites you want to test.
3.  **Execution:**
    * Save the Python script (e.g., `battery_test.py`).
    * Open a command prompt or terminal.
    * Navigate to the directory containing the script.
    * Run the script: `python battery_test.py` (or `python3 battery_test.py`).
4.  **Interruption:**
    * To stop the script, press `Ctrl+C`.

## Important Notes

* Battery consumption results may vary significantly based on hardware, operating system, and other running applications.
* This script automates browser actions; you will need separate tools or operating system features to measure actual battery consumption.
* It is highly recommended to close all other running programs, to minimize outside interference during testing.
* For more accurate and repeatable results, consider using a headless browser with a tool like Selenium or Puppeteer.
* If you are testing multiple browsers, run the script multiple times, once per browser, while keeping all other conditions as consistent as possible.

## Author

ENESE
