class Annual:
    
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
        write(self.config['name'], into="CUSTOMER NAME")       
        click(Button("Go to next tab"))
        time.sleep(3)
        
    def page_three(self):
        click(Button("NEXT"))
        time.sleep(3)
        
    def page_four(self):
        click(Button("Run"))
        time.sleep(3)

    def run(self, dryrun=False):
        for i in range(5):
            try:
                self.page_one()
                self.page_two()
                self.page_three()
                if not dryrun:
                    self.page_four()
                print(self.config['name'], " finished")
                break
            except:
                print(self.config['name'], " failed ", i, " times")
                pass