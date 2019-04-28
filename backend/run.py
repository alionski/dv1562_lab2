from datetime import datetime

import requests
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, request

app = Flask(__name__)
Base = declarative_base()
engine = create_engine("postgresql://docker:docker@lab_2_db/lab_2_db",
                       pool_size=10, max_overflow=20)
Session = sessionmaker(bind=engine)


class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    city = Column(String(100))
    timestamp = Column(DateTime())


def save_city(city):
    session = Session()
    new_request = Request(city=city, timestamp=datetime.utcnow())
    session.add(new_request)
    session.commit()
    session.close()


def get_cities():
    session = Session()
    cities = [r.city for r in session.query(Request.city).distinct()]
    session.close()
    return cities


@app.route("/", methods=['GET'])
def hello():
    cities = get_cities()
    return render_template("main.html", cities=(cities if cities else ""))


@app.route("/", methods=['POST'])
def weather():
    city = request.form.get("city")
    if not city:
        return render_template("main.html")
    url = "https://wttr.in/" + city + ".png"
    filename = city + ".png"

    r = requests.get(url, allow_redirects=True)
    open("static/images/"+filename, 'wb').write(r.content)
    save_city(city)

    cities = get_cities()
    return render_template("main.html", city=city, filename=filename, cities=(cities if cities else ""))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
