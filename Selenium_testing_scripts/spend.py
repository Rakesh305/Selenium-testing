class Spend:
    
    def __init__(self, url, app, config):
        self.url = url
        self.app = app
        self.config = config
        
    def page_one(self):
        go_to(self.url)
        time.sleep(5)
        click(Text("Global"))
        time.sleep(2)
        get_driver().back()
        click(Text(self.app))
        time.sleep(5)
        
    def page_two(self):
        write(self.config['project_name'], into="PROJECT NAME")
        write(self.config['model_name'], into="MODEL NAME")
        write(self.config['model_version'], into="MODEL VERSION")
        if self.config['place'] == 'intl':
            click(RadioButton("INTL"))
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_three(self):
        if self.config['model_type'] == 'multi':
            click(RadioButton("MULTIVARIATE"))
        if self.config["input_data"] == "table":
            click(RadioButton("TABLE FROM STUDIO"))
            try:
                click(Text("Select Database for Input Table"))
                click(Text("qa_workarea"))
            except:
                click(Text("Select Database for Input Table"))
                click(Text("qa_workarea"))

            time.sleep(5)
            try:
                click(Text("SELECT INPUT TABLE"))
                click(Text("sfdc_uni_multi"))
            except:
                click(Text("SELECT INPUT TABLE"))
                click(Text("sfdc_uni_multi"))
        time.sleep(5)
        write("Account_DUNS", into="INPUT DUNS")
        write("Total_Price_converted", into="INPUT TARGET")
        write("Close_Date", into="INPUT DATE")
        time.sleep(3)
        if self.config['model_type'] == 'uni':
            click(RadioButton("TRUE"))
            click(CheckBox("DERIVED"))
            click(CheckBox("EMPLOYEE"))
        
        if self.config['model_type'] == 'multi':
            write("D&B", into="ORGANIZATION NAME")
            click(TextField("FEATURE LIST"))
            click("diff_in_days")
            click("diff_in_months")
        else:
            write("2022-03-31", into="FORECAST END DATE")
        time.sleep(5)

        click(Button("NEXT"))
        time.sleep(3)
    def page_four(self):
        if self.config['advance'] and self.config["model_type"]=='uni':
            click(CheckBox("ADVANCED"))
            time.sleep(3)
            click(CheckBox("NORMALITY"))
            click(CheckBox("STATIONARITY"))
            click(CheckBox("NONE"))
        time.sleep(3)
        click(Button("Next"))
        time.sleep(3)
    def page_five(self):
        click(Button("RUN"))
        time.sleep(3)
        
        
    def run(self, dryrun=False):
        for i in range(5):
            try:
                self.page_one()
                self.page_two()
                self.page_three()
                self.page_four()
                if not dryrun:
                    self.page_five()
                print(self.config['project_name'], " finished")
                break
            except:
                print(self.config['project_name'], " failed ", i, " times")
                pass