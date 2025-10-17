import pyautogui

# pyautogui.sleep(2)
# aw = pyautogui.getActiveWindow()
# print(aw.title)
# print(aw.size)

# aw = pyautogui.getActiveWindow()
# # pyautogui.moveTo(aw.left+80, aw.top+30, duration=1)
# pyautogui.click(aw.left+80, aw.top+30, duration=1)

# for w in pyautogui.getAllWindows():
#     print(w)

windows = pyautogui.getWindowsWithTitle('제목없음')
for w in windows:
    print(w)

w1 = windows[0]
if w1.isActive == False:
    w1.activate()

pyautogui.sleep(1)
# if w1.isMaximized == False:
#     w1.maximized()

