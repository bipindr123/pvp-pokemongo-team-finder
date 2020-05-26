from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from itertools import combinations
import time

f = open("pokemons.txt","r")
pokemons = {}
pokemon_list = []

for line in f.readlines():
    pokemon, attack, defence, stamina = line[:-1].split(" ")
    pokemons[pokemon]= [attack,defence,stamina]

pokemon_combinations = list(combinations(pokemons,3))

op = webdriver.FirefoxOptions()
#op.add_argument('--headless')
driver = webdriver.Firefox(options=op)
driver.implicitly_wait(30)
for team in pokemon_combinations:
    driver.get("https://pvpoke.com/team-builder/all/1500/mew-m-8-18-0%2Csnorlax-m-10-4-0%2Cswampert-m-0-1-3")
    time.sleep(1.5)

    for pokemon in team:
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div[1]/button[1]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/input").send_keys(pokemon)
        driver.find_element_by_class_name("button.save-poke.button").click()
    driver.find_element_by_class_name("button.rate-btn.button").click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "threat-score"))
        )
    except:
        print("timeout error")
    finally:
        print(element.text)