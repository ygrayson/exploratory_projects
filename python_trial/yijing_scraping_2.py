"""
Scraping code for YiJing, login to website and scrape target data
Qianbo Yin
"""

import logging
import requests
from bs4 import BeautifulSoup


def main():
    # set logging level
    logging.basicConfig(level=logging.INFO)

    # URL, login credentials metrics
    login_url = "https://www.capitaliq.spglobal.com/"
    login_server_url = "https://login.spglobal.com/oam/server/auth_cred_submit"
    dashboard_url = "https://www.capitaliq.spglobal.com/web/client?auth=inherit#dashboard"
    search_url = "https://www.capitaliq.spglobal.com/apisvcs/search-service/v3/search/query"
    username = "yujh@mit.edu"
    password = "GoodLuckJiaheng22"
    credentials = {"username": username,
                   "emailAddress": username,
                   "password": password}

    # start session to login and scrape
    with requests.Session() as sess:
        # visit login page and obtain some credentials
        # login_html = sess.get(login_url)
        # login_soup = BeautifulSoup(login_html.text, 'html.parser')

        # post login credentials
        sess.post(login_server_url, data=credentials)

        # confirm login and get search credentials
        dashboard_html = sess.get(dashboard_url)
        if dashboard_html.url == dashboard_url:
            logging.info("Login Successful!")
        # search_soup = BeautifulSoup(search_html.text, 'html.parser')

        # list for search items and results
        search_items = ["New Credit"]#, "TD Bank"]
        all_results = []

        # loop through each item and conduct the search
        for search_item in search_items:
            # prepare search payload by combining search item and credential
            search_payload = {
                "SearchToken": search_item,
                "Start": 0, 
                "Rows": 20, 
                "Catalogs": "all", 
                "Fields": "", 
                "SortType": 1, 
                "SortFields": "",
                "Filters": [""],
                "AdvFilters": ["!EntityType:(ResearchReport) AND -(NewsWireDate:[* TO 2021-07-29T00:00:00.000Z]) "],
                "RequestType": 1
            }

            # find the intended page containing target information
            search_table_res = sess.post(search_url, data=search_payload)
            print(search_table_res.url)
            print(search_table_res.text)
            with open("html/b.html", 'w') as f:
                f.write(search_table_res.text)
        #     table_soup = BeautifulSoup(search_table_res.text, 'html.parser')
        #     target_url = table_soup.find(id="ctl02__SearchGridView").tbody.find('a')['href']
        #     target_url = login_url + target_url
            
        #     # extract the intended information on target page
        #     target_html = sess.get(target_url)
        #     target_soup = BeautifulSoup(target_html.text, 'html.parser')
        #     business_des_item = target_soup.find_all("table", {"class": "cTblListBody"})[1]
        #     business_des = business_des_item.tr.td.span.text
            
        #     # append business description to all_result
        #     all_results.append(business_des)
        
        # print(search_items)
        # print(all_results)


if __name__ == '__main__':
    main()
