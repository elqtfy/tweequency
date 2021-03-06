from selenium import webdriver
import requests
import subprocess
import sys
import glob
import fnmatch
import os
import random
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

import json
from selenium.webdriver.common.keys import Keys
import time

with open('creds.json','r') as infile:
	creds = json.load(infile)

profile = webdriver.FirefoxProfile()
profile.set_preference('security.sandbox.content.level', 2)
driver = webdriver.Firefox(profile)


def tweetdeck(): 
	driver.get('https://tweetdeck.twitter.com/')
	time.sleep(1)

	log_in = driver.find_elements_by_css_selector("a")[0]
	log_in.click()

	time.sleep(1)
	
	driver.execute_script('''
    document.querySelector('.js-username-field').value=arguments[0];
    document.querySelector('.js-password-field').value=arguments[1];
    document.querySelector('button.submit.EdgeButton').click();
    ''',creds['ID'],creds['password'])	 #put your ID and password here!
	time.sleep(3)

	###comment these lines if you want to listen to pre-open tweetdeck columns### 
	###from here#################################################################
	driver.execute_script('''
	document.querySelectorAll('a.link-complex')[8].click();
    ''')
	time.sleep(1)
	driver.execute_script('''
    document.querySelectorAll('a.link-complex')[9].click();
    ''')
	time.sleep(1)
	driver.execute_script('''
    document.querySelectorAll('a.link-complex')[7].click();
    ''')
	time.sleep(1)
	driver.execute_script('''
    document.querySelectorAll('a.link-complex')[6].click();
    ''')
	time.sleep(1)
	###to here###################################################################

	driver.execute_script('''
		var mutationObserver0 = new MutationObserver(function(mutations) {
				mutations.forEach(function(mutation) {
					//console.log('0');
					new Audio('https://od.lk/s/NjZfMTMzNDQyNjFf/BassPercussion%20%28online-audio-converter.com%29.mp3').play();//Base percussion opendrive link
					//var media = new Audio('https://od.lk/s/NjZfMTMzNDQyNjFf/BassPercussion%20%28online-audio-converter.com%29.mp3');
					//const playPromise = media.play();
					//if (playPromise !== null){
					//		playPromise.catch(() => { media.play(); })
					//}
					var newCard = document.querySelectorAll('.js-chirp-container')[0].querySelectorAll('.stream-item')[0];
					newCard.style.backgroundColor = '#f4c13f';
					setTimeout(function(){newCard.style.backgroundColor='white';},3000)
				});
			});
			mutationObserver0.observe(document.querySelectorAll('.js-chirp-container')[0],{
				attributes: true,
				characterData: true,
				childList: true,
				subtree: true,
				attributeOldValue: true,
				characterDataOldValue: true
			});

			var mutationObserver1 = new MutationObserver(function(mutations) {
				mutations.forEach(function(mutation) {
					//console.log('1');
					new Audio('https://od.lk/s/NjZfMTMzNDQyNTVf/DAWN%202.mp3').play(); //Dawn file
					var newCard = document.querySelectorAll('.js-chirp-container')[1].querySelectorAll('.stream-item')[0];
					newCard.style.backgroundColor = '#3ff4ea';
					setTimeout(function(){newCard.style.backgroundColor='white';},3000)
				});
			});
			mutationObserver1.observe(document.querySelectorAll('.js-chirp-container')[1],{
				attributes: true,
				characterData: true,
				childList: true,
				subtree: true,
				attributeOldValue: true,
				characterDataOldValue: true
			});

			var mutationObserver2 = new MutationObserver(function(mutations) {
				mutations.forEach(function(mutation) {
					console.log('2');
					new Audio('https://od.lk/s/NjZfMTMzNDQyNTdf/HandDrum.mp3').play();//HANDDRUM
					var newCard = document.querySelectorAll('.js-chirp-container')[2].querySelectorAll('.stream-item')[0];
					newCard.style.backgroundColor = '#6f3ff4';
					setTimeout(function(){newCard.style.backgroundColor='white';},3000)
				});
			});
			mutationObserver2.observe(document.querySelectorAll('.js-chirp-container')[2],{
				attributes: true,
				characterData: true,
				childList: true,
				subtree: true,
				attributeOldValue: true,
				characterDataOldValue: true
			});

			var mutationObserver3 = new MutationObserver(function(mutations) {
				mutations.forEach(function(mutation) {
					console.log('3');
					new Audio('https://od.lk/s/NjZfMTMzNDQyNThf/M%26K%20Perc_3.mp3.mp3').play();//DM&K perc
					var newCard = document.querySelectorAll('.js-chirp-container')[3].querySelectorAll('.stream-item')[0];
					newCard.style.backgroundColor = '#f43f5d';
					setTimeout(function(){newCard.style.backgroundColor='white';},3000)
				});
			});
			mutationObserver3.observe(document.querySelectorAll('.js-chirp-container')[3],{
				attributes: true,
				characterData: true,
				childList: true,
				subtree: true,
				attributeOldValue: true,
				characterDataOldValue: true
			});
    ''')

tweetdeck()


