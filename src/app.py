from flask import Flask

# Creating application
app = Flask(__name__)

# Run application
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)