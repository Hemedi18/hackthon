
from flask import Flask, render_template, request

app = Flask(__name__)

# Simple mapping of soil types to recommended crops (with basic nutrition info)
CROP_RECOMMENDATIONS = {
    "Loamy": [("Spinach", "Rich in Iron and Vitamin A"), ("Beans", "High in Protein")],
    "Sandy": [("Sweet Potatoes", "Good source of Vitamin A"), ("Groundnuts", "High in Protein and healthy fats")],
    "Clay": [("Rice", "Energy-rich"), ("Cabbage", "Rich in Fiber and Vitamin C")],
    "Peaty": [("Carrots", "Rich in Beta-Carotene"), ("Lettuce", "Low-calorie, Hydrating")],
    "Chalky": [("Beets", "Good for Blood Health"), ("Broccoli", "Rich in Vitamin K and C")],
    "Saline": [("Barley", "Tolerant to Salinity, Energy Source"), ("Quinoa", "High in Protein and Fiber")]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendation = None
    if request.method == 'POST':
        soil_type = request.form.get('soil_type')
        recommendation = CROP_RECOMMENDATIONS.get(soil_type, [])
    return render_template('index.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)
