import requests
from flask import Flask, request, jsonify

# Define Flask app
app = Flask(__name__)

# Define ingredient categories
harmful_ingredients = [
    "high fructose corn syrup", "artificial colors", "red 40",
    "aspartame", "sucralose", "bht", "bha", "msg", "hydrogenated oils",
    "nitrates", "nitrites", "propylparaben", "carrageenan"
]

moderate_ingredients = [
    "sugar", "canola oil", "soybean oil", "corn starch",
    "enriched flour", "xanthan gum", "lecithin"
]

clean_alternatives = {
    "soda": {"name": "Sparkling Water with Natural Flavor", "score": 9},
    "cola": {"name": "Sparkling Water with Natural Flavor", "score": 9},
    "soft drink": {"name": "Organic Kombucha (No Added Sugar)", "score": 10},
    "peanut butter": {"name": "Organic Peanut Butter (No Sugar or Oils)", "score": 10},
    "bread": {"name": "Organic Whole Grain Sourdough", "score": 9}
}

@app.route('/check_ingredients', methods=['POST'])
def check_ingredients():
    data = request.json
    ingredients = data.get("ingredients", [])

    result = {
        "harmful": [i for i in ingredients if i.lower() in harmful_ingredients],
        "moderate": [i for i in ingredients if i.lower() in moderate_ingredients],
        "clean_alternatives": clean_alternatives
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

