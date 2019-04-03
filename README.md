# To implement User Interface for Cloud HW2
This assignment requires us to develop a dynamic webpage that uses Javascript requests to send the user-inputted data to the REST-API we built, receive the results, and then display them on our webpage without refreshing the whole page again 

# Configuration Details:
1. To connect to the aws cloud service:
- ssh -i "red.pem" ubuntu@ec2-18-217-158-13.us-east-2.compute.amazonaws.com

2. After logging in:
- sudo apt-get update 
- sudo apt-get install python3-pip python3-dev python3-setuptools git
- sudo apt-get install language-pack-en
- sudo locale-gen en_GB.UTF-8

3. Install Django and djangorestframework
- pip3 install django
- pip3 install djangorestframework
- pip3 install django-import-export

4. Use git command to clone the project from github to var folder:
- sudo -i
- cd /var
- git clone https://github.com/reddyts09/cloud234.git

5. HW3 contains some files and their contents are as follows:
- apps.py:
  ```from django.apps import AppConfig
     class Hw3Config(AppConfig):
     name = 'hw3'
- urls.py:
  ```from django.urls import path
     from . import views
     #from django.views.decorators.csrf import csrf_exempt
     urlpatterns = [
     path('', views.index),
     ]
- views.py:
  ```from django.shortcuts import render
     def index(request):
     return render(request, 'index.html')
6. The main web application index.html that generates a GRAPH is:
   ```<!DOCTYPE HTML>
          <html>
          <head>
          <title>Meteorological Forecast</title>
          {% load static from staticfiles %}
          <style>
          body {
             background-repeat: no-repeat;
             background-size: 1200px 900px;
          }
          </style>
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
          <script src="http://canvasjs.com/assets/script/canvasjs.min.js"></script>
          <script>
          $(document).ready(function() {
              $('#button').on('click', function () {
                  var startDate = $('#date').val();
                  var TMAXPoints = [];
                  var TMINPoints = [];
                  var url = "/forecast/" + startDate +"/"
            $.getJSON(url, function(result) {
              for (var i = 0; i <= result.length - 1; i++) {
                TMAXPoints.push({
                  label: result[i].DATE,
                  y: parseInt(result[i].TMAX),
                });
                TMINPoints.push({
                  label: result[i].DATE,
                  y: parseInt(result[i].TMIN),
                });
              }
              console.log(result);
              var chart = new CanvasJS.Chart("chartContainer", {
                title:{
                  text: "Weather Forecast"
                },
                data: [{
                  type: "line",
                  dataPoints: TMAXPoints,
                        },
                {
                  type: "line",
                  dataPoints: TMINPoints,
                }]
              });
              chart.render();
            });
              });
          });
          </script>
          </head>
          <body background="{% static "img/w1.png" %}">
            <h1 align = "center" style="color : green">Meteorological Forecast</h1>
            <div style="text-align:center";>
              <input type = "number" id = "date" placeholder="Enter Date in YYYYMMDD" />
              <input type="button" id = "button" value = "Get Forecast"/>
              <br>
            </div>
          <br>
          <div id="chartContainer" style="height: 300px; width: 100%;"></div>
          </body>
          </html>

7. The main web application index.html that generates a TABLE is:
   ```<!DOCTYPE html>
      <html>
      <head>
      <title>Meteorological Forecast</title>
      {% load static from staticfiles %}
      <style>

        h1 {
          color: green;
        }

        th, td {
          padding: 5px;

        }
        table th {
          width: 30%;    
          background-color: green;
        }

        body {
           background-repeat: no-repeat;
           background-size: 1200px 900px;
        }

        </style>
        </head>
        <body background="{% static "img/w1.png" %}">
        <h1 align="center">Meteorological Forecast</h1><br>
        <center><label for="date">ENTER THE DATE:</label>
        <input type="number" id="date" min="20130101" max="99991231" required>
        <button id="button" onclick="weather()">Get Forecast</button></center>

        <div id="demo"></div>
        <script>
        function weather() {
          var date_obj = document.getElementById("date");
          if (!date_obj.checkValidity()) {
            document.getElementById("demo").innerHTML = date_obj.validationMessage;
          } 
          else {
            var x, txt = "";
            var url = '/forecast/'+date_obj.value;
            var ourRequest = new XMLHttpRequest();
            ourRequest.open('GET', url); 
            ourRequest.onload = function(){
                var ourData = JSON.parse(ourRequest.responseText);
                txt += "<br><br><table border=2 align='center' style='width:50%' id='t01'><tr><th>DATE</th><th>TMAX</th><th>TMIN</th></tr>";
            for (x = 0; x < 6; x++) {
                txt += "<tr><td align='center'>"+ourData[x].DATE+"</td><td align='center'>"+ourData[x].TMAX+"</td><td align='center'>"+ourData[x].TMIN+"</td></tr>";
            }
            txt += "</table>"
            document.getElementById("demo").innerHTML = txt
            };
        ourRequest.send();
      } 
    }

            </script>

            </body>
            </html>

8. The main cloud234 contains the file urls.py and its contents are as follows:
   ```from django.contrib import admin
      from django.urls import path, include
      #from django.views.decorators.csrf import csrf_exempt
      from rest_framework_swagger.views import get_swagger_view

      schema_view =  get_swagger_view(title = "WeatherAPI")

      urlpatterns = [
    
      path('', include('hw3.urls')),
      path('admin/', admin.site.urls),
      path('', include('hw2.urls')),
      path('swagger/', schema_view),
      ]

9. To access the UI Webpage type in the following AWS instance command in the url:
   ```
   http://ec2-18-217-158-13.us-east-2.compute.amazonaws.com

# Built With
- Django,AWS: Web Framework used
- HTML, CSS, JavaScript, AJAX:Web Development Applications used
- Database: sqlite3
- Github: repository for code

# Acknowledgements
I Thank Prof.Giridhar for provding me with the opportunity to work on this project that deals with hands on experience with Cloud, AWS, Resful API, Few of the well known web development applications and Django framework.
