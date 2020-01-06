from flask import Flask, render_template, redirect, url_for
import datetime
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    left = [1, 2, 3, 4, 5]
    # heights of bars
    height = [10, 24, 36, 40, 5]
    # labels for bars
    tick_label = ['one', 'two', 'three', 'four', 'five']
    # plotting a bar chart
    plt.bar(left,
            height,
            tick_label=tick_label,
            width=0.8,
            color=['red', 'green'])

    # naming the y-axis
    plt.ylabel('y - axis')
    # naming the x-axis
    plt.xlabel('x - axis')
    # plot title
    plt.title('My bar chart!')

    plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'static/images/plot.png'))


    return render_template('dashboard.html',
                           current_time=current_time,
                           plot='/static/images/plot.png')

if __name__ == '__main__':
    app.run()