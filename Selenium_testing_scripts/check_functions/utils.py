from helium import *
from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd
import re

sc_testcases = [
    "qabed_scorecard_us_1", "qabed_scorecard_us_2", "qabed_scorecard_us_3", "qabed_scorecard_us_4",
    "qabed_scorecard_intl_1", "qabed_scorecard_intl_2", "qabed_scorecard_global_1", "qabed_scorecard_global_2"
]

pro_q2_testcases = [
    "qabed_propensity_us_1", "qabed_propensity_us_2", "qabed_propensity_us_3", "qabed_propensity_us_4",
    "qabed_propensity_us_5", "qabed_propensity_us_6", "qabed_propensity_us_7", "qabed_propensity_us_8",
    "qabed_propensity_us_9", "qabed_propensity_us_10" , "qabed_propensity_intl_1", "qabed_propensity_intl_2",
    "qabed_propensity_intl_3", "qabed_propensity_intl_4",
    "qabed_propensity_intl_5", "qabed_propensity_intl_6", "qabed_propensity_intl_7", "qabed_propensity_intl_8",
    "qabed_propensity_intl_9", "qabed_propensity_intl_10"
]
cla_testcases = ["qabed_cla_us_1", "qabed_cla_us_2", "qabed_cla_us_3", "qabed_cla_us_4",
                 "qabed_cla_intl_1", "qabed_cla_intl_2"]



# def get_soup(url):
#     go_to(url)
#     wait_until(Text("Model Coefficients").exists)
#     page = get_driver().page_source
#     soup = BeautifulSoup(page, features="lxml")
#     return soup

def extract_cards(soup):
    cards = soup.find_all("div", {"class": "wgt-card"})
    return cards

def check_tables(card, num=1):
    tables = card.find_all("table")

    if len(tables) == num:
        return True
    else:
        return False

def check_link(card, num=1):
    links = card.find_all("a")
    try:
        if len(links) == num:
            return True
    except:
        return False
    
def check_img(card, num=1):
    imgs = card.find_all("img")
    try:
        if len(imgs) == num:
            return True
    except:
        return False

def check_version(version, num=1):
    version = version.find_all("pre")
    try:
        if len(version) == num:
            return True
    except:
        return False
    
def check_status(customer_name):

    # enter customer_name to search
    go_to("https://analyticsstudio-mlflows-dev.aas.dnb.net/#/wfeList")
    time.sleep(10)
    try:
        write(customer_name, into=S("//input"))
    except:
        write(customer_name, into=S("//input"))
    press(ENTER)
    
    # find the fire job id and return tuple
    time.sleep(5)
    model_name = Text(below=Text("MODEL NAME")).value
    fire_id = Text(below=Text("ID")).value
    status = Text(below=Text("STATUS")).value
    
    # if the status is still running return False else restun a tuple to show the fire_id and status
    if status == "Running":
        return False
    else:
        return {"model_name": model_name, "customer_name": customer_name, "fire_id": fire_id, "status": status}
    
def get_soup(result):
    url = "https://analyticsstudio-mlflows-dev.aas.dnb.net/#/view-workflow-result/" + result['fire_id']
    go_to(url)
    go_to(url)
    time.sleep(10)
    page = get_driver().page_source
    soup = BeautifulSoup(page, features="lxml")
    return soup

def scorecard_ui(soup):
    
    cards = extract_cards(soup)
    
    result = {}
    
    if "intl_2" not in test['customer_name']:
        para, url, version, report1, report2, chart = cards

        result['para'] = check_tables(para, 1)
        result['url'] = check_link(url, 1)
        result['version'] = check_version(version, 1)
        result['report1'] = check_tables(report1, 3)
        result['report2'] = check_tables(report2, 7)
        result['chart'] = check_img(chart, 1)
    else:
        para, url, version, warning, report_wfss1, report_wfss2,\
        chart_wfss, report_wofss1, report_wofss2, chart_wofss = cards
        
        result['para'] = check_tables(para, 1)
        result['url'] = check_link(url, 1)
        result['version'] = check_version(version, 1)
        result['report_wfss1'] = check_tables(report_wfss1, 3)
        result['report_wfss2'] = check_tables(report_wfss2, 7)
        result['chart_wfss'] = check_img(chart_wfss, 1)
        result['report_wofss1'] = check_tables(report_wofss1, 3)
        result['report_wofss2'] = check_tables(report_wofss2, 7)
        result['chart_wofss'] = check_img(chart_wofss, 1)
    return result

def data_check1(soup):
    info = soup.select("h3#data-processing-and-bad-rates")[0].find_all_next("p")[:3]
    return any([i.text.split(" :- ")[1].strip("% ").replace(".", "").isdigit() for i in info])

