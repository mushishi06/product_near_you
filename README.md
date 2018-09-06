# product_near_you
Django app API  will allow the user call a API and get back a list of active
items.

2. A rudimentary client so you can visualize the results more easily. The client does not
have any way to communicate with the API so you will need to implement that. To run the
client:

  ```
  $ cd client
  $ python -m SimpleHTTPServer
  ```

3. Four datasets in CSV format:
    * `shops.csv`: shops with their coordinates
    * `products.csv`: products per shop along available quantity and global popularity
    * `tags.csv`: a bunch of tags
    * `taggings.csv`: what tags each shop has


# Launch:

- Clone this repo.

- Create a [virtual env](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv "Virtual env's Setup docs")

	- Install virtual env `pip install virtualenv`

	- `cd product_near_you` and `virtualenv product_near_you`

	- To begin using the virtual environment, it needs to be activated: `source product_near_you/bin/activate`

- Install the dependency (`pip3 install -r requirements.txt`)

- Once all are setup go to `~/product_near_you/basic_api/` (`cd` cmd) and run `python manage.py runserver 0.0.0.0:5000`

# More informations:


This API accept two entries point:

- `GET` on  `/search/?lat=x.xxx&lng=y.yyyylimit=100&radius=50` give a list of products for the shops near the lat and lng.

	The endpoint receive:
	    1. the number (N) of products to return
	    2. a pair of coordinates (the user position)
	    3. a search radius (how far the search should extend)
	    4. optionally, some tags (what types of shops the user wants to see)


- `GET` on  `/search/{name}` give a list of shops who contain name.


PS the Radius is not correctly implemented