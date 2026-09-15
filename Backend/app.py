from flask import Flask
from routes.about import about_bp

app = Flask(__name__)

app.register_blueprint(about_bp)

@app.get("/api/health")
def health():
  return {
  "status": "ok"
  }
if __name__ == "__main__"
  app.run(debug=True)
