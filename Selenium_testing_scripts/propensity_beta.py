class Propensity_beta:
    
    def __init__(self, url, app, config):
        self.url = url
        self.app = app
        self.config = config
 
    def page_one(self):
        go_to(self.url)
        time.sleep(5)
        click(Text(self.app))
        if self.config['model_type'] == 'response':
            click(RadioButton("RESPONSE"))
        
        if self.config['market'] == 'intl':
            click(RadioButton("INTERNATIONAL"))
        if self.config['market'] == 'global':
            click(RadioButton("GLOBAL"))
        
        write(self.config['name'], into="PROJECT NAME")
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_two(self):
        write(1, into="LOAD MONTH")
        drag_file(self.config['input_file'], to="Drop files to attach, or browse")
        click(Button("Upload"))
        select(ComboBox(above="duns"), 'duns')
        if self.config['model_type'] == 'response':
            select(ComboBox(above="target"), 'target')
        click(Button("OK"))
        click(Button("GO TO NEXT PAGE"))
        time.sleep(5)
            
    def page_three(self):
        
        if 'side' in self.config:
            click(CheckBox("APPEND SIDE DATA"))
            click(RadioButton("TABLE"))
            click(Text("SELECT DATABASE FOR SIDE DATA"))
            click(Text("global_pilot_scores"))
            time.sleep(10)
            click(Text("SELECT SIDE TABLE"))

            click(Text("dnb_da_shipping_global"))

           
        
        if self.config['market'] == 'intl':
            if self.config['input']:
                click(CheckBox("INTL ADDRESSABLE MARKET INPUT RESTRICTION"))
                
                if self.config['i_sic']:
                    write(self.config['i_sic'], into="INCLUDE 4 DIGIT SIC") 
                    
                if self.config['i_esic']:
                    write(self.config['i_esic'], into="EXCLUDE 4 DIGIT SIC")
            
                if self.config['i_ind']:
                    for i in self.config['i_ind']:
                        click(CheckBox(i))
                
                if self.config['i_emp']:
                    for i in self.config['i_emp']:
                        click(CheckBox(i))
                        
                if self.config['i_cty']:
                    click(Button(to_right_of=Text("ALL")))
                    click(Text("SELECT COUNTRY"))
                    click(self.config['i_cty'])
                    
            if self.config['output']:
                click(CheckBox("INTL ADDRESSABLE MARKET OUTPUT RESTRICTION"))
                
                if self.config['o_sic']:
                    write(self.config['o_sic'], into="INCLUDE 4 DIGIT SIC") 
                    
                if self.config['o_esic']:
                    write(self.config['o_esic'], into="EXCLUDE 4 DIGIT SIC")
            
                if self.config['o_ind']:
                    for i in self.config['o_ind']:
                        click(CheckBox(i))
                
                if self.config['o_emp']:
                    for i in self.config['o_emp']:
                        click(CheckBox(i))
                        
                if self.config['o_cty']:
                    click(Button(to_right_of=Text("NONE")))
                    click(Text("SELECT COUNTRY"))
                    click(self.config['o_cty'])
        if self.config['market'] == 'us':
            if self.config['input']:
                click(CheckBox("USA ADDRESSABLE MARKET INPUT RESTRICTION"))
                
                if self.config['i_sic']:
                    write(self.config['i_sic'], into="INCLUDE 4 DIGIT SIC") 
                    
                if self.config['i_esic']:
                    write(self.config['i_esic'], into="EXCLUDE 4 DIGIT SIC")
            
                if self.config['i_ind']:
                    for i in self.config['i_ind']:
                        click(CheckBox(i))
                
                if self.config['i_emp']:
                    for i in self.config['i_emp']:
                        click(CheckBox(i))
                        
                if self.config['i_cty']:
                    click(Button(to_right_of=Text("ALL")))
                    click(Text("SELECT STATE"))
                    click(self.config['i_cty'])
                    
            if self.config['output']:
                click(CheckBox("USA ADDRESSABLE MARKET OUTPUT RESTRICTION"))
                
                if self.config['o_sic']:
                    write(self.config['o_sic'], into="INCLUDE 4 DIGIT SIC") 
                    
                if self.config['o_esic']:
                    write(self.config['o_esic'], into="EXCLUDE 4 DIGIT SIC")
            
                if self.config['o_ind']:
                    for i in self.config['o_ind']:
                        click(CheckBox(i))
                
                if self.config['o_emp']:
                    for i in self.config['o_emp']:
                        click(CheckBox(i))
                        
                if self.config['o_cty']:
                    click(Button(to_right_of=Text("NONE")))
                    click(Text("SELECT STATE"))
                    click(self.config['o_cty'])
        
        
        
  
                
        if self.config['deciles'] != 2:
            click(RadioButton("TOP SELECTED DECILES"))
            write(self.config['deciles'], into="HOW MANY")
            time.sleep(2)
            
        if self.config['iter'] != 5:
            click(CheckBox("ADVANCED MODEL PARAMETERS"))
            write(self.config['iter'], into="MODEL ITERATIONS") 
            time.sleep(2)   
        try:    
            click(Button("Go to next Page"))

        except:
            click(Button("Go to next Page"))

        time.sleep(3)
    def page_four(self):
        
        click(Button("Run"))
        
    def run(self, dryrun=False):
        for i in range(5):
            try:
                self.page_one()
                self.page_two()
                self.page_three()
                if not dryrun:
                    self.page_four()
                print(self.config['name'], ' success ')
                break
            except:
                print(self.config['name'], ' failed ', i , ' times')
                pass

        