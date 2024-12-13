from flask import Flask, request, render_template

app = Flask(__name__)

# Hidden flag and key
FLAG = "U1RVUlNFQ3tWVUxOM1JBQkwzX0FJfQ=="
SECRET_KEY = "Y0u_c4n1_d0_1is3"
HINT= "Y0u_d0_1t"

# A naive "AI" function
def vulnerable_ai(input_text):
    # Simulate "AI" by searching for the secret key in the input
    if SECRET_KEY in input_text:
        return f"Access Granted: {FLAG}"
    return f"Access Denied: No {HINT} found!"

@app.route('/')
def index():
    # Render the main form for the challenge
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get input from the form
    input_text = request.form.get('text', '')
    
    # Process input through the naive AI
    response = vulnerable_ai(input_text)
    
    # Return the result to the user
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)

