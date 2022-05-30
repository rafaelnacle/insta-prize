from requests import request
from flask import Flask, render_template, request, redirect
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
import warnings
import random


def scraping_ig(url):
    # filter deprecation warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # setup to use webdriver on repl.it
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1024, 768)

    url_ig = 'https://www.instagram.com'

    driver.get(url_ig)
    sleep(5)

    # select inputs
    input_username = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[1]/div/label/input')
    input_password = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[2]/div/label/input')

    btn_login = driver.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[3]/button')

    input_username.send_keys("")
    input_password.send_keys("")
    btn_login.click()
    sleep(5)

    try:
        btn_login_info = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button')
        btn_login_info.click()
        sleep(5)

        btn_dont_notify = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div/div[3]/button[2]')
        btn_dont_notify.click()
        sleep(5)
    except NoSuchElementException:
        print("The selector doesn't exists\n")

    # https://www.instagram.com/p/CWZTZZlsqTt/
    # url = input("Which url you want to make a raffle?: ")

    driver.get(url)
    sleep(5)

    try:
        btn_more_comments = driver.find_element_by_class_name(
            "NUiEW")
        btn_more_comments.click()

        while btn_more_comments.is_displayed():

            if btn_more_comments.is_displayed():
                btn_more_comments = driver.find_element_by_class_name(
                    "NUiEW")
                btn_more_comments.click()
                sleep(5)
            else:
                continue
    except NoSuchElementException:
        print("The selector doesn't exists\n")
    except ElementClickInterceptedException:
        print("Click intercepted\n")

    print("Loading...")
    sleep(5)

    comments = driver.find_elements_by_class_name("gElp9")
    sleep(5)

    user_list = []
    for comment in comments:
        if comment not in user_list:
            user_name = comment.find_element_by_class_name(
                "_6lAjh").text

            user_list.append(user_name)

    num_winners = request.args.get('winner')
    winner = random.choices(user_list, k=int(num_winners))

    return winner, comments
