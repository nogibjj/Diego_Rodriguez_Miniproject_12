[![Build and Push Docker Image](https://github.com/nogibjj/Diego_Rodriguez_Miniproject_12/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Diego_Rodriguez_Miniproject_12/actions/workflows/hello.yml)

# IDS706-Miniproject #12
## File Structure 
```
Diego_Rodriguez_Mini_Project#12/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
|   └── workflows/cicd.yml
├── mylib/
│   ├── __init__.py
|   └── lib.py
├── static/
|   └── images/plot.png
├── templates/
│   ├── dashboard.html
|   └── input_page.html
├── uploads/
|   └── wdi.csv
├── .gitignore
├── Data_summary.md
├── Dockerfile
├── Makefile
├── README.md
├── app.py
├── requirements.txt
└── test_main.py
```
## Purpose of project
The purpose of this project is to present a web service using `DockerHub` capabilities. This repository create a simple dashboard using `Flask`. The app receive a `CSV` file to create a scatter plot and descriptive information of the data. As reference, the data used in this repository correspond to the World Development Indicator from the World Bank, but any data could be uploaded into the app. 

###  Dockerfile

The `Dockerfile` in the main folder contains the image commands to run a `Flask` app. The process is as follow:

1. docker build -t <app_name> for creating the docker image.
2. docker run -p 5000:5000 <app_name> for running the dockercontainner.
3. docker push <user_name>/<app_name> to push the app to Dockerhub.

The `Makefile` contains simplify commands to run dockers syntax with from the CL.

###  Templates
1. `input_page.html` constains the data fields to receive a csv.file and the variables of interest for a scatter plot
2. `dashboard.html` produce the graph and the summary statistics for the `Flask` app

###  Walkthrough

1. Docker build:
   <img width="853" alt="Screenshot 2024-11-22 at 6 36 06 PM" src="https://github.com/user-attachments/assets/c885ecc0-aa2f-4f79-83ea-130406e15d4d">
2. Docker run:  
   <img width="1067" alt="Screenshot 2024-11-22 at 6 29 55 PM" src="https://github.com/user-attachments/assets/87669e9a-5104-4866-9985-e6a3dfc3033a">
3. Input page:
  ![Screenshot 2024-11-22 at 6 29 00 PM](https://github.com/user-attachments/assets/1a02fde0-dcd4-4f10-bb54-10212df36af9)
4. Dashboard creation:
  ![Screenshot 2024-11-22 at 6 29 09 PM](https://github.com/user-attachments/assets/d4cf1924-01c5-4a44-b963-1050cffe47be)
5. Docker Push:
  <img width="714" alt="Screenshot 2024-11-22 at 6 52 22 PM" src="https://github.com/user-attachments/assets/e58f6995-a719-4c95-92e7-caa837f0d952">
6. Dockerhub image:

   ![Screenshot 2024-11-22 at 9 14 22 PM](https://github.com/user-attachments/assets/07fb8e3b-e186-4d66-b868-56e483806781)




