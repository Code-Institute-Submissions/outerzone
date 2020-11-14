<h1 align="center">
    <a href="" target="_blank"><img src="" style="center" alt="Outer Zone Logo"></a>
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
Users are able to find out more about the artists, their releases and upcoming gigs. Those who register can buy 
records and merchandise, rate their purchases and speak with fellow fans through the Outer Zone Forum.

---
## User Experience

### Client Goals
The client is a Glasgow-based independent record label, who specialises in electronic music. Prior to the creation 
of this website, their internet presence was spread across a number of different websites, mainly [Soundcloud](https://soundcloud.com/outer-zone) 
and [Bandcamp](https://outerzone.bandcamp.com/). 

The client requested this website in order to:
* increase the profile of the record label.
* showcase the label's artists, their releases, upcoming gigs and media attention.
* provide a one-stop shop for users to find out more about the label and buy their records.
* create a community where electronic music fans can speak with like-minded people.
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
* to review a record they recently bought.
* a way to connect with an online electronic music community.
* details on upcoming gigs.

### User Stories
1. As a new visitor, I want to find out more about Outer Zone and their artists.
2. As a new visitor, I want to browse Outer Zone's releases and merchandise.
3. As a new visitor, I want to register an account so I can connect with others in the Outer Zone forum.
4. As a registered user, I want to purchase a record and other merchandise.
5. As a registered user, I want to update my account details, payment details and avatar.
6. As a registered user, I want to get involved in discussion on the online forum.
7. As a registered user, I want to edit and delete my posts.
8. As a registered user, I want to rate and review my purchases.
9. As someone within the electronic music industry, I want to understand more about Outer Zone and the types of sets their artists play.
10. As someone within the electronic music industry, I want to contact Outer Zone in order to work with them.
11. As admin for the site, I want to be able to moderate the forum and delete posts, where necessary.
12. As admin for the site, I want to be able to view all user accounts and their purchases.

### Wireframes
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
---
## Technologies
---
## Testing 
### Tools 
### Automated Testing
### User Testing
### User Feedback 
### Problem Solving
---
## Deployment 

pip3 install:
django
django-allauth
django-crispy-forms
stripe
Pillow
django-countries

---
## Credits 
### Content 
### Media 
### Code 
### Acknowledgements







**** MY NOTES ONLY - NOT PART OF FINAL README ****

Jonathan 12.11.2020
Checkout
* Order and OrderLineItem. Don't save to the database. Write line total as property on the model.
* Reading to do, Jonathan sent on Slack
* More comments on webhooks. URLs to Stripe documentation. Particularly on the delay on checkout 
* SQLite committed to repo. Add to gitignore, but only later when close to end.
* SECRET_KEY and DEBUG variables 

# Questions
* Where do I store JSON if data needs to be accessed in multiple apps?
# To Do
* Change navbar font to white, whilst still being able to see burger.
* Get MEDIA_URL to work on html (nav logo and product images)
* Products - Get filter by Artist to work.
* Products - use for statement to run through filter artists
* Products - fix margins and positioning of basket
* Change btn hover background-color to wine/turquoise?
* Testing - Lighthouse (in GoogleDev inspect section) analyses site. Can screenshot it
* Testing - Stripe has dummy credit card details that show different errors
* Checkout - Do I need extra css file for checkout?
* Checkout - amend styling of country input

# Done 
* Home - center container on small screens
* Products - search bar not working
* Products - Fix sort by name.
* Basket - fix delete
* Basket - fix update quantity
* Checkout - grand total not pulling through to admin?
* Checkout - move complete order btn to right

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