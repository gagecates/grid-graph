# Electric Grid Graph

This project utilizes React and Python/Flask to provide the user a specific portion
of the electric grid according to a bus number and level depth.

The front end has input validation to ensure the correct data to be fetched.

The backend operates as follows:

1. JSON file is parsed and nodes and edges are extracted.
2. Adjacency list is created from the data.
3. Front end provides users requested starting node and level.
4. Breath First Search algorithm used to provide specific nodes.
5. Pyton libraries networkx and matplotlib used to provide graph plot.
6. Backend serves plot to be displayed on front end for user.

[View deployed app here!](https://grid-graph-bf4b1268c069.herokuapp.com/).

## To run the app locally:

1. Download the zip file or clone the repository. To clone, go to the directory
   that you would like to clone it to and open the terminal. Run:

```
git clone https://github.com/gagecates/grid-graph.git
```

2. Navigate to the root of the project named 'sample app'
3. You can choose to run a virtual environment to download the dependencies or not.

### Virtual Environment:

```
pip install virtualenv (depending on version of pip might need to use pip3)
```

### Mac/Linux:

```
source mypython/bin/activate
```

### Windows:

```
mypthon\Scripts\activate
```

4. With (or without) virtual environment running, install dependencies:

```
pip install -r requirements.txt
```

5. In the terminal run the following to set up the flask app.

### Mac/Linux:

```
$ export FLASK_APP=app
$ flask run
```

### Windows:

```
set FLASK_APP=app
flask run
```

6. The flask server should now be running on localhost
7. To run the React project, navigate to the front-end directory:

```
cd front-end
```

8. Run the app:

```
npm start
```

9. The React app should also run on localhost and allow fetches to Flask server.
