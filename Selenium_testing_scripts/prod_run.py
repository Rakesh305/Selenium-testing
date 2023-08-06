def prod_marketing(url, region, dryrun=True):
#     %run -i propensity.py
#     %run -i propensity_config.py
    from propensity import Propensity
    from propensity_config import config_us
    app = "Global Propensity - Q2_2022"

    if region == "global_marketing":
        configs = config_us[:1] + config_intl[:1]
    else:
        configs = config_us[:1]

    for config in configs:
        pro = Propensity(url, app, config)
        pro.run(dryrun=dryrun)
        
    app = "Global Propensity and Response"
#     %run -i propensity_beta.py
#     %run -i propensity_beta_config.py

    if region == "us_marketing":
        configs = config_us[:1] + config_intl[:1] + config_res[:1]
    else:
        configs = config_us[:1] + config_res[1:]

    for config in configs:
        pro = Propensity_beta(url, app, config)
        pro.run(dryrun=dryrun)
        
        
# def prod_tools(url, dryrun=False):
#     #automl
#     %run -i automl.py
#     %run -i automl_config.py
#     app = "AutoML"
    
#     for config in configs:
#         automl = Automl(url, app, config)
#         automl.run(dryrun=False)
#     #batch    
#     %run -i Batch.py
#     %run -i batch_config.py
#     app = "Batch Extract" 
    

#     batch = Batch(url, app, config1)
#     batch.run(dryrun=dryrun)
     
#     #dex
#     %run -i dex.py
#     %run -i dex_config.py
#     app = "Data Exchange Sampler"
#     d = Dex(url, app, config1)
#     d.run(dryrun=dryrun)
    
#     #match
#     %run -i match.py
#     %run -i match_config.py
#     app ="DUNS Match"
#     m = Match(url, app, config1)
#     m.run(dryrun=dryrun)