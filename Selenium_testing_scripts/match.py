from helium import *
import uuid
class Match():
    def __init__(self, url, app, config):
        self.url = url
        self.app = app
        self.config = config
        
    def page_one(self, dryrun):
        go_to(self.url)
        time.sleep(5)
        click(Text(self.app))
        time.sleep(3)
        write(self.config['name'], into="PROJECT NAME")
        write("match", into="MODEL NAME")
        write(1, into="MODEL VERSION")
        tag = str(uuid.uuid1())[:6]
        write(tag, into="TAG")
        drag_file(self.config['file'], to="Drop files to attach, or browse")
        click(Button("UPLOAD"))
        wait_until(ComboBox("select field").exists)
        
        select(ComboBox(above="business_name"), 'Business Name')
        select(ComboBox(above="address"), 'Address Line 1')
        select(ComboBox(above="city"), 'City')
        select(ComboBox(above="province"),'State')
        select(ComboBox(above="postal_code"), 'ZIP')
        select(ComboBox(above="country"), 'Country')
        select(ComboBox(above="phone_number"), 'Phone')
        click(Button("OK"))
        time.sleep(3)
        if not dryrun:
            click(Button("Submit for Match"))
        
        
    
    def run(self, dryrun=False):
        for i in range(5):
            try:
                self.page_one(dryrun = dryrun)
                print(self.config['name'], ' finished')
                break
            except:
                print(self.config['name'], ' failed ', i , ' times')
                pass
