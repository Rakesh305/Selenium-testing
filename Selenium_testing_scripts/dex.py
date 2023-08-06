class Dex:
    
    def __init__(self, url, app, config, passcode):
        self.config = config
        self.url = url
        self.app = app
        self.passcode = passcode
    def page_one(self):
        go_to(self.url)
        time.sleep(5)
        click(Text(self.app))
        write(self.config['name'], into="CUSTOMER NAME")
        write(self.passcode, into="TEST BYPASS")
        if self.config['dataset'] != "BLACKKNIGHT ASSESSMENT MATCHED":
            click(RadioButton(self.config['dataset']))
        click(Button("NEXT"))
        time.sleep(3)
    def page_two(self):
        click(RadioButton(self.config['type']))
        if self.config['type'] == "DUNS LIST":
            drag_file(self.config['file'], to="Drop files to attach, or browse")
            click(Button("UPLOAD"))
            select(ComboBox(above="duns"), 'duns')
            click(Button("OK"))
            
        click(Button("NEXT"))
        time.sleep(4)
    def page_three(self):
        click(Button("SUBMIT"))
        time.sleep(3)
        
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