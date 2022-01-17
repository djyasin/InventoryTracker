
Book Inventory Tracker

This is a Django application designed to track inventory for book sellers. 



## With this app you can:

- Catalog books with the following information:
    - title, author, description, url, book image, creation date, and category
- Create book categories
- Users can register an account
- Logged in users can add, edit, and delete inventory
- Guests can view the library of books and book details

## Demo

Please follow these steps to run this application locally:
Once you have your project cloned and database set up, you will need to install pipenv. To do this, in terminal run:

```bash
$ pip install --user pipenv
```
Next navigate to you main folder for this project and install pipenv:
```bash
$ pipenv install
```
This will install the requirements needed for this project. 

Finally enter your virtual environment:
```bash
$ pipenv shell
```
From here you can run your server:
```bash
$ python manage.py runserver
```
Now you should be ready to use this project from your local server. To access the site you can go to **[http://127.0.0.1:8000](http://127.0.0.1:8000)** and create an account.

Once you have registered an account, you can add categories via the add category button to populate the database with category options. Once those have been added you can begin to populate the database with books. 
Please see the samples_books.csv for example data.