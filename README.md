Notice: Work in progress
To read: https://apihandyman.io/do-you-really-know-why-you-prefer-rest-over-rpc/

# Goal PandaWeb.
This repository tries to kickstart Data Scientists and Data Engineers in getting a working webapp.
So basically connecting the data-based world with the web world.

# Scope.
We will assume some Python based code has been written using the Pandas library and a working webbased MVP is to be created.
For the web-app we will initially use the MERN stack (MongoDB/Express/ReactJS/NodeJS) and keep the sample simple. Mern is similiar to the MEAN stack but replaces AngularJS with ReactJs as the frontend library. It will use the new ES2015 (ES6) Javascript notation.

At this moment there are 2 todo's in progress:
```
1. At the moment of writing a backend using Python (Flask) will also be written.
The reason for this is that Python models build by data scientists tend to use views (=code) on top of data.
Therefor just connecting to a sql or nosql database to get data and show it will not be enough.
A full Javascript stack is less likely to be used because of this. Unless the Python based model using Panda
can be rewritten in Nodejs, which is probably not the case.

2. Also one note, many prebuild ReactJS components tend to assume all data will be send to the client in 1 shot.
This makes a very convinient component but in real life the data will be way too big. So this means the components
should be rewritten to make Ajax based call which will transport partial data.
```

# Directory overview:

1. nodejs: Used by our api backend, single javascript file which acts as our HTTP server. It will host our Rest API backend and the frontend files.
2. python: Hosts our Python script initially filling our MongoDB with some sample data using a Panda Dataframe
3. Css/images/javascript : All required directories for our React frontend. Css is for the styling, images for static images, and javascript for our main React component . Css and js both have a app.* file for the main application, and subdirectories per component wich will be unified during each build proces (into build.css and build.js). These build files are used within our main index.html file

# Seperate files overview:

1. index.html: the main starting point for our app
2. .gitignore: to prevent node_modules being uploaded to github
3. build.* : Bundled css and javascript files. These files will be created by the build proces.

# Installation Overview

0. Install your Git client and clone this project
1. NodeJS and Express Backend API
NodeJS is a javascript backend in our cased used as Rest API provider. It will respond to AJAX based calls from our frontend ReactJs component.
We'll be using it in combination with the Express module enabling us act as a HTTP server and enabling the routing.
2. MongoDB and RoboMongo
The backend NOSQL database which we will fill with some data using a Python script. RoboMongo is a tool to check the connection and data using a GUI.
3. ReactJs and Babel (and browserify)
The Frontend Javascript library we'll be using is ReactJS. Babel will be used to read our JSX/Es6/es2015 javascript  files and generate javascript files usable by any browser. JSX is a combination of javascript and XML style notation making the code much clearer compared to nested javascript code. browserify is used to follow all dependencies of our entry javascript file and output of required code is put in a bundled file during the build.
4. griddle-react
A prebuild ReactJS table component we will use to put in our data. Notice it can't support multiheader tables, but works relatively simple.
5. fetch
Used to make Ajax based calls from our ReactJS frontend to the backend. We will use it to get the data from our NodeJS backend Api.
6. Mongo for NodeJS
To connect our backend API Layer (Nodejs) to our database Mongo
7. Python / Pandas / PyMongo
Our initial script will create a Panda dataframe using some dummy data having several datatypes. It will also insert it into MongoDB
Also we have a Python data API backend DataService.py if we dont want to use NodeJS. A utility script mongo_util.py will help use connect to MongoDB.

# LETS INSTALL

IMPORTANT after cloning the repository (step 0) change current directory to this repository.

## First install Git:
Install git client on your PC or server
Start a terminal or dos prompt
Clone the repository (git clone <the repo url as provided within github>)
Afterwards make sure you cd into the clonded PandaWeb directory.

## 1 NodeJS
Go to http://nodejs.org and install NodeJS for you OS (this will also install npm , make sure it's in your PATH)
```
npm install --save express
#npm install --save body-parser
npm install --save cors
```

