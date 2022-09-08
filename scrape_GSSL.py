# AM 08_09_2022 
# SCRAPING / COLLATING ENTIRETY OF THREAD FOR GYRAF SSL


import requests
import csv
import time
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
import numpy as np
import os
import glob
import shutil

url = "https://groupdiy.com/threads/gssl-help-thread.47/" #GYRAF SSL URL

os.makedirs('csv_files',exist_ok=True)

page_max=433
DELAY_TIME=0.5 # delay (seconds), prevent IP block

#join all comments w space
def join_text(in_txt):
	retval=' '.join(in_txt)
	return(retval)

#separate into the date and message
def split_into_date_and_subject(in_str):
	try: 
		hash_i=in_str.index('#')
		nek_space=in_str[hash_i:].index(' ')
		split_idx=hash_i+nek_space
		retval={'date':in_str[:split_idx],
				'subject':in_str[split_idx+1:]}
	except:
		retval={'date':'',
				'subject':in_str}
	finally:
		return(retval)


#convert our date/subject dict to np array
def sd_to_np(sd):
	retval=np.array([sd['date'],sd['subject']])
	return(retval)




#run thru all pages and scrape
for p in range(page_max):	
	all_joined_text=[]
	if p==0:
		url = "https://groupdiy.com/threads/gssl-help-thread.47/"
	else:
		p+=1 #increment cos idx start @ 0
		url = f"https://groupdiy.com/threads/gssl-help-thread.47/page-{p}"

	# Headers to mimic a browser visit
	headers = {'User-Agent': 'Mozilla/5.0'}

	# Returns a requests.models.Response object
	page = requests.get(url, headers=headers)

	soup = BeautifulSoup(page.text, 'html.parser')
	domains = soup.find_all("div", class_="message-cell message-cell--main")

	texts=[list(d.stripped_strings) for d in domains]
	joined=[join_text(t) for t in texts]

	#joined=[join_text(t[3:]) for t in texts]
	joined=[j.replace("'","") for j in joined]
	joined=[j.replace("\xa0"," ") for j in joined]

	#put all joined text into list...
	for j in joined:
		all_joined_text.append(j)
	if p==0: p+=1
	

	print('coagulating to df')
	sd_s=[split_into_date_and_subject(t) for t in all_joined_text] #get date and subject of post
	sd_s=[sd_to_np(s) for s in sd_s] #turn dict to np array
	collected_sd=np.array(sd_s) #this is collected comments etc
	all_merged_comments=pd.DataFrame(collected_sd) #merge into final big
	all_merged_comments.columns=['date','message']
	all_merged_comments.to_csv(f'csv_files/page_{p}.csv',index=False) #save csv files
	print(f'done for page: {p}, saved csv')


	time.sleep(DELAY_TIME) #delay for 5 second otherwise it's going to block IP addy


#now we are merging entire .csv into one

csv_fn_list=glob.glob('csv_files/*.csv')

#gotta sort by ascending page name
#credit: https://stackoverflow.com/questions/33159106/sort-filenames-in-directory-in-ascending-order
csv_fn_list.sort(key=lambda f: int(re.sub('\D', '', f)))
csv_files=[pd.read_csv(fn) for fn in csv_fn_list] #read all in 
entire_merged_comments=pd.concat(csv_files) #concat all csv files
entire_merged_comments.to_csv('COMPILED_COMMENTS_GSSL_THREAD_GROUPDIY_08_09_2022.csv',index=False) #put in bulk collection
#delete old csv
shutil.rmtree('csv_files') 

