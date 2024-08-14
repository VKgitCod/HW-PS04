import time
import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

flag = True

while flag:

    request = input("Введите запрос для Википедии: ")

    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

    assert "Википедия" in browser.title

    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(request)
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    a = browser.find_element(By.LINK_TEXT, request)
    a.click()

    choice = input("Введите:\n"
          "p - чтобы листать параграфы текущей статьи\n"
          "n - чтобы перейти на одну из связанных страниц \n"
          "q - чтобы выйти \n")

    if choice == "p":

        paragraphs = browser.find_elements(By.TAG_NAME, "p")

        for paragraph in paragraphs:
            print(paragraph.text)
            next_p = input("\n Если хотите прочитать следующий параграф нажмите - p \n"
                           "   Чтобы выйти нажмите любую клавишу \n")
            if next_p != "p":
                break

    elif choice == "n":

        hatnotes = []

        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)

        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)

        paragraphs = browser.find_elements(By.TAG_NAME, "p")

        for paragraph in paragraphs:
            print(paragraph.text)
            next_p = input("\n Если хотите прочитать следующий параграф нажмите - p \n"
                           "   Чтобы выйти нажмите любую клавишу \n")
            if next_p != "p":
                break

    else:
        flag = False


