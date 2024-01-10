import random
import pyautogui as pg
import time

animal=("Tere gaand mein keede paday",
"Teri Jhanten Kaat kar tere mooh par laga kar unki french beard bana doonga","Teri ma gandi rundi","Teri ma gadha ka lund choosay","Teri maa ki bimaar badboodar choot","Teri ma ki choot me hathi ka lund",
"Teri ma ki chut mai sabka lund",
"Teri maa ki phudi guy ki hai","Teri maa ka bhosda",
"Teri maa ki chute","Tere mai ki chut tere baap ka land",	
"Teri mi di kussi mey tera sarra khandan ko ghussa ker rakh doonga",
"Teri maa ki gaand ki baal mein jalaay hue"," maarey hue chipkili ki unday",
"Teri ma ki bur mein chaarpai bichhake teri bahen ko chodun",)
time.sleep(10)
for i in range(500):
    a=random.choice(animal)
    pg.write(a)
    pg.press('enter')
