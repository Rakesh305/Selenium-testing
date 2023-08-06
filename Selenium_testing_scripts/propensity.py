class Propensity:
    
    def __init__(self, url, app, config):
        self.url = url
        self.app = app
        self.config = config
        
    def page_one(self):
        go_to(self.url)
        time.sleep(5)
        click(Text(self.app))
        click(Button("NEXT"))
        write(self.config['name'], into="Specify the version of the model")
        if self.config['market'] != 'USA':
            click(RadioButton(self.config['market']))
        write(self.config['year'], into="LOAD YEAR")
        write(self.config['month'], into="LOAD MONTH")
        click(Button("GO TO NEXT TAB"))
        time.sleep(5)
    def page_two(self):
        drag_file(self.config['file'],  to="Drop files to attach, or browse")
        click(Button("UPLOAD"))
        select(ComboBox(above="duns"), 'duns')
        click(Button("OK"))
        click(Button("GO TO NEXT TAB"))
        time.sleep(5)
    def page_three(self):
        click(Button("GO TO NEXT TAB"))
        time.sleep(5)
        
    def page_four(self):
        click(Button("NEXT"))
        
        time.sleep(5)
    def page_five(self):
        write(self.config['iter'], into="MODEL ITERATIONS")
        click(Text("Minimum"))
        click(Button("GO TO NEXT TAB"))
        time.sleep(5)
    def page_six(self):
        if self.config['i_emp']:
            for i in self.config['i_emp']:
                click(CheckBox(i))
        if self.config['i_ind']:
            for i in self.config['i_ind']:
                click(CheckBox(i))
        if self.config['i_sic']:
            write(self.config['i_sic'], into="INCLUDE 4")
        
        if self.config['i_esic']:
            write(self.config['i_esic'], into="EXCLUDE 4")
            
        click(Button("GO TO NEXT TAB"))
        time.sleep(5)
    def page_seven(self):
        if self.config['o_cty']:
            click(Button(to_right_of=Text("NONE")))
            if self.config['market'] == 'USA':
                click(Text("SELECT STATE"))
                click(self.config['o_cty'])
            else:
                click(Text("SELECT COUNTRY"))
                click(self.config['o_cty'])
        time.sleep(5)
            
        if self.config['o_ind']:
            for i in self.config['o_ind']:
                click(CheckBox(i))
        if self.config['o_sic']:
            write(self.config['o_sic'], into="INCLUDE 4")
        if self.config['o_esic']:
            write(self.config['o_esic'], into="EXCLUDE 4")    
            
        click(Button("GO TO NEXT TAB"))
        time.sleep(5)
        
    def page_eight(self):
        if self.config['deciles'] != 2:
            click(CheckBox("RETURN"))
            write(self.config['deciles'], "SCORE FOR THE RANK ORDER FILTER")
        click(Button("NEXT"))
        time.sleep(5)
    def page_nine(self):
        click(Button("RUN"))
        
    def run(self, dryrun=False):
        for i in range(5):
            try:
                self.page_one()
                self.page_two()
                self.page_three()
                self.page_four()
                self.page_five()
                self.page_six()
                self.page_seven()
                self.page_eight()
                if self.config['market'] == "GLOBAL":
                    time.sleep(5)
                    click("Go to next tab")
                    click("Go to next tab")
                    click("Go to next tab")
                    click("Go to next tab")
                    click("Next")
                if not dryrun:
                    self.page_nine()
                print(self.config['name'], ' finished')
                break
            except:
                print(self.config['name'], ' failed ', i , ' times')
                pass