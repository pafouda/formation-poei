from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
  return "Ceci est une page d'accueil"



  @app.route('/citation/<author>')
  def hello():
    return render_template('homepage.html', author=author)


app.run(host="0.0.0.0", port=8085)