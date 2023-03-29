Django Ecommerce Site with PayPal Integration, AJAX, and CRUD Operations
This is a Django ecommerce website that enables users to purchase items using PayPal's web payment system. It also supports cart management and account creation for a seamless shopping experience. In addition, it provides CRUD operations for managing user accounts.

Features
Integration with PayPal's JavaScript SDK for secure and reliable payment processing
AJAX integration for a smooth and responsive user experience
User account creation and management for easy checkout and order tracking
Cart management for storing and retrieving user's selected items
Guest checkout functionality for non-registered users
Product search and filtering for quick and easy browsing
CRUD operations for managing user accounts, including create, read, update, and delete functionality
Installation
Clone the repository to your local machine
Install the required dependencies listed in the requirements.txt file using pip
Set up a PayPal developer account and create a new app to get your client ID and secret key
Copy the example.env file to .env and update the PAYPAL_CLIENT_ID and PAYPAL_CLIENT_SECRET variables with your own keys
Run the Django development server using python manage.py runserver
Visit http://localhost:8000 in your web browser to view the site
Usage
Register for a new account or log in if you already have one
Browse the available products and add items to your cart
View your cart and update the quantity or remove items as desired
Proceed to checkout and complete the payment process using PayPal's web payment system
Manage your account by performing CRUD operations on your user profile, including updating your personal information and deleting your account if desired