def data_check2(soup):
    df = pd.read_html(str(soup.find_all("table")[1]))[0]
    one = (df[df.columns[2]] == "0.00").any()
    two = df[df.columns[2]].isna().any()
    three = (df[df.columns[3]] == "0.00%").any()
    four = df[df.columns[3]].isna().any()
    return not one and not two and not three and not four

def data_check3(soup):
    df = pd.read_html(str(soup.find_all("table")[2]))[0]
    
    return not df[df.columns[1]].isna().any()

def data_check4(soup):
    df = pd.read_html(str(soup.find_all("table")[3]))[0]
    
    one = any(df[df.columns[-1]].isna())
    two = any(df[df.columns[-2]].isna())
    return not one and not two

def data_check5(soup):
    df = pd.read_html(str(soup.find_all("table")[6]))[0]
    one = np.all(df.values == 0)
    two = np.all(df.isna())
    return not one and not two

def data_check6(soup):
    df = pd.read_html(str(soup.find_all("table")[7]))[0]
    one = np.all(df.loc[:, df.columns != "max_ks"].values == 0)
    two = np.all(df.loc[:, df.columns != "max_ks"].isna())
    return not one and not two

def data_check7(soup):
    df = pd.read_html(str(soup.find_all("table")[8]))[0]
    one = np.all(df.loc[:, df.columns != "max_ks"].values == 0)
    two = np.all(df.loc[:, df.columns != "max_ks"].isna())
    return not one and not two

def data_check8(soup):
    df = pd.read_html(str(soup.find_all("table")[10]))[0]
    one = np.all(df.values == 0)
    two = np.all(df.isna())
    return not one and not two

def scorecard_data(soup):
    result = {}
    result["data_1"] = data_check1(soup) or False
    result["data_2"] = data_check1(soup) or False
    result["data_3"] = data_check1(soup) or False
    result["data_4"] = data_check1(soup) or False
    result["data_5"] = data_check1(soup) or False
    result["data_6"] = data_check1(soup) or False
    result["data_7"] = data_check1(soup) or False
    result["data_8"] = data_check1(soup) or False
    result["data_9"] = data_check1(soup) or False
    return result
 
def pro_data_check1(soup):
    df = pd.read_html(str(soup.find_all("table")[1]))[0]
    return np.all(~df.isna())

def pro_data_check2(soup):
    df = pd.read_html(str(soup.find_all("table")[2]))[0]
    return np.all(~df.isna())

def pro_data_check3(soup):
    df = pd.read_html(str(soup.find_all("table")[3]))[0]
    return np.all(~df.drop("max_ks", axis=1).isna())

def pro_data_check4(soup):
    df = pd.read_html(str(soup.find_all("table")[4]))[0]
    return np.all(~df.isna())

def pro_data_check5(soup):
    df = pd.read_html(str(soup.find_all("table")[0]))[0]
    if "USA" in pd.read_html(str(soup.find_all("table")[0]))[0].iloc[:,1].values:
        addressable = soup.findAll(text=re.compile("State for US"))[0]
    elif "INTL" in pd.read_html(str(soup.find_all("table")[0]))[0].iloc[:,1].values:
        addressable = soup.findAll(text=re.compile("Country for INTL"))[0]
    return len(addressable) != 0
        
def pro_data_check6(soup):
    df = pd.read_html(str(soup.find_all("table")[4]))[0]
    return np.all(~df.iloc[:,2].isna())

def propensity_data(soup):
    result = {}
    result["data_1"] = pro_data_check1(soup) or False
    result["data_2"] = pro_data_check2(soup) or False
    result["data_3"] = pro_data_check3(soup) or False
    result["data_4"] = pro_data_check4(soup) or False
    result["data_5"] = pro_data_check5(soup) or False
    return result

def propensity_ui(soup):
    result = {}
    cards = extract_cards(soup)
    para, url, version, report, records, table = cards
    result["para"] = check_tables(para)
    result["url"] = check_link(url)
    result["version"] = check_version(version)
    result["report"] = check_tables(report, 4) and check_img(report)
    result["records"] = check_tables(records, 2)
    return result

def propensity_beta_ui(soup):
    result = {}
    cards = extract_cards(soup)
    para, url, version, report, link = cards
    result["para"] = check_tables(para)
    result["url"] = check_link(url)
    result["version"] = check_version(version)
    result["report"] = check_tables(report, 4) and check_img(report)
    result["records"] = check_link(link)
    return result

def propensity_beta_data(soup):
    result = {}
    result["data_1"] = pro_data_check1(soup) or False
    result["data_2"] = pro_data_check2(soup) or False
    result["data_3"] = pro_data_check3(soup) or False
    result["data_4"] = pro_data_check6(soup) or False
    result["data_5"] = pro_data_check5(soup) or False
    return result

def cpi_table_check(table):
    df = pd.read_html(str(table))[0]
    return np.all(~df.isna())

