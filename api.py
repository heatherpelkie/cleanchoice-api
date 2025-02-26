Last login: Tue Feb 25 21:22:45 on ttys001
heathercbarone@Heathers-MBP ~ % nano api.py






















  UW PICO 5.09                          File: api.py                            

import requests
from flask import Flask, request, jsonify

# Define Flask app
app = Flask(__name__)

# Define ingredient categories
harmful_ingredients = ["high fructose corn syrup", "artificial colors", "red 40$
                        "aspartame", "sucralose", "bht", "bha", "msg", "hydroge$
                        "nitrates", "nitrites", "propylparaben", "carrageenan"]
moderate_ingredients = ["sugar", "canola oil", "soybean oil", "corn starch", "c$
                         "enriched flour", "xanthan gum", "lecithin"]

clean_alternatives = {
    "soda": {"name": "Sparkling Water with Natural Flavor", "score": 9},
    "cola": {"name": "Sparkling Water with Natural Flavor", "score": 9},
    "soft drink": {"name": "Organic Kombucha (No Added Sugar)", "score": 10},
    "peanut butter": {"name": "Organic Peanut Butter (No Sugar or Oils)", "scor$
    "bread": {"name": "Organic Whole Grain Sourdough", "score": 9},

^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  

