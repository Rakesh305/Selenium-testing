import os
cwd = os.getcwd()

config1 = {
    
    #page_one
    'customer_name': 'qabed_supplier_global_1' ,
    'model_name': 'supplier_scorecard',
    'model_version': 1,
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/C_supply_8k_22_05.csv"

        
}

config2 = {
    
    #page_one
    'customer_name': 'qabed_supplier_us_1' ,
    'model_name': 'supplier_scorecard',
    'model_version': 1,
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/C_supply_8k_22_05_US.csv"

        
}
config3 = {
    
    #page_one
    'customer_name': 'qabed_supplier_intl_1' ,
    'model_name': 'supplier_scorecard',
    'model_version': 1,

    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/C_supply_8k_22_05_INTL.csv"


        
}

config4 = {
    
    #page_one
    'customer_name': 'qabed_supplier_us_2' ,
    'model_name': 'supplier_scorecard',
    'model_version': 1,
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_us_2k.csv"

        
}
config5 = {
    
    #page_one
    'customer_name': 'qabed_supplier_intl_2' ,
    'model_name': 'supplier_scorecard',
    'model_version': 1,

    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_Intl_2k.csv"


        
}

config6 = {
    
    #page_one
    'customer_name': 'qabed_supplier_fail_1' ,
    'model_name': 'supplier_scorecard',
    'model_version': 1,

    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/C_supply_8k_22_05_fail_1.csv"

        
}

config7 = {
    
    #page_one
    'customer_name': 'qabed_supplier_fail_2' ,
    'model_name': 'supplier_scorecard',
    'model_version': 1,

    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/C_supply_8k_22_05_fail_2.csv"
        
}

config8 = {
    
    #page_one
    'customer_name': 'qabed_supplier_fail_3' ,
    'model_name': 'supplier_scorecard',
    'model_version': 1,

    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/C_supply_8k_22_05_fail_3.csv"

        
}

configs = [config1, config2, config3, config4, config5, config6, config7, config8]
