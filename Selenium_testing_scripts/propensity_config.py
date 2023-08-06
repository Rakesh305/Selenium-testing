import os
cwd = os.getcwd()

# intl
config1 = { "year": 2022, "month": 2, 
           "market": "INTERNATIONAL",
           "file": cwd + "/qa_files/propensity_intl.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_intl_1',
            "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",
               
           "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "", "o_esic": ""}

config2 = { "year": 2022, "month": 2, 
           "market": "INTERNATIONAL",
           "file": cwd + "/qa_files/propensity_intl.csv",
               "iter": 5, "deciles": 2, 'name': 'qabed_propensity_intl_2',
            "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "",
               
           "o_ind": [], "o_emp": [], "o_cty": "GERMANY", "o_sic": "",  "o_esic": ""}

config3 =   { "year": 2022, "month": 2, 
           "market": "INTERNATIONAL",
           "file": cwd + "/qa_files/propensity_intl.csv",
               "iter": 5, "deciles": 2, 'name': 'qabed_propensity_intl_3',        
             "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",
               
           "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "7379,5045",  "o_esic": ""}

config4 =     { "year": 2022, "month": 2, "market": "INTERNATIONAL",
           "file": cwd + "/qa_files/propensity_intl.csv",
               "iter": 5, "deciles": 2, 'name': 'qabed_propensity_intl_4', 
            "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "7379,5045", "i_esic": "",
               
           "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "",  "o_esic": ""}

config5 =      { "year": 2022, "month": 2, "market": "INTERNATIONAL",
           "file": cwd + "/qa_files/propensity_intl.csv",
               "iter": 5, "deciles": 3, 'name': 'qabed_propensity_intl_5', 
            "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",
               
           "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "",  "o_esic": ""}

config6 =      {  "year": 2022, "month": 2, "market": "INTERNATIONAL",
           "file": cwd + "/qa_files/propensity_intl.csv",
               "iter": 5, "deciles": 2, 'name': 'qabed_propensity_intl_6', 
            "i_ind": [], "i_emp": [
            "1 - 9",
            "10 - 49",
            "50 - 99"
        ], "i_cty": [], "i_sic": "", "i_esic": "",
               
           "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "",  "o_esic": ""}

config7 =      {  "year": 2022, "month": 2, "market": "INTERNATIONAL",
           "file": cwd + "/qa_files/propensity_intl.csv",
               "iter": 5, "deciles": 2, 'name': 'qabed_propensity_intl_7', 
            "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",
               
           "o_ind": ["Mining",
            "Public Administration",
            "Retail Trade",
            "Services",
            "Transportation, Communication",
            "Wholesale Trade"], "o_emp": [], "o_cty": [], "o_sic": "",  "o_esic": ""}

config8 =      {  "year": 2022, "month": 2, "market": "INTERNATIONAL",
           "file": cwd + "/qa_files/propensity_intl.csv",
               "iter": 5, "deciles": 2, 'name': 'qabed_propensity_intl_8', 
            "i_ind": ["Transportation, Communication","Wholesale Trade",], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",
               
           "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "",  "o_esic": ""}

config9 =      {  "year": 2022, "month": 2, "market": "INTERNATIONAL",
           "file": cwd + "/qa_files/propensity_intl.csv",
               "iter": 10, "deciles": 2, 'name': 'qabed_propensity_intl_9', 
            "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "7379,5045", 
               
           "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "", "o_esic": ""
               }

config10 = {
            "year": 2022, "month": 2, "market": "INTERNATIONAL",
            "file": cwd + "/qa_files/propensity_intl.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_intl_10',
            "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "",               
            "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "", "o_esic": "7379,5045"
          }

config11 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_us_1',
            "i_ind": [], "i_emp": [],  "i_cty": [], "i_sic": "",   "i_esic": "",            
            "o_ind": [], "o_emp": [], "o_cty": '', "o_sic": "",  "o_esic": ""
            }

config12 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_us_2',
            "i_ind": [], "i_emp": [],  "i_cty": [], "i_sic": "",   "i_esic": "",            
            "o_ind": [], "o_emp": [], "o_cty": 'TX', "o_sic": "",  "o_esic": ""
            }

config13 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_us_3',
            "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "",   "i_esic": "",            
            "o_ind": [], "o_emp": [], "o_cty": "", "o_sic": "9999,7389,5812,7231",  "o_esic": ""
        }

config14 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_us_4',
            "i_ind": [], "i_emp": [], 
            "i_cty": [], "i_sic": "9999,7389,5812,7231",   "i_esic": "",            
            "o_ind": [], "o_emp": [], 
            "o_cty": "", "o_sic": "",  "o_esic": ""
        }

config15 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 5, "deciles": 3, 'name': 'qabed_propensity_us_5',
            "i_ind": [], "i_emp": [], 
            "i_cty": [], "i_sic": "",   "i_esic": "",            
            "o_ind": [], "o_emp": [], 
            "o_cty": "", "o_sic": "",  "o_esic": ""
        }

config16 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_us_6',
            "i_ind": [], "i_emp": ["1 - 9",
            "10 - 49",
            "50 - 99"], 
            "i_cty": [], "i_sic": "",    "i_esic": "",           
            "o_ind": [], "o_emp": [], 
            "o_cty": "", "o_sic": "",  "o_esic": ""
        }

