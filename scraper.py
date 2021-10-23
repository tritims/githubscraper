import requests

repos_url = f"https://api.github.com/search/repositories"
def getTotalItems(topic, min_star_count):
    res = getReposByTopic(topic, min_star_count, per_page_count=1, page_number=1, include_count=True)
    return res['total_count']

def getReposByTopic(topic, min_star_count, per_page_count, page_number, include_count=False):
    url = f"{repos_url}?q=topic:{topic}+stars:>{min_star_count}&per_page={per_page_count}&page={page_number}"
    # print(url)
    res = requests.get(url)
    res_dict = res.json()
    if(include_count):
        return res_dict
    else:
        try:
            return res_dict['items']
        except:
            print(f"error response: {res_dict}")


