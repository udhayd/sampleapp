#! /usr/bin/python3

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
  return "Welcome to Docker Container world, Lets Explore further. Cheers !!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
