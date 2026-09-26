from flask import Flask, render_template, redirect
from routes.about import about_bp
from routes.login import auth_bp

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')

app.secret_key = 'cookiecheesecake'

app.register_blueprint(about_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.get("/api/health")
def health():
    return {
        "status": "ok"
    }

@app.after_request
def allow_amplify(response):
    response.headers["Access-Control-Allow-Origin"] = (
        "https://main.d13wzj1s6istn6.amplifyapp.com"
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)