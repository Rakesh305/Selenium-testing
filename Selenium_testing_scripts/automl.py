class Automl:
    
    def __init__(self, url, app, config):
        self.url = url
        self.app = app
        self.config = config
        
    def page_one(self):
        go_to(self.url)
        time.sleep(5)
        click(Text(self.app))
        click(Button("NEXT"))
        time.sleep(5)
        
    def page_two(self):
        write(self.config['name'], into="CUSTOMER NAME")
        if self.config["input_data"] == "table":
            try:
                click(Text("Select Database for Input Table"))
                click(Text("user_sample_data"))
            except:
                click(Text("Select Database for Input Table"))
                click(Text("user_sample_data"))
                
                time.sleep(5)
            try:
                click(Text("SELECT INPUT TABLE"))
                write(self.config["table_name"], into="type to search")
                time.sleep(3)
                press(ENTER)
            except:
                click(Text("SELECT INPUT TABLE"))
                write(self.config["table_name"], into="type to search")
                time.sleep(3)
                press(ENTER)
            write(self.config["duns_col"], into="INPUT DUNS FIELD")
            
        if self.config["input_data"] == "csv":
            click(RadioButton("UPLOAD"))
            drag_file(self.config["input_file"], to="Drop files to attach, or browse")
            click(Button("UPLOAD"))
            wait_until(ComboBox("select field").exists, 50)
            select(ComboBox(above="duns"), 'duns')
            select(ComboBox(above="target"),'target')
            click(Button("OK"))
            
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_three(self):
        if self.config['model'] == 'binary':
            click(CheckBox("LIGHTGBM"))
            click(CheckBox("XGBOOST"))
        else:
            click(RadioButton("REGRESSION"))
            time.sleep(1)
            click(CheckBox("XGBOOST"))
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_four(self):
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_five(self):
        click(Button("RUN THE MODEL"))
        
    def run(self, dryrun=False):
        for i in range(5):
            try:
                self.page_one()
                self.page_two()
                self.page_three()
                self.page_four()
                if not dryrun:
                    self.page_five()
                print(self.config['name'], " finished")
                break
            except:
                print(self.config['name'], " failed ", i, " times")
                pass