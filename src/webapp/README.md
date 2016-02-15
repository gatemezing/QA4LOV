## List of dependencies

- Quepy Library 
- Python 2.7
- Flask 
- Datalift to store LOV dataset

## How to launch the src/webapp
- Download the repository `src/webapp`
- Launch Datalift containing an instance of [LOV dataset](http://lov.okfn.org/dataset/lov/) published at `http://localhost:9091/sparql/data`. 
- If different endpoint, change the value in the file `main.py` in Line 15: `sparql = SPARQLWrapper("http://localhost:9091/sparql/data")` to the corresponding endpoint
- `$ ./app.py`  
- The server starts at http://127.0.0.1:5000/
- Enter a question 
- Et voila!
