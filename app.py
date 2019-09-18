from flask import Flask,render_template

import pandas as pd
import numpy as np


app = Flask(__name__)

@app.route('/')
def guide():
    return INTRO()

@app.route('/introduction')
def INTRO():
    return render_template('introduction.html')

@app.route('/page1')
def PAGE1():
    return render_template('page1.html')

@app.route('/page2')
def PAGE2():
    return render_template('page2.html')

@app.route('/page3')
def PAGE3():
    return render_template('page3.html')

@app.route('/page4')
def PAGE4():
    return render_template('page4.html')

@app.route('/page5')
def PAGE5():
    return render_template('page5.html')

@app.route('/page6')
def PAGE6():
    return render_template('page6.html')

@app.route('/page7')
def PAGE7():
    return render_template('page7.html')


if __name__ == '__main__':
    app.run()