As a bonus will describe how to install it on linux AWS if you use this OS:
Download x64 from nodejs.org for linux first
```
cd $HOME (ec2-user)
wget https://nodejs.org/dist/v6.9.1/node-v6.9.1-linux-x64.tar.xz
tar -xvf node-v6.9.1-linux-x64.tar.xz
<check out bin dir path for npm and node)
<put in .bashrc and restart session>
```
## 2 MongoDB

install mongo using default settings, goto https://www.mongodb.com/ and install using the instructions.
As a bonus we will describe how to install on Linux AWS if you use AWS.

### To install on amazon linux:
create file /etc/yum.repos.d/mongodb-org-3.2.repo

Put these lines in:
```
[mongodb-org-3.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.2.asc
```
To install MongoDB:
```
sudo yum install -y mongodb-org
```

### RoboMongo
Install robomongo (https://robomongo.org/ ) to test your connection afterwards. It's a nice GUI to check your data also.

## 3 ReactJS and Babel

```
npm install --global browserify
npm install --global babel-cli
npm install --save-dev react
npm install --save-dev react-dom
npm install --save-dev babel-preset-react
npm install --save-dev babel-preset-es2015
```

## 4 griddle-react

```
npm install react --save
npm install griddle-react --save
```

## 5 React-fetch

```
npm install react-fetch
```

## 6 MongoDB for NodeJS

```
npm install --save mongodb@2
#npm install --save monk
```

## 7 Python (Anaconda!) / Pandas / PyMongo

https://www.python.org/ and install python v3.
Even better use Anaconda 3 to install Python 3, and Jupyter notebooks and soms required modules
like Werkzeug which you need if you use the Python based API backend instead of NodeJS.

Install these Python modules using Pip afterwards (similiar to Javascript's npm):
```
python -m pip install pymongo
python -m pip install numpy
python -m pip install pandas
python -m pip install flask-httpauth
pip install -U flask-cors
```



# Building and testing the app

## 1 Start MongoDB as described and the connection using RoboMongo.

To start MongoDB on Windows (notice the install):
```
cd C:\Program Files\MongoDB\Server\3.2\bin
mongod --dbpath D:\mongo_data
```

Or if you use Linux AWS: To start and monitor MongoDB:
```
sudo service mongod start  
sudo cat /var/log/mongodb/mongod.log  
```

Now start RoboMongo to check the connection (use default everywhere)

## 2 Fill the MongoDB with data

go to the Python sub dir
```
python panda_to_mongo_db.py
```
Use RoboMongo again to see the new data

## 3 Start the backend (NodeJS/Express or Python/Flask)

If using NodeJS: Start the backend API and test it using curl:
```
cd nodejs
node DataService.js
```

If you use Python/Flask as backend instead of NodeJs:
```
cd python
python DataService.py
```

Test the backend first:
```
//Test url using these command line statements:
curl -i -X GET http://localhost:3000/pandaweb/all
curl -i -X GET http://localhost:3000/pandaweb/range/1/10
curl -i -X DELETE http://localhost:3000/pandaweb/delete/<some id like 5845cb0f8f9bfe03f813ba0c>
```

## 4 Build a new application

From main PandaWeb directory:
```
babel --presets react,es2015 js/source -d js/build
browserify js/build/app.js -o bundle.js
LINUX: cat css/*/* css/*.css | sed 's/..\/..\/images/images/g' > bundle.css
Windows: type css\components\* css\* > bundle.css
```
## 5 Test application:

The http://localhost:3000 url will show our fantastic application.

# To build a productions version:

After building execute this to minimise to CSS and Javascript code.
```
uglify -s bundle.js -o __deployme/bundle.js
cssshrink bundle.css > __deployme/bundle.css
cp index.html __deployme/index.html
cp -r images/ __deployme/images/
```

# Bonus:

## Install Atom

This is a nice editor , go to atom.io and install this editor.
From the welcome page within the editor after installation click on install packages. Some nice ones can be found after searching for nodejs and python:

Examples:
```
es-lint (javascript spelling)
mini-map
```
