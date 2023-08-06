class Insurance:
    
    def __init__(self, url, app, config):
        self.url = url
        self.app = app
        self.config = config
        
    def page_one(self):
        go_to(self.url)
        time.sleep(5)
        click(Text(self.app))
        time.sleep(5)
        
    def page_two(self):
        write(self.config['name'], into="PROJECT NAME")
        write(self.config["model_name"], into="MODEL NAME")

            
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_three(self):
        drag_file(self.config["input_file"], to="Drop files to attach, or browse")
        click(Button("UPLOAD"))
        wait_until(ComboBox("select field").exists, 50)
        select(ComboBox(above="duns"), 'duns')
        select(ComboBox(above="premium"),'premium')
        select(ComboBox(above="claims"),'claims')
        select(ComboBox(above="load_year"),'load year')
        select(ComboBox(above="load_month"),'load month')
        click(Button("OK"))
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_four(self):
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_five(self):
        click(Button("RUN"))
        
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