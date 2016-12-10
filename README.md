Notice: Work in progress

# Goal PandaWeb.
This repository tries to kickstart Data Scientists and Data Engineers in getting a working webapp.
So basically connecting the data-based world with the web world.

# Scope.
We will assume some Python based code has been written using the Pandas library.
For the web-app we will initially use the MERN stack (MongoDB/Express/ReactJS/NodeJS) and keep the sample simple. Mern is similiar to the MEAN stack but replaces AngularJS with ReactJs as the frontend library. At this moment the sample code can be tested on a local pc, as the html files are not yet provided by the NodeJS backend. In a later stage we will do this and also show how to use a Python backend using only WerkZeug (the workhorse for Python Flask).

# Directory overview:

1. nodejs: Used by our api backend, single javascript file which acts as our HTTP server
2. python: Hosts ourPython script filling our MongoDB with some sample data using a Panda Dataframe
3. Css/images/javascript : All required directories for our React frontend. Css is for the styling, images for static images, and javascript for our main React component Css and js both have a app.* file for the main application, and subdirectories per component wich will be unified during each build proces (into build.css and build.js). These build files are used within our main index.html file

# Seperate files overview:

1. index.html: the main starting point for our app
2. .gitignore: to prevent node_modules being uploaded to github
3. build.* : Bundled css and javascript files.

# Installation Overview

0. Install your Git client and clone this project
1. NodeJS and Express Backend API
NodeJS is a javascript backend in our cased used as API provider. It will respond to AJAX based calls from our frontend ReactJs component.
We'll be using it in combination with the Express module enabling us act as a HTTP server and does the routing.
2. MongoDB and RoboMongo
The backend NOSQL database which we will fill with some data. RoboMongo is a tool to check the connection and data using a GUI.
3. ReactJs and Babel (and browserify)
The Frontend Javascript library we'll be using is ReactJS. Babel will be used to read our JSX/Es6/es2015 javascript  files and generate javascript files usable by any older browser. JSX is a combination of javascript and XML style notation making the code much clearer compared to nested javascript code. browserify is used to follow all dependencies of a entry javascript file and put all required code in a bundled file.
4. griddle-react
A prebuild ReactJS table component we will use to put in our data. Notice it can't support multiheader tables, but works relatively simple.
5. fetch
Used to make Ajax based calls from our ReactJS frontend to the backend. We will use it to get the data from our NodeJS backend Api.
6. Mongodb MONK
Connector for NodeJS backend to connect to MongoDB and read the data we stored in the database.
7. Python / Pandas / PyMongo
Our initial script will create a Panda dataframe using some dummy data having several datatypes. It will also insert it into MongoDB

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
npm install --save body-parser
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

install mongo , goto https://www.mongodb.com/ and install using the instructions.
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

## 6 MongoDB and MONK for NodeJS

```
npm install --save mongodb@2
npm install --save monk
```

## 7 Python (Anaconda!) / Pandas / PyMongo

https://www.python.org/ and install python v3.
Even better use Anaconda 3 to install Python 3, and Jupyter notebooks and soms required modules
like Werkzeug which you need.

Install these Python modules using Pip afterwards (similiar to Javascript's npm):
```
python -m pip install pymongo
python -m pip install numpy
python -m pip install pandas
```

## 8 (OPTIONAL) : Python as backend , no nodejs

Switch to python subdir and install json-rpc module with Python Pip, example on WIndows
If you don't use Anaconda's Python you have to install Werkzeug using Pip also.
```
pip install json-rpc
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

## 3 Start and test NodeJS

Start the backend API and test it using curl:
```
cd nodejs
node DataService.js
curl --header "Accept:application/json" http://localhost:8080/data
```
This should give you JSON with a message and some data

## 4 Build a new application

From main PandaWeb directory:
```
babel --presets react,es2015 js/source -d js/build
browserify js/build/app.js -o bundle.js
LINUX: cat css/*/* css/*.css | sed 's/..\/..\/images/images/g' > bundle.css
Windows: type css\components\* css\* > bundle.css
```
## 5 Test application:

Open index.html from the File Explorer , using Chrome browser. As some browers don't allow accessing it using the defaults like Edge. (TODO: Check this)
Also TODO , serve the frontend using the backend server so it can be used from a server.

## 6 Optional run using Python backend:

Start Python Werkzueg backend (Flask workhorse):
```
cd C:\Users\Gebruiker\Documents\github\pandaweb\python
python DataService.py
```

Test using another terminal session:
```
python DataClient.py
```

It will return a string  "myquery" we send to our search_text backend function:
```
response is:{'jsonrpc': '2.0', 'id': 0, 'result': '{message: myquery }'}
result is:{message: myquery }
```

TODO: Let this Python backend use our MongoDB backend, and callable from our React Frontend

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
