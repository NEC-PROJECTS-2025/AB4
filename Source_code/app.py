from flask import Flask, request, render_template
import numpy as np

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    # Render the Prediction input page
    return render_template('index.html')

@app.route('/evaluation')
def evaluation():
    # Render the Model Evaluation page
    return render_template('evaluation.html')

@app.route('/flowchart')
def flowchart():
    # Render the Project Flowchart page
    return render_template('flowchart.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input data from the form
    data = request.form

    # Extract all input values as floats
    features = {
        'CR_S11': float(data['CR_S11']),
        'BIO_S11': float(data['BIO_S11']),
        'QR_PRO': float(data['QR_PRO']),
        'CR_PRO': float(data['CR_PRO']),
        'CC_PRO': float(data['CC_PRO']),
        'ENG_PRO': float(data['ENG_PRO']),
        'G_SC': float(data['G_SC']),
        '2ND_DECILE': float(data['2ND_DECILE']),
        'QUARTILE': float(data['QUARTILE']),
    }

    # Directly assign input values to results without additional logic
    results = features.copy()

    # Calculate overall percentile as the mean of individual results
    overall_percentile = round(np.mean(list(results.values())), 2)

    # Classify the student's performance
    if overall_percentile < 50:
        performance = "The student academics needs to be improved."
    elif 50 <= overall_percentile < 75:
        performance = "The student academics is average."
    else:
        performance = "The student's academics are good."

    # Render the prediction result page with results and overall percentile
    return render_template('prediction.html', results=results, overall_percentile=overall_percentile, performance=performance)

if __name__ == '__main__':
    app.run(debug=True)
