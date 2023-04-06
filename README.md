# Covid-BackEnd
## Author : ASAD HIJAW

### Installation
 - git clone https://github.com/asadhijj/Covid-BackEnd.git
 - pip install -r requirements.txt
 - python manage.py migrate (to set up the database)
 - python manage.py runserver (to start the server)
 
### API Endpoints
- /api/countries/ (GET) - Get a list of all countries.
- /api/countries/create/ (POST) - Create a new country record.
- /api/countries/<int:pk>/delete/ (DELETE) - Delete a specific country record by ID.

