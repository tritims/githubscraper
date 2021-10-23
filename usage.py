import scraper
import math 
import pandas as pd
import time 
import random

# topics = ['keras', 'tensorflow', 'theano', 'pytorch', 'deep-learning', 'caffe']
topics = ['keras', 'theano']
MIN_STAR_COUNT = 500
PER_PAGE_COUNT = 100

consolidated = []
for t in topics:
    print(f"=========== working on topic: {t} ============")
    # find out number of pages
    total_items = scraper.getTotalItems(t, MIN_STAR_COUNT)
    total_pages = math.ceil(total_items/100.0)
    print(f"Total Pages: {total_pages}")
    res = []
    for page in range(total_pages):
        try:
            print(f"scraping page {page+1}...")
            time.sleep(random.random()*5)
            respo = scraper.getReposByTopic(t, MIN_STAR_COUNT, PER_PAGE_COUNT, page+1)
            res += respo
        except BaseException as e:
            print(f"Exception: {str(e)}")
            exit(0)
                # print(f"Response: {str(respo)}")
            # print(f"Response: {str(respo)}")
    pd.DataFrame(res).to_csv(f"{t}.csv")
    consolidated += res

df = pd.DataFrame(consolidated)
df.to_csv('repos_dl.csv')
print(df.head())
    