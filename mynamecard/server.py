#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:54:04 2021

@author: gretapan
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)