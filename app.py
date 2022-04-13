import os
import csv
import requests
import re
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__, template_folder='template')


@app.route("/")
def home():
    URL = "https://techiesneh-ts-m3u.vercel.app/api/getM3u?sid=1239416157_D&sname=PL%20Mishra&ent=1000000071_1000000156_1000000471_1000000500_1000000647_1000000711_1000000985_1000001051_1000001124_1000001131_1000001274_1000001296_1000001303_1000001368_1000001512_1000001573_1000001685_1000001694_1000001817_1000000001&tkn=VEnGKKq27rpbrIZZ23UORQ1JAreyp1MN"
    
    page = requests.get(URL)
    filename = 'old.txt'
    with open(filename, 'w') as file_object:
        file_object.write(str(page.text))
        
    fo = open("old.txt")
    fo.seek(195076)
    sep = fo.read(195076 - 192984)
    print (sep)    
    
    newfilename = 'scrapped.txt'
    with open(newfilename, 'w') as file_object:
        file_object.write(str(sep))
        
        
    return render_template("index.html", title="hello world", scrapped=(sep))




    
if __name__ == '__main__':
    app.run()
