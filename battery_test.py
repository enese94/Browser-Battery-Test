import time
import webbrowser
import pyautogui
import random
## Change the name of the browser and add the executable on PATH
webbrowser.register('vivaldi', None, webbrowser.BackgroundBrowser(r"PATH"))

def scroll_and_wait(duration=30):
    """Scrolls up and down for a specified duration."""
    start_time = time.time()
    while time.time() - start_time < duration:
        scroll_amount = random.randint(-500, 500)
        pyautogui.scroll(scroll_amount)
        time.sleep(0.1)

def battery_test(website_list, browser_name="vivaldi"):
    """Opens a browser, navigates to websites, scrolls, and repeats indefinitely."""
    try:
        while True:
            for website in website_list:
                webbrowser.get(browser_name).open_new_tab(website)
                time.sleep(2)
                scroll_and_wait()
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(1)
    except KeyboardInterrupt:
        print("Test interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

website_list = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.wikipedia.org",
    "https://www.amazon.com",
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

battery_test(website_list)