config17 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_us_7',
            "i_ind": [], "i_emp": [], 
            "i_cty": [], "i_sic": "",   "i_esic": "",            
            "o_ind": ["Mining",
            "Public Administration",
            "Retail Trade",
            "Services",
            "Transportation, Communication",
            "Wholesale Trade"], "o_emp": [], 
            "o_cty": "", "o_sic": "",  "o_esic": ""
        }

config18 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_us_8',
            "i_ind": ["Transportation, Communication","Wholesale Trade"], "i_emp": [], 
            "i_cty": [], "i_sic": "",  "i_esic": "",             
            "o_ind": [], "o_emp": [], 
            "o_cty": "", "o_sic": "",  "o_esic": ""
        }

config19 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 10, "deciles": 2, 'name': 'qabed_propensity_us_9',
            "i_ind": [], "i_emp": [], 
            "i_cty": [], "i_sic": "",              
            "o_ind": [], "o_emp": [],  "i_esic": "7379,5045",
            "o_cty": "", "o_sic": "",  "o_esic": ""
        }

config20 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 10, "deciles": 2, 'name': 'qabed_propensity_us_10',
            "i_ind": [], "i_emp": [], 
            "i_cty": [], "i_sic": "",              
            "o_ind": [], "o_emp": [],  "i_esic": "",
            "o_cty": "", "o_sic": "",  "o_esic": "7379,5045"
        }
# negative samples

config31 = {
            "year": 2022, "month": 2, 
            "market": "INTERNATIONAL",
            "file": cwd + "/qa_files/propensity_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_fail_1',
            "i_ind": [], "i_emp": [], 
            "i_cty": [], "i_sic": "",              
            "o_ind": [], "o_emp": [],  "i_esic": "",
            "o_cty": "", "o_sic": "",  "o_esic": ""
    
}

config32 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/propensity_intl.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_fail_2',
            "i_ind": [], "i_emp": [], 
            "i_cty": [], "i_sic": "",              
            "o_ind": [], "o_emp": [],  "i_esic": "",
            "o_cty": "", "o_sic": "",  "o_esic": ""
    
}

config33 = {
            "year": 2022, "month": 2, 
            "market": "USA",
            "file": cwd + "/qa_files/prop_res_sample_intl_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_global_1',
            "i_ind": [], "i_emp": [], 
            "i_cty": [], "i_sic": "",              
            "o_ind": [], "o_emp": [],  "i_esic": "",
            "o_cty": "", "o_sic": "",  "o_esic": ""
    
}

config34 = {
            "year": 2022, "month": 2, 
            "market": "INTERNATIONAL",
            "file": cwd + "/qa_files/prop_res_sample_intl_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_global_2',
            "i_ind": [], "i_emp": [], 
            "i_cty": [], "i_sic": "",              
            "o_ind": [], "o_emp": [],  "i_esic": "",
            "o_cty": "", "o_sic": "",  "o_esic": ""
    
}

config99 = { "year": 2022, "month": 2, 
           "market": "GLOBAL",
           "file": cwd + "/qa_files/prop_res_sample_intl_us.csv",
            "iter": 5, "deciles": 2, 'name': 'qabed_propensity_global_3',
            "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",
               
           "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "", "o_esic": ""}


config_prd = [config1, config11, config31]

config_global = [config99, config33, config34]

config_intl = [config1, config2, config3, config4, config5, config6, config7, config8, config9, config10]
config_us =   [config11, config12, config13, config14, config15, config16, config17, config18, config19, config20]
config_neg = [config31, config32]

configs = config_intl + config_us + config_neg + config_global
