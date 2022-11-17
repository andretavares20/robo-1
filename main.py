from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=servico)

driver.maximize_window()

driver.get("https://tipminer.com/blaze/double")

black_to_black=0
black_to_white=0
black_to_red=0
white_to_white=0
white_to_red=0
white_to_black=0
red_to_red=0
red_to_white=0
red_to_black=0

roll_black='roll black '
roll_red='roll red '
roll_white='roll white '

peido = True
cont=0

while peido==True and cont<10:

    cont = cont+1

    cor1 = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]").get_attribute("class")
    cor2 = driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]").get_attribute("class")
    print('COR1: '+str(cor1))
    print('COR2: '+str(cor2))

    if cor1 == roll_black and cor2 == roll_black:
        black_to_black = black_to_black+1
        now = datetime.now()
        print('black_to_black: '+str(now))
        time.sleep(30)
    
    elif cor1 == roll_black and cor2 == roll_white:
        black_to_white = black_to_white+1
        now = datetime.now()
        print('black_to_white: '+str(now))
        time.sleep(30)

    elif cor1 == roll_black and cor2 == roll_red:
        black_to_red = black_to_red+1
        now = datetime.now()
        print('black_to_red: '+str(now))
        time.sleep(30)

    elif cor1 == roll_white and cor2 == roll_white:
        white_to_white = white_to_white+1
        now = datetime.now()
        print('white_to_white: '+str(now))
        time.sleep(30)

    elif cor1 == roll_white and cor2 == roll_red:
        white_to_red = white_to_red+1
        now = datetime.now()
        print('white_to_red: '+str(now))
        time.sleep(30)

    elif cor1 == roll_white and cor2 == roll_black:
        white_to_black = white_to_black+1
        now = datetime.now()
        print('white_to_black: '+str(now))
        time.sleep(30)

    elif cor1 == roll_red and cor2 == roll_red:
        red_to_red = red_to_red+1
        now = datetime.now()
        print('red_to_red: '+str(now))
        time.sleep(30)

    elif cor1 == roll_red and cor2 == roll_white:
        red_to_white = red_to_white+1
        now = datetime.now()
        print('red_to_white: '+str(now))
        time.sleep(30)

    elif cor1== roll_red and cor2 == roll_black:
        red_to_black = red_to_black+1
        now = datetime.now()
        print('red_to_black: '+str(now))
        time.sleep(30)

    

print('BLACK TO BLACK: '+str(black_to_black))
print('BLACK TO WHITE: '+str(black_to_white))
print('BLACK TO RED: '+str(black_to_red))
print('WHITE TO WHITE: '+str(white_to_white))
print('WHITE TO RED: '+str(white_to_red))
print('WHITE TO BLACK: '+str(white_to_black))
print('RED TO RED: '+str(red_to_red))
print('RED TO BLACK: '+str(red_to_black))
print('RED TO WHITE: '+str(red_to_white))
        

    





