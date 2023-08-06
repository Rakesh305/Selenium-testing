
from helium import *

class Batch():
    def __init__(self, url, app, config, passcode):
        self.url = url
        self.app = app
        self.config = config
        self.passcode = passcode

        
    def page_one(self):
        go_to(self.url)
        time.sleep(5)
        click(Text(self.app))
        write(self.config['name'], into="CUSTOMER NAME")
        write("batch", into="MODEL NAME")
        write(1, into="MODEL VERSION")
        write(self.passcode, into="TEST BYPASS")
        
        if self.config['type'] == "tpa":
            driver = get_driver()
            driver.find_element_by_xpath("//input[@value='{}']".format(self.config['type'])).click()
        else:
            click(RadioButton(self.config['type']))

        
        
        click(Button("GO TO NEXT TAB"))
        
        
    def page_two(self):
        if self.config['type'] == "annual":
            click(Button("Next"))
            time.sleep(5)
            try:
                click("SELECT PICKLE PATH")
                write("s3://dnb-analytics-customers/e2_qa_workarea/qa_cluster_workarea/pickle_folder/sc_qabed_scorecard_us_1_scorecard_1_c8728bfc_4e1c_4966_9ef9_e2bcd8c367ba_20230321_1650.pkl",
                     into = "Type to search")
                press(ENTER)
            except:
                click("SELECT PICKLE PATH")
                write("s3://dnb-analytics-customers/e2_qa_workarea/qa_cluster_workarea/pickle_folder/sc_qabed_scorecard_us_1_scorecard_1_c8728bfc_4e1c_4966_9ef9_e2bcd8c367ba_20230321_1650.pkl",
                     into = "Type to search")
                press(ENTER)
            click(Button("Next"))
        else:
        #wait_until(Button("NEXT").is_enabled)
            time.sleep(10)
            click(RadioButton("CSV FILE"))
            drag_file(self.config['file'], to="Drop files to attach, or browse")
            click(Button("UPLOAD"))
            wait_until(ComboBox("select field").exists)
            combobox = find_all(ComboBox("select field"))
            select(ComboBox(above="duns"), 'duns')
            select(ComboBox(above="model_score"),'model score')
            result = "Success"
            click(Button("OK"))
            click(Button("NEXT"))

    def page_three(self):
        try:
            click(Button("SUBMIT"))
        except:
            click(Button("Run"))
        
    
    def run(self, dryrun=False):
        for i in range(5):
            try:
                self.page_one()
                self.page_two()
                if not dryrun:
                    self.page_three()
                print(self.config['name'], ' finished')
                break
            except:
                print(self.config['name'], ' failed ', i , ' times')
                pass

def batch_run(configs):
    for config in configs:
        batch = Batch(url, app, config)
        batch.run()


# batch_run(batch_configs)
