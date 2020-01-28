from flask import render_template


def getHomePage():
    return render_template('index.html', title='Home')
