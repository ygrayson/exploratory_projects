"""
Scraping code for YiJing, login to website and scrape target data
Qianbo Yin
"""

import logging
import pandas as pd
import requests
from bs4 import BeautifulSoup


def main():
    # set logging level
    logging.basicConfig(level=logging.INFO)

    # URL, login credentials metrics
    login_url = "https://www.capitaliq.com/"
    login_server_url = "https://login.spglobal.com/oam/server/auth_cred_submit"
    dashboard_url = "https://www.capitaliq.com/CIQDotNet/my/dashboard.aspx"
    search_url = "https://www.capitaliq.com/CIQDotNet/Search/Search.aspx"
    username = "yujh@mit.edu"
    password = "GoodLuckJiaheng22"
    credentials = {"__EVENTTARGET": "",
                   "__EVENTARGUMENT": "",
                   "__VIEWSTATE": None,
                   "__VIEWSTATEGENERATOR": "806EEE24",
                   "__EVENTVALIDATION": None,
                   "captchaValidated": 0,
                   "username": username,
                   "password": password,
                   "PersistentLogin": "false"}

    # start session to login and scrape
    with requests.Session() as sess:
        # visit login page and obtain some credentials
        login_html = sess.get(login_url)
        logging.info(login_html.ok)
        login_soup = BeautifulSoup(login_html.text, 'html.parser')
        credentials["__VIEWSTATE"] = login_soup.find(id="__VIEWSTATE")['value']
        credentials["__VIEWSTATEGENERATOR"] = login_soup.find(id="__VIEWSTATEGENERATOR")['value']
        credentials["__EVENTVALIDATION"] = login_soup.find(id="__EVENTVALIDATION")['value']

        # post login credentials
        sess.post(login_server_url, data=credentials)

        # confirm login and get search credentials
        search_html = sess.get(search_url)
        if search_html.url == search_url:
            logging.info("Login Successful!")
        search_soup = BeautifulSoup(search_html.text, 'html.parser')

        # list for search items and results
        df = pd.read_csv('html/original_data.csv')
        search_items = df['lender_norm1']
        all_status = []
        all_business_des = []

        # loop through each item and conduct the search
        for search_item in search_items:
            # prepare search payload by combining search item and credential
            search_payload = {
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": search_soup.find(id="__VIEWSTATE")['value'],
                "__VIEWSTATEGENERATOR": search_soup.find(id="__VIEWSTATEGENERATOR")['value'],
                "__EVENTVALIDATION": search_soup.find(id="__EVENTVALIDATION")['value'],
                "SearchText": search_item,
                "_SearchButton.x": 0,
                "_SearchButton.y": 0,
                "_ScopeSelector$_SearchScope": "Profiles"
            }

            # find the intended page containing target information
            search_table_res = sess.post(search_url, data=search_payload)
            table_soup = BeautifulSoup(search_table_res.text, 'html.parser')
            try:
                target_url = table_soup.find(id="ctl02__SearchGridView").tbody.find('a')['href']
                target_url = login_url + target_url
            except:
                all_status.append("")
                all_business_des.append("")
                continue
            
            # extract the intended information on target page
            target_html = sess.get(target_url)
            target_soup = BeautifulSoup(target_html.text, 'html.parser')
            try:
                business_des_item = target_soup.find_all("table", {"class": "cTblListBody"})[1]
                business_des = business_des_item.tr.td.span.text
            except:
                business_des = ""
            try:
                form_item = target_soup.find(id="frmMain").find_all("tr", {"class": "cTblRowBG"})[0]
                if form_item.b.text == "Status:":
                    status = form_item.findChildren()[2].text
                else:
                    status = ""
            except:
                status = ""
            
            # append business description to all_result
            all_business_des.append(business_des)
            all_status.append(status)

            # logging
            logging.info("Scraping complete for " + str(search_item))
        
        df['status'] = all_status
        df['business description'] = all_business_des
        df.to_csv('html/final_data.csv')
        # print(search_items)
        # print(all_status)
        # print(all_business_des)


if __name__ == '__main__':
    main()
