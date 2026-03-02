import pyautogui
import time
import webbrowser

# Safety
pyautogui.FAILSAFE = True

# Step 1: Open browser with URL
url = "https://emicalculator.net/home-loan-emi-calculator/"
webbrowser.open(url)

# Wait for page to load
time.sleep(8)

# -------------------------------
# NOTE:
# Use pyautogui.displayMousePosition()
# to get correct coordinates
# -------------------------------

# Step 2: Click Home Value field
pyautogui.click(x=473, y=461)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("8000000", interval=0.05)

# Step 3: Click Down Payment field
pyautogui.click(x=1422, y=451)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("6000000", interval=0.05)

# Step 5: Click Start Month & Year field
pyautogui.click(x=1431, y=570)
time.sleep(1)
pyautogui.click(x=1332,y=294)
time.sleep(1)
location = pyautogui.locateOnScreen('apr.png', confidence=0.8)
pyautogui.click(pyautogui.center(location))

# Step 6: Press Enter
pyautogui.press('enter')
pyautogui.moveTo(1749, 296, duration=0.5)

pyautogui.scroll(-600)

print("✅ EMI form filled successfully")