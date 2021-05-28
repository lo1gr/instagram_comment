import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException



import numpy as np
from time import time
import os
import re
import json
from bs4 import BeautifulSoup
import sys

import logging

class GiveawayActions():
    def __init__(self, data, user, password, tag_friends):
        self.cur_time = time()
        self.data = data
        self.driver = webdriver.Chrome(ChromeDriverManager().install())   #old way: installed the latest chromedriver each time => inefficient
        # self.driver = init_driver()
        self.user = user
        self.pw = password
        self.tag_friends = tag_friends

        logger = logging.getLogger('get_free_stuff')
        # Create the Handler for logging data to a file
        logger_handler = logging.FileHandler('get_free_stuff.log', 'w')
        logger_handler.setLevel(logging.DEBUG)
        # Create a Formatter for formatting the log messages
        logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        # Add the Formatter to the Handler
        logger_handler.setFormatter(logger_formatter)
        # Add the Handler to the Logger
        logger.addHandler(logger_handler)
        logging.basicConfig(level=logging.INFO)
        self.logger = logger

        self.go_next = False
        self.users_followed = {str(self.cur_time):[]}
        self.error_count = 0 
    
    def login(self):
        """
        Logs in the user on instagram
        """
        self.driver.get('https://www.instragram.com/accounts/login/')
        try:
            self.driver.find_element_by_xpath('//*[@id="details-button"]').click()
            self.driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
        except:
            pass

        self.driver.find_element_by_xpath("//button[text()='Accept All']").click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(self.user)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.pw)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save Info']"))).click()

    def like_pic(self):
        """
        Likes a post, if post has been deleted then set go_next to True to skip to next post
        """
        # @TODO: if post has already been liked: do not like it again and close the tab
        self.logger.info("Liking post")
        # get aria-label (either "Like" or "Unlike") of svg element with class _8-yf5
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'fr66n')))
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            unique_list_comments = list(set(re.findall(r'"username":"([a-z0-9._]*?)"}',str(soup))))

            if self.user in unique_list_comments:
                self.logger.info("Already commented on post, exiting")
                self.go_next = True
                self.close_and_open_tab()
            else:
                try:
                    WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'fr66n'))).click()
                except:
                    self.go_next = True
                    self.logger.info("Post does not exist anymore")
                    self.close_and_open_tab()

        except:
            self.error_count+=1
            if self.error_count > 4:
                self.logger.warning("GOING NEXT")
                self.go_next = True
                return  
            else:
                sleep(3)
                self.logger.warning("TIMEOUT")
                self.driver.refresh()
                self.like_pic()


    def comment_pic(self):
        """
        Comments on the pic the users chosen + adds a custom addition at the end for more human-like interaction
        """
        self.logger.info("Commenting on post")

        try:
            WebDriverWait(self.driver, 5) \
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh"))).click()
            comment = (' ').join(self.tag_friends)
            # Removing emojis -> error with Chrome
            comment_addition = ['','','','','','','','',' !!!',' :) ', ' :) ', ' :) ', ' :) ', ' :) ', ' :) ', ' :) '' a must!', ' big dreams!', ' fingers crossed', " today is my lucky day"]
            index_add = np.random.randint(0,len(comment_addition))
            comment = comment + comment_addition[index_add]
            self.logger.info(comment)
            self.driver.find_element_by_class_name("Ypffh").send_keys(comment)
            sleep(0.5)
            self.driver.find_element_by_class_name("Ypffh").send_keys(Keys.ENTER) # not working?
            self.driver.find_element_by_xpath('//button[contains(text(), "Post")]').click() 

        except Exception as e:
            self.driver.refresh()
            self.error_count+=1
            self.logger.error("comment pic error: " + str(self.error_count) + " => "  + str(e))  
            if self.error_count < 4:
                self.comment_pic()
             
    
    def follow_user(self, caption, username):
        """
        Follows user who posted + all users tagged in post
        """
        # follow this first user:
        to_follow = self.extract_accounts_to_follow(caption)
        self.logger.info("Following users")
        # following user who posted
        try:
            self.driver.find_element_by_xpath("//button[text()='Follow']").click()
            self.logger.info("Following : " + username)
            # TODO: append here username of user who posted
            self.users_followed[str(self.cur_time)].append(username)
        except:
            self.logger.info("User who posted already followed")
            self.users_followed[str(self.cur_time)].append(username)
        # follow the other users tagged in the post:
        for el in to_follow:
            sleep(np.random.uniform(1.5,3))
            try:
                self.open_and_switch_to_tab('https://www.instragram.com/'+el)
                sleep(2)
                self.driver.find_element_by_xpath("//button[text()='Follow']").click()
                self.users_followed[str(self.cur_time)].append(el)
                self.logger.info("Followed: " + str(username))
                self.close_and_open_tab()
            except:
                self.logger.info("User already followed: " + str(username))
                self.users_followed[str(self.cur_time)].append(el)
                self.close_and_open_tab()
                continue
             
    def extract_accounts_to_follow(self, caption):
        """
        extract accounts to follow, meaning accounts tagged in a caption. 
        Returns:
            [list]: [list of usernames to follow]
        """
        accounts_to_follow = re.findall("@([a-z0-9_.]*)", caption)
        # get list of unique users
        accounts_to_follow = list(set(accounts_to_follow))
        return accounts_to_follow
    
    def unfollow(self):
        """
        Unfollows users after 10 days
        """
        with open('users_followed.json') as json_file:
            data = json.load(json_file)

        list_keys = list(data.keys())

        # unfollow after 10 days
        list_to_unfollow = [k for k in list_keys if time()-int(k)>864000]
        
        if len(list_to_unfollow) > 0:
            for el in list_to_unfollow:
                for user in data[el]:
                    self.open_and_switch_to_tab("https://www.instagram.com/"+user)
                    sleep(1)
                    try:
                        self.driver.refresh()
                        sleep(1.5)
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click()
                        sleep(0.5)
                        self.driver.find_element_by_xpath("//button[text()='Unfollow']").click()
                    except Exception as e:
                        self.logger.error("Exception unfollow is: " + str(Exception))
                        continue
                    
                    self.close_and_open_tab()

                # remove the timestamp of unfollowed users
                del data[el]
                with open('users_followed.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)


    def action(self, shortcode, caption, username):
        """
        Performs the following actions on an instagram post:
        - Like
        - Comment
        - Follow
        """
        self.logger.info(self.data)
        self.open_and_switch_to_tab('https://www.instragram.com/p/'+self.data)
        sleep(np.random.uniform(30,40))
        self.like_pic() 
        sleep(np.random.uniform(2,4))
        if not self.go_next:
            self.comment_pic()
            sleep(np.random.uniform(10,30))
            self.follow_user(caption, username)
            sleep(np.random.uniform(1,3))
            self.close_and_open_tab()
    
    def comment(self):
        """
        Performs the following actions on an instagram post:
        - Comment
        """
        self.logger.info(self.data)
        self.open_and_switch_to_tab('https://www.instragram.com/p/'+self.data)
        sleep(np.random.uniform(5,30))
        self.comment_pic()
        sleep(np.random.uniform(1,3))
        self.close_and_open_tab()
        
    
    def launch(self):
        """
        Lauching the pipeline. Keeping track of the users followed in a json file
        """
        self.logger.info("LETS WIN SOME GOODIES!")

        try:
            self.login()
            count = 0

            while True:
                if count!=0 and count%10==0:
                    sleep(np.random.uniform(30,90))
                count+=1
                self.comment()
                sleep(np.random.uniform(5,20))

                if time()-self.cur_time > 3600:
                    self.logger.warning("Raising exception, too long")
                    raise Exception

        except Exception as e:
            self.logger.warning(f"Error: {e}")
            self.logger.info(f"commented {count} times!")
        
        
        # with open('stats.json', 'w') as outfile:
        #     json.dump(stats, outfile, indent=4)
        #     outfile.close()

    def open_and_switch_to_tab(self, url):
        """
        Opens a new tab and switches to it (for faster performance)
        """
        handles = self.driver.window_handles
        self.driver.execute_script(f"window.open('{url}');")
        # index based
        self.driver.switch_to.window(self.driver.window_handles[len(handles)])

    def close_and_open_tab(self, tab_index=0):
        """
        Closes a specific tab
        """
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[tab_index])
        