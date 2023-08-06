from supplier_scorecard import Supplier_Scorecard
from supplier_scorecard_config import configs

url = "https://analyticsstudio-mlflows-dev.aas.dnb.net/#/webapps"
app = "Supplier Scorecard"
for config in configs[:1]:
    sc = Supplier_Scorecard(url, app, config)
    sc.run(dryrun=True)
        

