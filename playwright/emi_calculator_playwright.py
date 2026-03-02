from playwright.sync_api import sync_playwright

URL = "https://emicalculator.net/home-loan-emi-calculator/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1400, "height": 900})
    page = context.new_page()

    # Open URL
    page.goto(URL, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)

    # -------------------------------
    # Home Value (HV) – 800000
    # -------------------------------
    hv_input = page.locator(
        "xpath=(//label[contains(text(),'Home Value')]/following::input)[1]"
    )
    hv_input.click()
    hv_input.press("Control+A")
    hv_input.type("800000")

    # -------------------------------
    # Margin / Down Payment (%) – 20
    # -------------------------------
    dp_input = page.locator(
        "xpath=(//label[contains(text(),'Margin')]/following::input)[1]"
    )
    dp_input.click()
    dp_input.press("Control+A")
    dp_input.type("20")

    # -------------------------------
    # Loan Amount – 60,00,000
    # -------------------------------
    loan_input = page.locator(
        "xpath=(//label[contains(text(),'Loan Amount')]/following::input)[1]"
    )
    loan_input.click()
    loan_input.press("Control+A")
    loan_input.type("6000000")

    # -------------------------------
    # Start Month & Year – Apr 2025
    # -------------------------------
    start_date_input = page.locator(
        "xpath=(//label[contains(text(),'Start Month')]/following::input)[1]"
    )
    start_date_input.click()
    start_date_input.press("Control+A")
    start_date_input.type("Apr 2025")

    # -------------------------------
    # Click "Add Prepayments"
    # -------------------------------
    add_prepayment_btn = page.locator(
        "xpath=/html/body/div[1]/div/main/article/div[3]/div/div[3]/a"
    )
    add_prepayment_btn.click()
    page.wait_for_timeout(1500)

    # -------------------------------
    # One-time only – 600,00,000
    # -------------------------------
    one_time_input = page.locator(
        "xpath=//*[@id='extraonetime']"
    )
    one_time_input.click()
    one_time_input.press("Control+A")
    one_time_input.type("60000000")

    # -------------------------------
    # Scroll Down
    # -------------------------------
    for _ in range(5):
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(300)

    # Pause to verify
    page.wait_for_timeout(5000)

    browser.close()