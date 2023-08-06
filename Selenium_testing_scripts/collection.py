class Collection:
    
    def __init__(self, url, app, config):
        self.config = config
        self.url = url
        self.app = app
        
    def page_one(self):
        go_to(self.url)
        time.sleep(5)
        click(Text(self.app))
        time.sleep(3)
        write(self.config['name'], into="PROJECT NAME")
        write("Collections", into="MODEL NAME")
        click(Button("NEXT"))
    
    def page_two(self):
        drag_file(self.config['file'], to="Drop files to attach, or browse")
        click(Button("UPLOAD"))
        time.sleep(3)
        select(ComboBox(above="duns"), 'duns')
        select(ComboBox(above="curent_bal"),'current_balance')
        select(ComboBox(above="dpd_0_30"), 'Aging Bucket_30')
        select(ComboBox(above="dpd_31_60"), 'Aging Bucket_60')
        select(ComboBox(above="dpd_61_90"), 'Aging Bucket_90')
        select(ComboBox(above="dpd_90_120"), 'Aging Bucket_120')
        select(ComboBox(above="dpd_120_180"), 'Aging Bucket_180')
        select(ComboBox(above="dpd_180_210"), 'Aging Bucket_999')
        select(ComboBox(above="load_year"), 'load_year')
        select(ComboBox(above="load_month"), 'load_month')
        click(Button("OK"))
        click(Button("NEXT"))
        
    def page_three(self):
        click(RadioButton(self.config['bad']))
        write(self.config['per'], "BAD PERCENTAGE")
        click(RadioButton(self.config['risk']))
        click(Button("NEXT"))
        
    def page_four(self):
        write("OutSource to Agency", into="LEVEL 0 MOST SEVERE")
        click(Button("NEXT"))
    
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
                print(self.config['name'], ' finished')
                break
            except:
                print(self.config['name'], ' failed ', i, ' times')
                pass