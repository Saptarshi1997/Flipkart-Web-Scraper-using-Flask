import re
from urllib.request import urlopen as ureq
import pymongo
from pymongo import mongo_client
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")


@app.route('/scrap', methods=['POST'])
def search_box():
    searchstring = request.form['content'].replace(' ', '')
    try:

        dbconn = pymongo.MongoClient("mongodb://localhost:27017/")
        db = dbconn["Scrapperdb"]
        mycollection = db[searchstring]

        rev = mycollection.find({})
        k = list(rev)

        if len(k) > 0:
            reviews = mycollection.find({})
            return render_template("results.html", reviews=reviews)

        else:
            url = "https://www.flipkart.com/search?q=" + searchstring

            uClient = ureq(url)
            all_product_page = uClient.read()
            uClient.close()

            soup = BeautifulSoup(all_product_page, 'html.parser')
            product = soup.find_all("div", {"class": "_13oc-S"})

            reviews = []
            for item in product:
                product_page = "https://www.flipkart.com" + item.a["href"]
                item.div.div.a['href']
                review_req = requests.get(product_page)
                htmlcontent_review = review_req.content
                review_soup = BeautifulSoup(htmlcontent_review, 'html.parser')
                review_class = review_soup.find("div", {"class": "col JOpGWq"})

                try:
                    review_attr = review_class.find_all(
                        'a', attrs={'href': re.compile('/product-reviews')})
                    review_href = review_attr[-1]['href']
                    review_url = "https://www.flipkart.com" + review_href

                    for page in range(1, 4):
                        review_page_link = review_url + '&page=' + str(page)
                        page_req = requests.get(review_page_link)
                        page_htmlcontent = page_req.content
                        page_soup = BeautifulSoup(
                            page_htmlcontent, 'html.parser')
                        page_product_review = page_soup.find_all(
                            "div", {"class": "col _2wzgFH K0kLPL"})

                        for review in page_product_review:
                            try:
                                stars = review.div.div.text
                            except:
                                print("No Rating")
                            try:
                                commentheads = review.div.p.text
                            except:
                                print("No Commentheads")
                            try:
                                comtag = review.find_all(
                                    'div', {'class': 'row'})
                                commentbodies_bbbbb = comtag[1].div.div.text
                                if 'READ MORE' in commentbodies_bbbbb:

                                    commentbodies = commentbodies_bbbbb.replace('READ MORE', '...')
                            except:
                                print("No commentbodies")

                            dictionary = {"Product": request.form['content'], "Rating": stars, "Title": commentheads,
                                          "Description": commentbodies}
                            mycollection.insert_one(dictionary)
                            reviews.append(dictionary)
                except:
                    print('no reviews')
            return render_template('results.html', reviews=reviews)

    except:
        return 'something went wrong'


if __name__ == "__main__":
    app.run(debug=False)
