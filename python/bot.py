from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


instaSignedIn=False


def getmail():
 url2="https://temp-mail.org/en/"
 chromedriver_path = r'C:\Users\Orkideh\Downloads\chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
 webdriver = webdriver.Chrome(executable_path=chromedriver_path)
 sleep(2)
 webdriver.get(url2)
 sleep(3)
 email_temp = webdriver.find_element_by_id('mail')
 final_mail=email_temp.text
 create_insta_ac(final_mail)


   


def choose_option():
 option_user23=input("[$]Do You Want To Create A New Acoount Or Have One?[1 for yes,2 for no] : ")
 if(int(option_user23)==1):
     getmail()
     
    



def login_instapls():



 chromedriver_path = r'C:\Users\Orkideh\Downloads\chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
 webdriver = webdriver.Chrome(executable_path=chromedriver_path)
 sleep(2)
 webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
 sleep(3)

 username = webdriver.find_element_by_name('username')
 username.send_keys(final_email)
 password = webdriver.find_element_by_name('password')
 password.send_keys(insta_pass3)

 button_login = webdriver.find_element_by_css_selector('body > div > section > main > div > article > div > div > div > form > div > button > div')
 button_login.click()
 sleep(3)

 notnow = webdriver.find_element_by_css_selector('body > div > div > div > div > div > button.aOOlW.HoLwm')
 notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications


 hashtag_list = ['vojood', 'gomshodim']

#############################################
 prev_user_list = []
 # - if it's the first time you run it, use this line and comment the two below

 #prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
 #prev_user_list = list(prev_user_list['0'])

 new_followed = []
 tag = -1
 followed = 0
 likes = 0
 comments = 0

 for hashtag in hashtag_list:
     tag += 1
     webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
     sleep(5)
     first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
     first_thumbnail.click()
     sleep(randint(1,2))    
     try:        
         for x in range(1,200):
             username = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            
             if username not in prev_user_list:
                 # If we already follow, do not unfollow
                 if webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                    
                     webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                    
                     new_followed.append(username)
                     followed += 1

                     # Liking the picture
                     button_like = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                    
                     button_like.click()
                     likes += 1
                     sleep(randint(18,25))

                     # Comments and tracker
                     comm_prob = randint(1,10)
                     print('{}_{}: {}'.format(hashtag, x,comm_prob))
                     if comm_prob > 7:
                         comments += 1
                         webdriver.find_element_by_xpath('/html/body/div/div/div/div/article/div/section/span/button/span').click()
                         comment_box = webdriver.find_element_by_xpath('/html/body/div/div/div/div/article/div/section/div/form/textarea')

                         if (comm_prob < 7):
                             comment_box.send_keys('dada eyval!')
                             sleep(1)
                         elif (comm_prob > 6) and (comm_prob < 9):
                             comment_box.send_keys('Nice work :)')
                             sleep(1)
                         elif comm_prob == 9:
                             comment_box.send_keys('Nice TRACK!!')
                             sleep(1)
                         elif comm_prob == 10:
                             comment_box.send_keys('So cool! :)')
                             sleep(1)
                         # Enter to post comment
                         comment_box.send_keys(Keys.ENTER)
                         sleep(randint(22,28))

                 # Next picture
                 webdriver.find_element_by_link_text('Next').click()
                 sleep(randint(25,29))
             else:
                 webdriver.find_element_by_link_text('Next').click()
                 sleep(randint(20,26))
     # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
     except:
         continue

 for n in range(0,len(new_followed)):
     prev_user_list.append(new_followed[n])
    
 updated_user_df = pd.DataFrame(prev_user_list)
 updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
 print('Liked {} photos.'.format(likes))
 print('Commented {} photos.'.format(comments))
 print('Followed {} new people.'.format(followed))

def create_insta_ac(email0):
    
 insta_username3=input("[*] Enter Username For Insta [Good] : ")
 insta_pass3=input("[*] Enter Password For Insta : ")
 insta_fullname3=input("[*] Enter FullName For Insta : ")

 id_em='emailOrPhone'
 id_fulln='fullName'
 id_usname='username'
 id_passw='password'
 url2="https://www.instagram.com/"
 chromedriver_path = r'C:\Users\Orkideh\Downloads\chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
 webdriver = webdriver.Chrome(executable_path=chromedriver_path)
 sleep(2)
 webdriver.get(url2)
 username_insts = webdriver.find_element_by_name(id_usname)
 pass_insts = webdriver.find_element_by_name(id_passw)
 em_insts = webdriver.find_element_by_name(id_em)
 fullname_insts = webdriver.find_element_by_name(id_fulln)
 em_insts.send_keys(email0)
 fullname_insts.send_keys(insta_fullname3)
 username_insts.send_keys(insta_username3)
 pass_insts.send_keys(insta_pass3)
 


################################################################################################################################################3
choose_option()









