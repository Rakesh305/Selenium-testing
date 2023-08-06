import os
cwd = os.getcwd()

config1 = {
    'name': 'qabed_collection_us_1',
    'file': cwd + "/qa_files/collections_aging_file.csv",
    'bad': 'AGING BUCKET_30',
    'per': 50,
    'risk': 'COLLECTIONS RISK SEGMENT'
}
config2 = {
    'name': 'qabed_collection_us_2',
    'file': cwd + "/qa_files/collections_aging_file.csv",
    'bad': 'AGING BUCKET_30',
    'per': 20,
    'risk': 'COLLECTIONS RISK SEGMENT'
}
config3 = {
    'name': 'qabed_collection_us_3',
    'file': cwd + "/qa_files/collections_aging_file.csv",
    'bad': 'AGING BUCKET_60',
    'per': 30,
    'risk': 'COLLECTIONS RISK SEGMENT'
}
config4 = {
    'name': 'qabed_collection_us_4',
    'file': cwd + "/qa_files/collections_aging_file.csv",
    'bad': 'AGING BUCKET_60',
    'per': 20,
    'risk': 'COLLECTIONS RISK SEGMENT'
}
config5 = {
    'name': 'qabed_collection_us_5',
    'file': cwd + "/qa_files/collections_aging_file.csv",
    'bad': 'AGING BUCKET_90',
    'per': 20,
    'risk': 'COLLECTIONS RISK SEGMENT'
}
config6 = {
    'name': 'qabed_collection_us_6',
    'file': cwd + "/qa_files/collections_aging_file.csv",
    'bad': 'AGING BUCKET_120',
    'per': 20,
    'risk': 'COLLECTIONS RISK SEGMENT'
}
config_prd = [config1]

configs = [config1, config2, config3, config4, config5, config6]
