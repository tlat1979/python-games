from flask import render_template


def getHomePage():
    return render_template('home.html', title='Home')
