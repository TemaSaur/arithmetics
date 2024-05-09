# Project title

## Installation

To run the app using pypy:

* get the appropriate version of pypy from [here](https://www.pypy.org/download.html)
* install requirements from the requirements.txt

		path/to/pypy -mpip install -r requirements.txt

* run the app via

		path/to/pypy -m uvicorn main:app --host 0.0.0.0 --port 80 --reload