# ShopNow Ecommerce Application

This is a  REST API based ecommerce app in Django
where Users can sign up and shop as well as view and like other Products.
Admin can add Vendors having products with specific features

## Features

- Signup
- Signin
- Admin interface to create products
- Admin interface to create Vendor
- User interface to view products
- User interface to add product to cart

## Runnning app

This app has a Makefile where frequntly run commands have been written. Below are the commands which can be run on terminal to execute some actions.

- make run: This command starts the app on port 8005 (I set this port as default). You can open the make file and set a port of your choice.

- make superuser: This command allows you create a superuser from the terminal using `valid email address` and password

- migration: I created this command to help me quickly make migrations and auto generate migration files containing changes that need to be applied to the database

- migrate: This command makes the actual modifications to your database, based on the migration files

- test: This command analyzes an application program interface (API) to verify it fulfills its expected functionality, security, performance and reliability

## Other Features

- Swagger APIDOCs is used for API documentation and schema generation. visit `localhost:8005/api/schema/` and `localhost:8005/api/docs/` go generate schema and docs
- Circle-ci is configured to run the continous integration pipelines
- black is used for code formatting
