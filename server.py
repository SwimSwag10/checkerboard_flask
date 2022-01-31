from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
  return render_template("index.html", x=8, y=8, x_color="white", y_color="black")

@app.route('/<int:y_num>')
def x_num(y_num):
  return render_template("index.html", x=8, y=y_num, x_color="white", y_color="black")

@app.route('/<int:x_num>/<int:y_num>')
def num(x_num,y_num):
  return render_template("index.html", x=x_num, y=y_num, x_color="white", y_color="black")

@app.route('/<int:x_num>/<int:y_num>/<string:x_color>')
def num_x_color(x_num,y_num,x_color):
  return render_template("index.html", x=x_num, y=y_num, x_color=x_color, y_color="black")

@app.route('/<int:x_num>/<int:y_num>/<string:x_color>/<string:y_color>')
def num_color(x_num,y_num,x_color,y_color):
  return render_template("index.html", x=x_num, y=y_num, x_color=x_color, y_color=y_color)

if __name__=="__main__":
  app.run(debug=True)