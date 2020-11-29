<h1 align="center">
    <a href="" target="_blank"><img src="/media/bwlogo.jpg" style="center" alt="Outer Zone Logo"></a>
</h1>

<div align="center">

# Outer Zone Record Label

[Open in GitHub](https://github.com/H4RP3RK/outerzone)

</div>

## Contents Table
1. [Introduction](#introduction)
2. [User Experience](#user-experience)
    - [Client Goals](#client-goals)
    - [Target Audience](#target-audience)
    - [User Goals](#user-goals)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
3. [Design](#design)
4. [Features](#features)
    - [Features on every page](#features-on-every-page)
    - [Features to be implemented](#features-to-be-implemented)
5. [Database](#database)
6. [Technologies](#technologies)
7. [Testing](#testing)
    - [Tools](#tools)
    - [Automated Testing](#automated-testing)
    - [User Testing](#user-testing)
    - [User Feedback](#user-feedback)
    - [Problem Solving](#problem-solving)
8. [Deployment](#deployment)
9. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

---
## Introduction
A website for record label, Outer Zone, in order to showcases the label's artists and build a community of fans.
Users are able to find out more about the artists, their releases and upcoming gigs. All users are able to purchase products and, those 
who register with the site can save their delivery details for later purchases and see a record of previous orders.

---
## User Experience

### Client Goals
The client is a Glasgow-based independent record label, who specialises in electronic music. Prior to the creation 
of this website, their internet presence was spread across a number of different websites, mainly [Soundcloud](https://soundcloud.com/outer-zone) 
and [Bandcamp](https://outerzone.bandcamp.com/). 

The client requested this website in order to:
* increase the profile of the record label.
* showcase the label's artists, their releases and upcoming gigs.
* provide a one-stop shop for users to find out more about the label and buy their records.
* allow others within the industry, such as distributors, gig promoters or journalists, to easily get in touch with the label.

### Target Audience
The target audience are:
- fans of electronic music
- predominately in the 20-45 age bracket
- English speaking
- located anywhere in the world

### User Goals
Users visit the website because they want:
* to find out more about the label and their artists.
* to buy a record or other merchandise.
* details on upcoming events.

### User Stories
1. As a new visitor, I want an introduction to the Outer Zone label and their artists.
2. As a new visitor, I want to browse Outer Zone's releases.
3. As a user of the site, I want to sample the artists' music before I decide to buy.
4. As a user of the site, I want to know about artists' upcoming events.
5. As a user of the site, I want to purchase records.
6. As a user of the site, I want to register for an account.
7. As a registered user, I want to save my delivery details for future purchases.
8. As a registered user, I want to update my delivery details.
9. As a registered user, I want to see a record of my previous purchases.
10. As someone within the electronic music industry, I want to understand more about Outer Zone and the types of sets their artists play.
11. As someone within the electronic music industry, I want to contact Outer Zone in order to work with them.
12. As admin for the site, I want to be able to add products to the site.
13. As admin for the site, I want to be able to edit and delete products on the site.
14. As admin for the site, I want to be able to add artists to the site.
15. As admin for the site, I want to be able to edit and delete artist details on the site.

### Wireframes

#### Member Journey
##### Small Screens
<img src="media/wireframes/small.png" style="center" alt="Wireframe for small screen">

##### Medium Screens
<img src="media/wireframes/medium.png" style="center" alt="Wireframe for small screen">

##### Large Screens
<img src="media/wireframes/large.png" style="center" alt="Wireframe for small screen">

---
## Design
---
## Features

* Register/Login
* Update Details
* Add Avatar
* Join Chatroom
* Rate Tunes
* Buy Records and Merchandise
* Message Record Label
* Profiles on each Artist
* Clips of tunes (soundcloud API?)
* Upcoming Events
* Admin access to update details

### Features on every page
### Features to be implemented
---
## Database 

An SQL database was used for this project. The structure of the relationships between the models are outlined in the diagram below.

<img src="media/ms4_data.png" style="center" alt="Data relationships">
---
## Technologies

* [Gitpod](https://www.gitpod.io/)
* [Github](https://github.com/) - version control and storage of the project
* [Heroku](https://dashboard.heroku.com/) - for deployment of the completed website
* HTML and CSS 
* Javascript - used for accordion function on the artist detail page.
* [JQuery](https://jquery.com/) - Javascript library user for the navbar and search/filter functionality on products page.
* [Django](https://www.djangoproject.com/) - Python web framework.
* [Django Crispy Forms](https://github.com/django-crispy-forms) - styling of Django Forms.
* [Stripe](https://stripe.com/en-gb) - to enable payment through the site.
* [Postgres](https://www.postgresql.org/) - A SQL database used to store project data.
* [AWS](https://aws.amazon.com/) - for cloud storage of the static files and media.
* [Bootstrap](https://getbootstrap.com/) - for the responsive grid layout and navbar. All templates were tailored to the needs of the site. 
* [Google Fonts](https://fonts.google.com/) - used to style the website fonts.
* [Font Awesome](https://fontawesome.com/) - icons for certain buttons.

---
## Testing 

Testing details can be found here in [testing.md](TESTING.md)

---
## Deployment 

### Locally

To run this project locally from your own computer, you must first have an IDE installed, as well as PIP, Python3 and Git.
You should also set up an online account with [Stripe](https://stripe.com/en-gb).

1. Go to the [GitHub page](https://github.com/H4RP3RK/outerzone) for the Outer Zone project, click the 'code' button and download the zip file.
Using Git, the repo can be cloned by typing the following command into your terminal:
```
git clone https://github/H4RP3RK/outerzone
```
2. The repository should now be saved locally, so you can open the folder through your IDE.
3. Install all the required modules for the project, as outlined in the requirements.txt file.
4. Set up your environment variables for the following:
    * "DEVELOPMENT": true
    * "SECRET_KEY"
    * "STRIPE_PUBLIC_KEY"
    * "STRIPE_SECRET_KEY"
    * "STRIPE_WH_SECRET"
5. Migrate the models to create the database by using the commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
6. Create a superuser account in order to access the database through admin by typing the command:
```
python3 manage.py createsuperuser
```
7. Run the program locally by using the command:
```
python3 manage.py runserver
```
8. Add '/admin' to the URL for the locally created website in order to access the admin database. You'll be asked to type in the username and password you created for your superuser account.
9. From the admin database, you'll be able to add items in each of the models. Add products and artists to get the website up and running.

### Heroku

1. Make sure that there is a requirements.txt file. If not, create one using the command:
```
pip3 freeze > requirements.txt
```
2. Create a Procfile by using the command:
```
echo web: python3 app.py > Procfile
```
3. Push the new requirements.txt and Procfile to GitHub using the commands:
```
git add .
git commit "<message>"
git push
```
4. Go to the [Heroku website](www.heroku.com). If you don't already have an account, create one, then log in.
5. Create a new app for the project. You can do this by clicking on the new button at the top left of the screen, then choose "create new app" from the dropdown.
6. You'll be prompted to give the app a unique name and choose the region most appropriate for your location.
7. On the resources tab, set up a new Postgres database. You can use the free plan.
7. Go to settings > reveal config vars and set the following variables:
    * AWS_ACCESS_KEY_ID
    * AWS_SECRET_ACCESS_KEY
    * DATABASE_URL
    * EMAIL_HOST_PASS
    * EMAIL_HOST_USER
    * SECRET_KEY
    * STRIPE_PUBLIC_KEY
    * STRIPE_SECRET_KEY
    * STRIPE_WH_SECRET 
    * USE_AWS
8. Go to the deploy tab of your Heroku dashboard and link your Heroku app with your GitHub. Tick the box for automatic deployment.
9. Back in your IDE terminal, login to Heroku with the command:
```
heroku login -i
```
10. Migrate all your data by using the command:
```
python3 manage.py migrate
```
11. Load in the data one model at at a time, using the command below. Start with the artists file.
```
python3 manage.py loaddata <data name>
```
12. Create a superuser account for yourself using the command:
```
python3 manage.py createsuperuser
```
13. Git add, commit and push your changes (see step 3). Go back to your Heroku dashboard and, once the app build is complete, open the app using the URL provided on settings > domains.
14. Your project should now be live.
15. You can read, create, update and delete data by adding '/admin' to the domain URL and logging in with your superuser details.

---
## Credits 
### Content 
### Media 
### Code 
### Acknowledgements







**** MY NOTES ONLY - NOT PART OF FINAL README ****

pip3 install:
django
django-allauth
django-crispy-forms
stripe
Pillow
django-countries
dj_database_url
psycopg2-binary
gunicorn

Jonathan 12.11.2020
Checkout
* More comments on webhooks. URLs to Stripe documentation. Particularly on the delay on checkout 

Jonathan 27.11.2020

# To Do
* Testing - Lighthouse (in GoogleDev inspect section) analyses site. Can screenshot it
* Testing - Stripe has dummy credit card details that show different errors
* Change photos for smaller screens
* Fix readme logo
* Fix image resolutions on home page 
* Add if statements so only completed links appear on artist page 
* Add link to artist page on products page.
* Products - if no products by that artist, display a message so page can be refreshed
* Profile - add name to page


# Done 
* Get MEDIA_URL to work on html (nav logo and product images)
* Home - center container on small screens
* Home - fix layout of photos
* Home - turn arrows into buttons
* Artists - add artists page
* Events - add events html
* Products - search bar not working
* Products - Fix sort by name.
* Products - Get filter by Artist to work
* Products - use for statement to run through filter artists
* Products - fix margins and positioning of basket
* Basket - fix delete
* Basket - fix update quantity
* Checkout - grand total not pulling through to admin?
* Checkout - move complete order btn to right
* Comments - add comments to show code borrowed from elsewhere
* Mini Checkout - amend layout
* Artist - Get records to show on page
* Events - add model 
* Change navbar font to white, whilst still being able to see burger.
* Why is there overflow on smaller screens?
* Where do I store JSON if data needs to be accessed in multiple apps?
* Login - add styling for anchors
* Buttons - why is btn writing white?
* Fix padding and text size for smaller screens 
* Fonts - vh for headings
* Messages - add messages
* Profile - why is updated details not working?
* Checkout - amend styling of country input
* Products - fix the search bar alignment
* Checkout - Do I need extra css file for checkout?
* Disable verifications step or link to send email
* SQLite committed to repo. Add to gitignore, but only later when close to end.
* SECRET_KEY and DEBUG variables 
* Order and OrderLineItem. Don't save to the database. Write line total as property on the model.
* Reading to do, Jonathan sent on Slack
* Fix arrows on home page
* Give instructions for creating superuser
* Update artist JSON with new fields
* Products - Search bar isn't working.

# Project Requirements
## Main Technologies
* HTML, CSS, JavaScript, Python+Django
* Relational database (recommending MySQL or Postgres)
* Stripe payments
* Additional libraries and APIs

## Mandatory Requirements
A project violating any of these requirements will FAIL
* Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.
* Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).
* Data Modeling: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models beyond the examples shown on the course
* User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).
* User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
* Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, donations, etc. After paying successfully, the user would then gain access to additional functionality/content on the site. Note that for this project you should use Stripe's test functionality, rather than actual live payments.
* Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).
* Use of JavaScript: The frontend should contain some JavaScript logic you have written to enhance the user experience.
* Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
* Version Control: Use Git & GitHub for version control.
* Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
* Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
* Security: Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.

# Assessment Criteria
Your Full-stack Django project will be assessed based on the following criteria:

### Usability and Visual Impact:
* Project Purpose
* UX design
* Suitability for purpose
* Navigation
* Ease of use
* Information Architecture
* Defensive Design
### Layout and Visual Impact:
* Responsive Design
* Image Presentation
* Colour scheme and typography
### Code Quality:
* Appropriate use of HTML
* Appropriate use of CSS
* Appropriate use of JavaScript
* Appropriate use of Python
* Appropriate use of the template language
* Appropriate use of Django
### Application Features:
* App logic
* Cross-app logic
* E-commerce
* Authentication and Security
### Software Development practices:
* Directory Structure and File Naming
* Version control
* Testing implementation
* Testing write-up
* Readme file
* Comments
* Data store integration
* Deployment implementation
* Deployment write-up