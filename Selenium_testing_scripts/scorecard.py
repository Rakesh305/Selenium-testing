class Scorecard:
    def __init__(self, url, app, config):
        self.config = config
        self.url = url
        self.app = app
    
    def page_one(self):
        go_to(self.url)
        time.sleep(5)
        click(Text(self.app))
        write(self.config['customer_name'], into="customer NAME")
        write(self.config['model_name'], into="MODEL NAME")
        write(self.config['model_version'], into="MODEL VERSION")
        
        if self.config['model_type'] == 'intl':
            click(RadioButton("INTL SCORECARD"))
        click(Button("Next"))
    
    def page_two(self):
        if self.config['input_data'] == 'table':
            click(RadioButton("TABLE FROM STUDIO"))
            wait_until(S(".dropdown").exists)

            t = find_all(S(".dropdown"))
            click(t[0])
            time.sleep(5)
            write("qa_workarea", into="Type to search")
            press(ENTER)
            time.sleep(5)
            
            click(t[1])
            write("scorecard_data_us", into="Type to search")
            press(ENTER)
            
            write("target", into="TARGET COLUMN NAME")
            
        else:
            drag_file(self.config['input_file'], to="Drop files to attach, or browse")
            click(Button('UPLOAD'))
            time.sleep(3)
            select(ComboBox(above="duns"), 'duns')
            select(ComboBox(above="phycountryname"),'COUNTRY_NAME')
            select(ComboBox(above="target"), 'target')
            select(ComboBox(above="load_year"), 'load_year')
            select(ComboBox(above="load_month"), 'load_month')
            time.sleep(3)
            click(Button("OK"))
            click(Button("NEXT"))
        time.sleep(3)
        
    def page_three(self):
        if 'ba' in self.config['features']:
            click(CheckBox("HQ - BUSINESS ACTIVITY"))
        if 'bi' in self.config['features']:
            click(CheckBox("HQ - BUSINESS INQUIRIES"))
        if 'dt' in self.config['features']:
            click(CheckBox("HQ - DETAIL TRADE"))
        if 'sd' in self.config['features']:
            click(CheckBox("SHIPPING DATA"))
        if 'ald' in self.config['features']:
            click(CheckBox("ALTERNATIVE DATA"))
            time.sleep(2)
            click(CheckBox("ABERDEEN_BUSINESS_INTELLIGENCE"))
            click(CheckBox("PIPECANDY_CONSOLIDATED_DATA"))
            click(CheckBox("FUNDZ_FILING_DATA"))
        
        if self.config['intl_append_score']:
            click(RadioButton("YES"))
        click(Button("NEXT"))
        time.sleep(3)
    
    def page_four(self):
        if 'fss' not in self.config['comp_scores']:
            click(Button(to_left_of=TextField("fss_points")))
            
        if 'css' not in self.config['comp_scores']:
            click(Button(to_left_of=TextField("css_points")))
            
        if self.config['advanced']:
            click(CheckBox("ADVANCED SETTINGS"))
            
        click(Button("NEXT"))
        time.sleep(3)
    
    def page_five(self):
        click(Button("NEXT"))
        time.sleep(3)

    def page_six(self):
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_seven(self):
        click(Button("RUN"))
        time.sleep(3)
        
    def run(self, dryrun=False):
        for i in range(5):
            try:
                self.page_one()
                self.page_two()
                self.page_three()
                self.page_four()
                if self.config['intl_append_score']:
                    self.page_five()
                    self.page_six()
                if not dryrun:
                    self.page_seven()
                print(self.config['customer_name'], 'finished')
                break
            except:
                print(self.config['customer_name'], ' failed ' , i , ' times')
                pass