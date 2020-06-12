from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from itertools import combinations
import time

f = open("pokemons.txt","r")
f2 = open("res.txt","w")
pokemons = {}
pokemon_list = []
count = 0
for line in f.readlines():
    pokemon, level, attack, defence, stamina = line[:-1].split(" ")
    if pokemon == "muk":
        pokemon = "muk (alolan)"
    if pokemon == "mewtwo":
        pokemon = "mewtwo (Armored)"
    pokemons[pokemon]= [level,attack,defence,stamina]

pokemon_combinations = list(combinations(pokemons,3))
print(pokemons)
#op.add_argument('--headless')
driver = webdriver.PhantomJS()
driver.implicitly_wait(10)
for team in pokemon_combinations:
    driver.get("https://pvpoke.com/team-builder/")
    time.sleep(3)
    el = driver.find_element_by_xpath("/html/body/div/div/div[1]/select[1]")
    select = Select(el)
    select.select_by_value("2500")
    time.sleep(0.5)
    print(team)
    f2.write(str(team) + "\n")
    for pokemon in team:
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div/div[1]/button[1]").send_keys(Keys.ENTER)
        time.sleep(0.5)
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/input").send_keys(pokemon)
        except:
            print("error cant find")
            f2.write("error\n")
        
        driver.execute_script("$('.fields').css('display','block')")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/div[1]/input").clear()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/div[1]/input").send_keys(pokemons[pokemon][0])
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/div[1]/div/input[1]").clear()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/div[1]/div/input[2]").clear()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/div[1]/div/input[3]").clear()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/div[1]/div/input[1]").send_keys(pokemons[pokemon][1])
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/div[1]/div/input[2]").send_keys(pokemons[pokemon][2])
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[1]/div[1]/div[8]/div/div[1]/div/input[3]").send_keys(pokemons[pokemon][3])
        driver.find_element_by_class_name("button.save-poke.button").click()
    driver.find_element_by_class_name("button.rate-btn.button").send_keys(Keys.ENTER)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "threat-score"))
        )
    except:
        print("timeout error")
    finally:
        print(str(count) + " " + element.text)
        count = count+1
        f2.write(element.text + "\n")
        f2.flush()
