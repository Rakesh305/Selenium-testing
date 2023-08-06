import os
cwd = os.getcwd()

# intl
config1 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_1",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "input": False, "output": False,
    "iter": 5, "deciles": 2,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",    
    "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "", "o_esic": ""
    
}

config2 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_2",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": True,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",      
    "o_ind": [], "o_emp": [], "o_cty": "GERMANY", "o_sic": "", "o_esic": ""
    
}

config3 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_3",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": True,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",      
    "o_ind": [], "o_emp": [], "o_cty": "", "o_sic": "7379,5045", "o_esic": ""
    
}

config4 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_4",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 2,
    "input": True, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "7379,5045",  "i_esic": "",        
    "o_ind": [], "o_emp": [], "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config5 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_5",
    "input": False, "output": False,
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 3,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",   
    "o_ind": [], "o_emp": [], "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config6 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_6",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 2,
    "input": True, "output": False,
    "i_ind": [], "i_emp": ["1 - 9","10 - 49","50 - 99"], "i_cty": [], "i_sic": "",   "i_esic": "",  
    "o_ind": [], "o_emp": [], "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config7 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_7",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": True,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "",     
    "o_ind": ["CONSTRUCTION", "MANUFACTURING", "RETAIL TRADE"], "o_emp": "",  "i_esic": "",  
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config8 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_8",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 2,
    "input": True, "output": False,
    "i_ind": ["MINING", "SERVICES", "MISSING"], "i_emp": [], "i_cty": [], "i_sic": "",  "i_esic": "",  
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config9 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_9",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 10, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "7379,5045", 
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config10 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_10",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": True,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "", 
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": "7379,5045"
    
}

config71 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_intl_11",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 2,
    "input": True, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": "GERMANY", "i_sic": "", "i_esic": "",      
    "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "", "o_esic": ""
    
}



# us

config11 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_1",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "input": False, "output": False,
    "iter": 5, "deciles": 2,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",    
    "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "", "o_esic": ""
    
}

config12 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_2",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": True,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",      
    "o_ind": [], "o_emp": [], "o_cty": "TX", "o_sic": "", "o_esic": ""
    
}

config13 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_3",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": True,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",      
    "o_ind": [], "o_emp": [], "o_cty": "", "o_sic": "9999,7389,5812,7231", "o_esic": ""
    
}

config14 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_4",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 2,
    "input": True, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "9999,7389,5812,7231",  "i_esic": "",        
    "o_ind": [], "o_emp": [], "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config15 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_5",
    "input": False, "output": False,
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 3,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",   
    "o_ind": [], "o_emp": [], "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config16 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_6",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 2,
    "input": True, "output": False,
    "i_ind": [], "i_emp": ["1 - 9","10 - 49","50 - 99"], "i_cty": [], "i_sic": "",   "i_esic": "",  
    "o_ind": [], "o_emp": [], "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config17 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_7",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": True,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "",     
    "o_ind": ["CONSTRUCTION", "MANUFACTURING", "RETAIL TRADE"], "o_emp": "",  "i_esic": "",  
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config18 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_8",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 2,
    "input": True, "output": False,
    "i_ind": ["MINING", "SERVICES", "MISSING"], "i_emp": [], "i_cty": [], "i_sic": "",  "i_esic": "",  
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config19 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_9",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 10, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "7379,5045", 
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config20 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_10",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": True,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "", 
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": "7379,5045"
    
}

config41 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_us_11",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 2,
    "input": True, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": "TX", "i_sic": "", "i_esic": "",      
    "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "", "o_esic": ""
    
}




# negative samples

config21 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_fail_1",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "", 
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config22 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_fail_2",
    "input_file": cwd + "/qa_files/propensity_intl.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "", 
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}


# response examples

config31 = {
    "model_type": "response",
    "market": "intl",
    "name": "qabed_propensitybeta_res_1",
    "input_file": cwd + "/qa_files/prop_res_sample_intl.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "",     
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": ""
    
}

config32 = {
    "model_type": "response",
    "market": "us",
    "name": "qabed_propensitybeta_res_2",
    "input_file": cwd + "/qa_files/prop_res_sample_usa.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "",     
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": ""
    
}

# global exmaples
config51 = {
    "model_type": "response",
    "market": "global",
    "name": "qabed_propensitybeta_res_3",
    "input_file": cwd + "/qa_files/prop_res_sample_intl_us.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "",     
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": ""
    
}

config52 = {
    "model_type": "propensity",
    "market": "global",
    "name": "qabed_propensitybeta_global_1",
    "input_file": cwd + "/qa_files/prop_res_sample_intl_us.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "",     
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": ""
    
}

config53 = {
    "model_type": "propensity",
    "market": "intl",
    "name": "qabed_propensitybeta_global_2",
    "input_file": cwd + "/qa_files/prop_res_sample_intl_us.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "", 
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}

config54 = {
    "model_type": "propensity",
    "market": "us",
    "name": "qabed_propensitybeta_global_3",
    "input_file": cwd + "/qa_files/prop_res_sample_intl_us.csv",
    "iter": 5, "deciles": 2,
    "input": False, "output": False,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "","i_esic": "", 
    "o_ind": [], "o_emp": "", 
    "o_cty": "", "o_sic": "", "o_esic": ""
    
}

# service package
config61 = {
    "model_type": "propensity",
    "market": "us",
    "name": "service_propensitybeta_us_1",
    "input_file": cwd + "/qa_files/propensity_us.csv",
    "input": False, "output": False,
    "iter": 5, "deciles": 2,
    "i_ind": [], "i_emp": [], "i_cty": [], "i_sic": "", "i_esic": "",    
    "o_ind": [], "o_emp": [], "o_cty": [], "o_sic": "", "o_esic": ""
    
}

config_service = [config61]
config_prd = [config1, config2, config11, config12, config21, config31, config61]


config_global = [config51, config52, config53, config54]
config_intl = [config1, config2, config3, config4, config5, config6, config7, config8, config9, config10, config71]
config_us = [config11, config12, config13, config14, config15, config16, config17, config18, config19, config20, config41]
config_neg = [config21, config22]
config_res = [config31, config32]

configs = config_intl + config_us + config_neg + config_res + config_global
