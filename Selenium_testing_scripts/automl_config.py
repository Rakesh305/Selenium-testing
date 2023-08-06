import os
cwd = os.getcwd()
config1 = {
    "model": "binary",
    "name": "qabed_automl_binary_1",
    "table_name": "dnb_sample_automl",
    "input_data": "table",
    "duns_col": "id",
    "target_col": "target"
}
config2 = {
    "model": "regression",
    "name": "qabed_automl_regression_1",
    "table_name": "dnb_sample_automl_regression",
    "input_data": "table",
    "duns_col": "id",
    "target_col": "target"
}
config3 = {
    "model": "binary",
    "name": "qabed_automl_binary_2",
    "table_name": "dnb_automl_binary",
    "input_data": "csv",
    "input_file": cwd + "/qa_files/AUTOML_Binary_automl_test.csv",
    "duns_col": "id",
    "target_col": "target"
}

config4 = {
    "model": "regression",
    "name": "qabed_automl_regression_2",
    "table_name": "dnb_automl_regression",
    "input_data": "csv",
    "input_file": cwd + "/qa_files/AUTOML_Regression_automl_test.csv",
    "duns_col": "id",
    "target_col": "target"
}

configs = [config1, config2, config3, config4]