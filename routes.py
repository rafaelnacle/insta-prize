from raffle import scraping_ig

from requests import request
from flask import Flask, render_template, request, redirect
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


def routes():
    app = Flask("InstaPrize")

    @app.route('/')
    def home():

        return render_template('index.html')

    @app.route("/result")
    def result():

        post_url = request.args.get('url')
        winners_id = request.args.get('winner')

        winners, comments = scraping_ig(post_url)

        return render_template('result.html', winners=winners, comments=comments)

    app.run(host="0.0.0.0")
