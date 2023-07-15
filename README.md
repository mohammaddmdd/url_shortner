# URL Shortener Project
This project is a URL shortener application built using Django.
It allows users to create short URLs for long web addresses and redirect visitors to the original links.
## Features
   - User authentication: Users can sign up, log in, and log out of the application.
   - URL shortening: Users can generate short URLs for their long web addresses.
   - Redirects: Visitors can access the short URLs and get redirected to the original links.
## Installation
Clone the repository:

``` https://github.com/mohammaddmdd/url_shortner.git ```

Navigate to the project directory:

``` cd url-shortener ```

Create a virtual environment:

``` python -m venv venv ```

Activate the virtual environment:

For Windows:

``` venv\Scripts\activate ```

For macOS and Linux:

``` source venv/bin/activate ```

Install the project dependencies:

``` pip install -r requirements.txt ```

Set up the database:
  Create a PostgreSQL database and update the DATABASES configuration in settings.py with the appropriate details.

  Apply the database migrations:

  ``` python manage.py migrate ```

## Usage ##
Start the development server:

``` python manage.py runserver ```
Sign up for a new account or log in with your existing credentials.

Use the application to generate short URLs for your long web addresses.

## Deployment ##
To deploy the URL shortener application to a production server, follow these steps:

Set up a production environment with a web server (e.g., Nginx) and a WSGI server (e.g., Gunicorn).

Configure the web server to serve static files and proxy requests to the WSGI server.

Update the necessary settings (e.g., ALLOWED_HOSTS) in settings.py for the production environment.

Set up the database for the production environment and update the DATABASES configuration in settings.py accordingly.

Collect the static files:

``` python manage.py collectstatic ```

Configure the WSGI server (e.g., Gunicorn) to run the application.

Start the WSGI server and web server.

Access the application using the appropriate domain or IP address.


