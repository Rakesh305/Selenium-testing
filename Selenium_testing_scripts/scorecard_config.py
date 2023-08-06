import os
cwd = os.getcwd()

config1 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_us_1' ,
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'us',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_us_2k.csv",

    #page_three
    'features': [],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': False

        
}
config2 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_us_2' ,
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'us',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_us_2k.csv",

    #page_three
    'features': ['ba', 'bi', 'dt', 'sd'],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': False

        
}
config3 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_us_3' ,
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'us',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_us_2k.csv",

    #page_three
    'features': ['ald'],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': False

        
}

config4 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_us_4' ,
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'us',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_us_partitions_30k.csv",

    #page_three
    'features': [],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': False

        
}

config11 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_intl_1' ,
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'intl',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_intl_2k.csv",

    #page_three
    'features': [],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': False

        
}

config12 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_intl_2',
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'intl',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_intl_2k.csv",

    #page_three
    'features': [],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': True
        
}

config21 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_fail_1' ,
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'intl',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_us_2k.csv",

    #page_three
    'features': [],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': False

        
}
config22 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_global_1' ,
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'intl',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_global_4k.csv",

    #page_three
    'features': [],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': False

        
}
config23 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_global_2' ,
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'us',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_global_4k.csv",

    #page_three
    'features': [],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': False

        
}

config24 = {
    
    #page_one
    'customer_name': 'qabed_scorecard_fail_2',
    'model_name': 'scorecard',
    'model_version': 1,
    'model_type': 'us',
    #page_two
    #csv
    'input_data': 'csv',
    'input_file': cwd + "/qa_files/Scorecard_data_intl_2k.csv",

    #page_three
    'features': [],
    'advanced': False,
    'comp_scores': ['css', 'fss'],
    'intl_append_score': False

        
}

config_prd = [config1, config11, config21]

config_us = [config1, config2, config3, config4]
config_intl = [config11, config12]
config_neg = [config21, config22, config23, config24]

configs = config_us + config_intl + config_neg
