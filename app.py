import os
import csv
import requests
import re
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__, template_folder='template')


@app.route("/")
def home():
   ghhv=requests.Session()
   head={"Host":"techiesneh-ts-m3u.vercel.app",
      "user-agent":"Mozilla/5.0 (Linux; Android 11; SM-F127G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}


   url=ghhv.get('https://techiesneh-ts-m3u.vercel.app/api/getM3u?sid=1239416157_D&sname=PL%20Mishra&ent=1000000071_1000000156_1000000471_1000000500_1000000647_1000000711_1000000985_1000001051_1000001124_1000001131_1000001274_1000001296_1000001303_1000001368_1000001512_1000001573_1000001685_1000001694_1000001817_1000000001&tkn=VEnGKKq27rpbrIZZ23UORQ1JAreyp1MN',headers=head)
   starhindi=url.text.split("Star Sports 1 Hindi HD")[0].    split("#KODIPROP:inputstream.adaptive.license_key=")[80].split()[0]

   print(starhindi)
  
   return render_template("index.html", title="hello world", streamurl=(starhindi))




    
if __name__ == '__main__':
    app.run()
