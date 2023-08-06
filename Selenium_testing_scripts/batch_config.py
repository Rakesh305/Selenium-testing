import os
cwd = os.getcwd()

batch_config1 = {
    'name': 'qabed_batch_us_1',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_us.csv",
    'type': 'duns only'
}

batch_config2 = {
    'name': 'qabed_batch_us_2',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_us.csv",
    'type': 'tpa'
}

batch_config3 = {
    'name': 'qabed_batch_us_3',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_us.csv",
    'type': 'tpa+it'
}

batch_config4 = {
    'name': 'qabed_batch_us_4',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_us.csv",
    'type': 'sdmr'
}



batch_config5 = {
    'name': 'qabed_batch_intl_1',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_intl.csv",
    'type': 'duns only'
}
# batch_config6 = {
#     'name': 'qabed_batch_intl_2',
#     'pass': 'asgfedccx',
#     'file': cwd + "/qa_files/batch_extract_intl.csv",
#     'type': 'tpa'
# }

batch_config7 = {
    'name': 'qabed_batch_intl_3',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_intl.csv",
    'type': 'tpa+it'
}

batch_config8 = {
    'name': 'qabed_batch_intl_4',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_intl.csv",
    'type': 'sdmr'
}



batch_config9 = {
    'name': 'qabed_batch_global_1',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_global.csv",
    'type': 'duns only'
}

# batch_config10 = {
#     'name': 'qabed_batch_global_2',
#     'pass': 'asgfedccx',
#     'file': cwd + "/qa_files/batch_extract_global.csv",
#     'type': 'tpa'
# }

batch_config11 = {
    'name': 'qabed_batch_global_3',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_global.csv",
    'type': 'tpa+it'
}

batch_config12 = {
    'name': 'qabed_batch_global_4',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_global.csv",
    'type': 'sdmr'
}

batch_config13 = {
    'name': 'qabed_batch_us_5',
    'pass': 'asgfedccx',
    'file': cwd + "/qa_files/batch_extract_us.csv",
    'type': 'annual'
}

config_prd = [batch_config1]
config_us = [batch_config1,batch_config2, batch_config3, batch_config4, batch_config13]
config_intl = [batch_config5,  batch_config7,batch_config8]
config_global = [batch_config9,  batch_config11, batch_config12]
configs = [batch_config1,batch_config2, batch_config3, batch_config4, batch_config5,  batch_config7,batch_config8, batch_config9,  batch_config11, batch_config12, batch_config13]
