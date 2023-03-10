from flask import Flask
from flask import render_template

app = Flask(__name__)
if __name__ == "__main__":
    app.run()
app._static_folder ='templates/static/' 


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')    
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=False)