def check_table_size(table, a, b):
    df = pd.read_html(str(table))[0]
    return df.shape == (a,b)

def cpi_data(soup):
    result = {}
    para, job, report, cumu, customer, opt_table = extract_cards(soup)
    summary, conservative, moderate, aggressive, color = report.find_all("table")
    result["data_1"] = cpi_table_check(summary)
    result["data_2"] = cpi_table_check(conservative)
    result["data_3"] = cpi_table_check(moderate)
    result["data_4"] = cpi_table_check(aggressive)
    result["data_5"] = cpi_table_check(color)
    return result

def cpi_ui(soup):
    result = {}
    para, job, report, cumu, customer, opt_table = extract_cards(soup)
    summary, conservative, moderate, aggressive, color = report.find_all("table")
    result["summary"] = check_table_size(summary, 6, 6)
    result["conservative"] = check_table_size(conservative, 5, 7)
    result["moderate"] = check_table_size(moderate, 5, 7)
    result["aggressive"] = check_table_size(aggressive, 5, 7)
    result["color"] = check_table_size(color, 5, 1)
    return result

def automl_ui(soup):
    result = {}
    cards = extract_cards(soup)
    para, job, metric, iteration = cards
    if "regression" in str(soup):
        result["metric"] = check_tables(metric, 4)
        result["iteration"] = check_tables(iteration, 2)
    else:
        result["metric"] = check_tables(metric, 6)
        result["iteration"] = check_tables(iteration, 3)
    return result

def automl_data(soup):
    result = {}
    cards = extract_cards(soup)
    para, job, metric, iteration = cards
    if "regression" in str(soup):
        lgb_metrics, lgb_bst, xgb_metrics, xgb_bst = metric.find_all("table")
        lgb_iter, xgb_iter = iteration.find_all("table")
        result["lgb_metrics"] = cpi_table_check(lgb_metrics)
        result["xgb_metrics"] = cpi_table_check(xgb_metrics)
        result["lgb_bst"] = cpi_table_check(lgb_bst)
        result["xgb_bst"] = cpi_table_check(xgb_bst)
        result["lgb_iter"] = cpi_table_check(lgb_iter)
        result["lgb_iter"] = cpi_table_check(lgb_iter)
        
    else:
        cat_metrics, cat_bst, lgb_metrics, lgb_bst, xgb_metrics, xgb_bst = metric.find_all("table")
        cat_iter, lgb_iter, xgb_iter = iteration.find_all("table")
        result["cat_metrics"] = cpi_table_check(cat_metrics)
        result["lgb_metrics"] = cpi_table_check(lgb_metrics)
        result["xgb_metrics"] = cpi_table_check(xgb_metrics)
        result["cat_bst"] = cpi_table_check(cat_bst)
        result["lgb_bst"] = cpi_table_check(lgb_bst)
        result["xgb_bst"] = cpi_table_check(xgb_bst)
        result["cat_iter"] = cpi_table_check(cat_iter)
        result["lgb_iter"] = cpi_table_check(lgb_iter)
        result["lgb_iter"] = cpi_table_check(lgb_iter)
    return result

def cla_ui(soup):
    result = {}
    cards = extract_cards(soup)
    if "qabed_cla_intl_2" not in str(soup):
        para, url, version, report1, report2, report3 = cards
        result["para"] = check_tables(para)
        result["url"] = check_link(url)
        result["version"] = check_version(version)
        result["report1"] = check_tables(report1, 3)
        result["report2"] = check_tables(report2, 7)
        result["report3"] = check_tables(report3, 9)
    else:
        para, url, version, warning, report1, report2, report3, report4, report5, report6 = cards
        result["para"] = check_tables(para)
        result["url"] = check_link(url)
        result["version"] = check_version(version)
        result["report1"] = check_tables(report1, 3)
        result["report2"] = check_tables(report2, 7)
        result["report3"] = check_tables(report3, 3)
        result["report4"] = check_tables(report4, 7)
        result["report5"] = check_tables(report5, 9)
        result["report6"] = check_tables(report6, 9)
    return result

def cla_data(soup):
    result = {}
    cards = extract_cards(soup)
    if "qabed_cla_intl_2" not in str(soup):
        para, url, version, report1, report2, report3 = cards
        tables = report3.find_all("table")
        for i, table in enumerate(tables):
            df = pd.read_html(str(table))[0]
            result["table_" + str(i)] = np.all(~df.isna())
        
    else:
        para, url, version, warning, report1, report2, report3, report4, report5, report6 = cards
        
        tables = report5.find_all("table")
        tables = tables + report6.find_all("table")
        for i, table in enumerate(tables):
            df = pd.read_html(str(table))[0]
            if i == 15:
                result["table_" + str(i)] = np.all(~df.xs("mean", level=1, axis=1).isna())
            else:
                result["table_" + str(i)] = np.all(~df.isna())

    return result