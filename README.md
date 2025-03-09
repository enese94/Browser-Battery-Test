# Browser Battery Consumption Test Script

This Python script automates web browsing actions to simulate typical user behavior and facilitate the testing of browser battery consumption within a single tab. It opens a specified browser, navigates to a predefined list of websites within the same tab, performs scrolling actions, and repeats the process indefinitely or until manually interrupted.

## Purpose

The primary goal of this script is to provide a consistent and repeatable method for evaluating the battery efficiency of different web browsers under controlled conditions, focusing on single-tab navigation. By simulating user interaction through automated website navigation and scrolling within a single browser tab, the script aims to provide accurate data regarding browser power usage.

## Features

* **Automated Single-Tab Web Browsing:** Opens a specified web browser and navigates through a list of user-defined websites, all within the same tab.
* **Simulated User Interaction:** Mimics user scrolling behavior with random scroll amounts to replicate realistic browsing patterns.
* **Indefinite Execution:** Runs continuously, allowing for long-term battery consumption testing.
* **Error Handling:** Includes robust error handling to prevent unexpected script termination.
* **Customizable Browser Path:** Allows users to specify the path to their browser executable, enabling the testing of various browsers.
* **Cross-Platform Compatibility:** Designed to function on Windows, macOS, and Linux operating systems.
* **Randomized Scrolling:** Incorporates randomized scrolling to emulate more realistic user interaction.
* **Remote Debugging:** Uses remote debugging to navigate through websites on the same tab.
* **User-Friendly Browser Selection:** Prompts the user to input the desired browser and its path.

## Pre-requisites

* **Python 3.x:** Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).
* **pyautogui Library:** Install the `pyautogui` library using pip: `pip install pyautogui`.
* **A web browser:** Chrome, Firefox, Vivaldi, or any other browser you want to test.
* **Remote Debugging:** Some browsers may require enabling remote debugging.

## Program Functions

* **`get_browser_path(browser_name)`:**
    * Attempts to locate the browser executable path based on the operating system and browser name.
    * If the path is not found in common locations, it prompts the user to enter the full path.
    * Returns the executable path or `None` if invalid.
* **`open_browser(browser_path, start_url)`:**
    * Opens the specified browser with the given starting URL using `subprocess.Popen()`.
    * Returns `True` if successful, `False` otherwise.
* **`navigate_to_url(browser_path, url)`:**
    * Navigates to the given URL within the browser's existing tab using remote debugging via `subprocess.Popen()`.
    * Returns `True` if successful, `False` otherwise.
* **`scroll_and_wait(duration=30)`:**
    * Simulates user scrolling by randomly scrolling up and down for a specified duration.
    * Uses `pyautogui.scroll()` for scrolling and `time.sleep()` for delays.
* **`battery_test(website_list, browser_name, start_url)`:**
    * Orchestrates the battery test process.
    * Gets the browser path, opens the browser, navigates to each website, scrolls, and repeats.
    * Handles errors and user interruptions.

## How to Run

### Windows

1.  **Install Python and pyautogui:**
    * Download and install Python 3.x from [python.org](https://www.python.org/).
    * Open Command Prompt or PowerShell and run `pip install pyautogui`.
2.  **Save the script:**
    * Save the Python script as `battery_test.py`.
3.  **Run the script:**
    * Open Command Prompt or PowerShell, navigate to the script's directory, and run `python battery_test.py`.
4.  **Enter Browser Information:**
    * The script will ask for the browser name, and if needed the path.
5.  **Interrupt the test:**
    * Press `Ctrl+C` to stop the script.

### Linux

1.  **Install Python and pyautogui:**
    * Use your distribution's package manager to install Python 3 and pip.
    * Open a terminal and run `pip3 install pyautogui`.
2.  **Save the script:**
    * Save the Python script as `battery_test.py`.
3.  **Run the script:**
    * Open a terminal, navigate to the script's directory, and run `python3 battery_test.py`.
4.  **Enter Browser Information:**
    * The script will ask for the browser name, and if needed the path.
5.  **Interrupt the test:**
    * Press `Ctrl+C` to stop the script.

### macOS

1.  **Install Python and pyautogui:**
    * Install Python 3.x using Homebrew or from [python.org](https://www.python.org/).
    * Open Terminal and run `pip3 install pyautogui`.
2.  **Save the script:**
    * Save the Python script as `battery_test.py`.
3.  **Run the script:**
    * Open Terminal, navigate to the script's directory, and run `python3 battery_test.py`.
4.  **Enter Browser Information:**
    * The script will ask for the browser name, and if needed the path.
5.  **Interrupt the test:**
    * Press `Ctrl+C` to stop the script.

## Important Notes

* Battery consumption results may vary depending on hardware, operating system, and other running applications.
* This script automates browser actions; you will need separate tools or operating system features to measure actual battery consumption.
* It is highly recommended to close all other running programs to minimize outside interference during testing.
* Remote debugging must be allowed by the browser.
* If the browser path is incorrect, the script will not function.
