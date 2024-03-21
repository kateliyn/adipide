def last_tab(driver):
    """
    Switch to the last tab in the current window.

    Args:
        driver: The WebDriver instance.
    """
    driver.switch_to.window(driver.window_handles[-1])

