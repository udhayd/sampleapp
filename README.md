# Simple Web Application

This is a simple web application using [Python Flask] 
  
  Below are the steps required to get this working on a ubuntu linux system.
  
   
## 1. Install python3 & its required dependencies
  
  Python and its dependencies

    apt-get install -y python3 python3-setuptools python3-dev build-essential python3-pip

## 2. Install and Configure Web Server

Install Python Flask dependency

    pip3 install flask

- Copy app.py or download it from source repository

## 3. Start Web Server

Start web server

    python3 app.py & 
    
## 4. Test

Open a browser and go to URL

    http://<IP>:8080            ===> 'Welcome to Docker Container world, Lets Explore further. Cheers !!'
