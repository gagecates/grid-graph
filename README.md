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

[## View deployed app here!](https://grid-view-gmc.herokuapp.com/).