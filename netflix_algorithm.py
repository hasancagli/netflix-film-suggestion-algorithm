import pandas as pd 
import numpy as np

from selenium import webdriver
import time

dataset = pd.read_csv('netflix_titles.csv')

def createImdbList(dataset):
    imdbList = []

    browser = webdriver.Chrome()
    browser.get('https://www.imdb.com/')

    time.sleep(0.1)

    f = open("imdbScores.txt", "a")
    f.write('imdbScores = [')
    f.close()

    
    for i in range(dataset['title'].size):
        searchInput = browser.find_element_by_xpath('//*[@id="suggestion-search"]')
        
        searchInput.send_keys(dataset['title'][i])
        searchButton = browser.find_element_by_xpath('//*[@id="suggestion-search-button"]')
        searchButton.click()
        #time.sleep(0.02)

        try : 
            willBeClicked = browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a')
            willBeClicked.click()
            #time.sleep(0.02)
        except :
            f = open("imdbScores.txt", "a")
            f.write("0,")
            f.close()
            continue

        imdbScore = ""
        try: 
            imdbScore = browser.find_element_by_xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[2]/div/div[1]/a/div/div/div[2]/div[1]/span[1]')
        except :
            try: 
                imdbScore = browser.find_element_by_xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/strong/span')
            except : 
                imdbScore = ""
            
        if (imdbScore == ""):
            imdbList.append("")
            f = open("imdbScores.txt", "a")
            f.write("0,")
            f.close()
        else : 
            imdbList.append(imdbScore.text)
            f = open("imdbScores.txt", "a")
            f.write(imdbScore.text + ",")
            f.close()

    f = open("imdbScores.txt", "a")
    f.write("]")
    f.close()
    

createImdbList(dataset)
# print(type(dataset['title'][0]))
# print(dataset['title'].size)
