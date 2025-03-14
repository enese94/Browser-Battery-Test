import time
import webbrowser
import pyautogui
import random
import platform
import os
import subprocess

def get_browser_path(browser_name):
    """Asks the user for the browser path if not found in common locations."""
    os_name = platform.system()
    path = None

    if os_name == "Windows":
        if browser_name == "chrome":
            path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        elif browser_name == "firefox":
            path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        elif browser_name == "vivaldi":
            path = r"C:\Users\YourUserName\AppData\Local\Vivaldi\Application\vivaldi.exe"
        elif browser_name == "edge":
            path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        elif browser_name == "opera":
            path = r"C:\Users\YourUserName\AppData\Local\Programs\Opera\opera.exe"
        elif browser_name == "brave":
            path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        elif browser_name == "zen": # example if zen browser is installed on windows
            path = r"C:\Users\YourUserName\AppData\Local\ZenBrowser\Application\zen.exe"

    elif os_name == "Darwin":
        if browser_name == "chrome":
            path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        elif browser_name == "firefox":
            path = "/Applications/Firefox.app/Contents/MacOS/firefox"
        elif browser_name == "vivaldi":
            path = "/Applications/Vivaldi.app/Contents/MacOS/Vivaldi"
        elif browser_name == "edge":
            path = "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
        elif browser_name == "opera":
            path = "/Applications/Opera.app/Contents/MacOS/Opera"
        elif browser_name == "brave":
            path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        elif browser_name == "safari":
            path = "/Applications/Safari.app/Contents/MacOS/Safari"
        elif browser_name == "zen": #example if zen browser is installed on MacOS
             path = "/Applications/ZenBrowser.app/Contents/MacOS/ZenBrowser"

    elif os_name == "Linux":
        if browser_name == "chrome":
            path = "/usr/bin/google-chrome"
        elif browser_name == "firefox":
            path = "/usr/bin/firefox"
        elif browser_name == "vivaldi":
            path = "/usr/bin/vivaldi"
        elif browser_name == "edge":
            path = "/usr/bin/microsoft-edge"
        elif browser_name == "opera":
            path = "/usr/bin/opera"
        elif browser_name == "brave":
            path = "/usr/bin/brave-browser"
        elif browser_name == "zen": #example if zen browser is installed on linux.
            path = "/usr/bin/zenbrowser"

    if path and os.path.exists(path):
        return path
    else:
        path = input(f"Enter the full path to your {browser_name} executable: ")
        if os.path.exists(path):
            return path
        else:
            return None

def open_browser(browser_path, start_url):
    """Opens the browser with the given URL."""
    try:
        subprocess.Popen([browser_path, start_url])
        return True
    except Exception as e:
        print(f"Error opening browser: {e}")
        return False

def navigate_to_url(browser_path, url):
    """Navigates the browser to the given URL using subprocess."""
    try:
        subprocess.Popen([browser_path, "--remote-debugging-port=9222", "--remote-debugging-address=127.0.0.1", url])
        return True
    except Exception as e:
        print(f"Error navigating to URL: {e}")
        return False

def scroll_and_wait(duration=30):
    """Scrolls up and down for a specified duration."""
    start_time = time.time()
    while time.time() - start_time < duration:
        scroll_amount = random.randint(-500, 500)
        pyautogui.scroll(scroll_amount)
        time.sleep(0.1)

def battery_test(website_list, browser_name, start_url):
    """Opens a browser, navigates to websites, scrolls, and repeats indefinitely."""
    browser_path = get_browser_path(browser_name)

    if not browser_path:
        print(f"Browser '{browser_name}' not found or path invalid.")
        return

    if not open_browser(browser_path, start_url):
        return

    time.sleep(5)

    try:
        while True:
            for website in website_list:
                if not navigate_to_url(browser_path, website):
                    return
                time.sleep(2)
                scroll_and_wait()
                time.sleep(1)

    except KeyboardInterrupt:
        print("Test interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

website_list = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.amazon.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.reddit.com",
    "https://www.linkedin.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.nytimes.com",
    "https://www.bbc.com",
    "https://www.cnn.com",
    "https://www.espn.com",
    "https://www.weather.com",
    "https://www.imdb.com",
    "https://www.rottentomatoes.com",
    "https://www.ebay.com",
    "https://www.craigslist.org",
    "https://www.walmart.com",
    "https://www.target.com",
    "https://www.homedepot.com",
    "https://www.lowes.com",
    "https://www.apple.com",
    "https://www.microsoft.com",
    "https://www.adobe.com",
    "https://www.oracle.com",
    "https://www.salesforce.com",
    "https://www.shopify.com",
]

browser_name = input("Enter the name of the browser you want to test (chrome, firefox, vivaldi, edge, opera, brave, safari, zen or another): ").lower()
start_url = "about:blank"
battery_test(website_list, browser_name, start_url)
