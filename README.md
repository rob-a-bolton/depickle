# Depickle

Depickle your pickled data.  
Usage: `./depickle.py -i ./somePickle -o ./depickledData.json`

Handles regular py primitives that `json` would export fine, as well as:

* Sets (converted to lists)
* ndarray (converted to lists)
* partial functions (converted to strings)

