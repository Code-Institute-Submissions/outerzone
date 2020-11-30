## Testing 

### Tools 
The following tools were used to test the website code and layout throughout the development.

* Google Chrome Developer Tool - used throughout the project to test code and scalability.
* Unicorn Revealer - used throughout the project to resolve layout issues with web pages.
* Contrast Ratio - used to ensure that colours meet readability guidelines.
* W3C Markup Validation - used to validate HTML code, although this proved difficult with JINJA also included in the code.
* W3C CSS Validation - used to validate CSS code.
* JS Hint - used to validate JS code
* Pylint - to validate Python code. Some "line too long" errors were ignored as it was felt that the code was most reader friendly in its current format.

### Automated Testing
Automated unit testing was used to test the code in the artists app. [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.3/#) was used to determine the amount 
of code tested and produce a report. This can be found as an html file in the [htmlcov folder](https://github.com/H4RP3RK/outerzone/tree/master/htmlcov) of this repo.

### User Testing
#### All Pages 

* Header
    1. Click on the Outer Zone logo to verify that it links to the home page.
    2. Hover over all nav bar links to check that the text/icon turns grey.
    3. Click on the navbar burger to ensure that the navigation menu drops down.
    4. Click on each navigation link to ensure that it directs to the appropriate page.
    5. Shopping basket reflects the total price of items in the basket at any one time.
    When user is not logged in, check that:
    6. the navigation menu shows Sign Up and not logout.
    7. The text underneath the person icon is Login, and links to a login page.
    When user is logged in, check that:
    8. the navigation menu shows logout and not Sign Up.
    9. The text underneath the person icon is Profile, and links to the user's profile page.
    When logged in as superuser, check that: 
    10. links to Add Product and Add Artist appear in the navigation menu.

* Responsive Design
    1. Burger appears on small and medium screens.
    2. Full navigation bar shows on large screens.
    3. Font size changes in line with the view height of the device.
    4. All images and text are visible/readable on all screen sizes.
    5. Grid design responds as expected, dependent upon screen size.

#### Home Page 
* Links 
    1. Links appear blue and turn grey when hovered over.
    2. Artists and Buy links lead to artists page and products page, respectively.
    3. When clicking on downward arrows, page smooth scrolls to the next block of text. 
    4. When clicking on upward arrow, page smooth scrolls to the top of the page.

* Images 
    1. Images remain fixed when scrolling.
    2. Focal point of images are visible on different screen resolutions. 
    3. Images change appropriately, dependent upon screen resolution.

#### Artists 
* Artist List
    1. All artists in the database are listed on the page.
    2. The image and artist name match.
    3. Both the image and artist name link to the appropriate artist page.

#### Artist Detail
* Data 
    1. The appropriate name, image, description, social media links, youtube video, products and events appears for each artist.

* Buy 
    1. If products for the artist are listed in the database, their image appears in the Buy container.
    2. Each image links to the appropriate product detail page.

* Events 
    1. If events for the artist are listed in the database, they appear on the page.
    2. The events are listed in chronological order.
    3. The accordion is closed when the page is loaded.
    4. By clicking on the accordion title, the detail appears.
    5. The event detail matches the title.
    6. The downward arrow disappears when the event is open.
    7. More than one event can be opened at a time.

* Listen 
    1. If a youtube URL for the artist is listed in the database, a YouTube video appears in the Listen section.
    2. The YouTube video width flexes to fit inside the Listen container on all screen resolutions.
    3. The YouTube video plays the appropriate video.
    4. The video can link to YouTube and opens in a new tab.

* More 
    1. If social media links are listed for the artist, they appear in this section.
    2. Each icon links to the appropriate web page.
    3. Each web page opens in a new tab.

#### Products
* Products
    1. All products listed in the database appear as separate cards on the product page.
    2. Images, names, artists and prices all match the information in the database.
    3. The artists' display names appear rather than their names (ie the artist names are capitalised and have spaces between words).
    4. All products link to the appropriate product detail page.

* Search and Filters
    1. When search term is typed and search button pressed, products with a matching title or artist name display.
    2. Invalid search terms display a blank screen. ******Add a message*******
    3. The casing of the search input will not impact the search results.
    4. Pressing search button without a search term displays an error message to ask user to enter search term.
    5. Filter by artist shows a list of all artists listed on the database.
    6. Clicking on each artist will display only their products.
    7. If an artist does not have any products on the database, a blank screen appears. ******Add a message*******
    8. Sort by price, artist and title orders all the products appropriately.

#### Product Detail
* Data
    1. The appropriate image, title and price for the product appears.

* Form 
    1. The quantity is automatically set to 1.
    2. The quantity can be increased or decreased using the arrows on the number input.
    3. The quantity cannot drop below 1 and cannot got past 99.
    4. When adding a new product to the basket, a success message appears to show that the relevant product and quantity has been added.
    5. When increasing the quantity of a product already in the basket, a success message appears to show that the quantity has increased to the appropriate figure.
    6. The shopping basket icon total amends as the user clicks the add to basket button.

#### Basket
 * Basket products
    2. If no products have been put in the basket, message appears "basket is empty".
    3. If products have been added to the basket, the relevant items, quantity, subtotal and total appear.
    4. The product quantity can be changed in the basket by updating the number and clicking on the edit icon.
    5. If product quantity is updated, ensure that subtotal and total update appropriately.
    6. Products can be deleted from basket by clicking on the bin icon.
    7. If product is deleted, check that basket total also updates.

* Links
    1. Return to shop button returns to products page.
    2. Checkout button directs to checkout.

#### Checkout
* Product Details
    1. Product details match the details in the basket.
    2. Total charged to the card reflects cost of items in the basket.
    3. The Adjust Basket button leads back to the basket page.

* Payment Details 
    1. Form cannot be submitted if any of the fields with the asterix(*) are left blank.
    2. Form can be submitted if only the fields with the asterix(*) are completed.
    3. Form can be submitted with all fields completed.
    4. Email address field can only accept input that follow email convention.
    5. Save delivery details can be ticked and unticked.
    6. If ticked, delivery details save to profile.
    7. If unticked, delivery details do not save to profile. 
    8. If user already has delivery details saved on their profile, these prepopulate the form.
    9. The form cannot be submitted without card details.
    10. The card details must match a credit/debit card number convention.
    11. Clicking the complete order button processes payment if form is completed appropriately.
    12. If form fields are missing or completed inappropriately, error messages will appear at the appropriate field when the complete order form is clicked.
    13. If unsuitable credit card details are used, clicking the complete order button will direct to processing page and then redirect back to the checkout page. An error message should appear to show the user the issue.

#### Order Confirmation
* Alert
    1. An alert appears to confirm the order number and inform user that a confirmation email has been sent to them.
    2. A confirmation email is sent to the user's email address.

* Order Details
    1. The appropriate order details are listed.

#### Profile
* Delivery Details
    1. The delivery details are prepopulated with the details input on the user's order.
    2. Any field can be amended and updated by clicking on the update details form.
    3. Updated details pull through to the checkout page.

* Order History
    1. If the user has made previous orders, the details display in a list.
    2. The order number links to further details about the order.

#### Add Product
* Form
    1. Only superusers can access this page.
    2. If non-superuser tries to access this page, a message appears to inform user that only superusers can access.
    3. The artist field displays a dropdown of all artists on the database.
    4. Products cannot be added for an artist that is not already on the database.
    5. The form cannot be submitted without all fields marked with an asterix(*) are completed.
    6. An image can be uploaded from the user's local system and added to the form.
    7. By clicking the add product button, the product is added to the database, appears on the products page, the relevant artists' page and has its own product detail page.
    8. Clicking cancel redirects the user to the products page.

#### Add Artist
* Form
    1. Only superusers can access this page.
    2. If non-superuser tries to access this page, a message appears to inform user that only superusers can access.
    3. The artist field displays a dropdown of all artists on the database.
    4. Products cannot be added for an artist that is not already on the database.
    5. The form cannot be submitted without all fields marked with an asterix(*) are completed.
    6. An image can be uploaded from the user's local system and added to the form.
    7. By clicking the add artist button, the artist is added to the database, appears on the artists page, on the dropdown on product filter page and has its own artist detail page.
    8. Clicking cancel redirects the user to the artists page.

#### All Auth
* Sign Up
    1. Form cannot be submitted until all fields are completed.
    2. Verification email is sent to user's email address.
    3. The link within the email address redirects to confirmation that user's account is set up.

* Login
    1. Sign Up link appears blue and directs to sign up page.
    2. Valid user and password details signs user in.
    3. Invalid combination shows relevant error messages.
    4. Forgot password directs to forgot password page.

* Forgot Password 
    1. Sends email to user with link to reset password.

* Sign Out 
    1. Only those who are logged in are shown Logout link.
    2. Text appears to ask user if they are sure they wish to log out.
    3. The remain signed in button redirects to the home page.
    4. The sign out button signs out the user and redirects them to the home page. An alert appears to confirm that user has been signed out.

### User Feedback 
Friends, family and colleagues were enlisted to test the site on mobile phones, tablets, laptops and desktops. They also tested the site 
using different bandwidths to ensure that the there were no significant loading time lags.

The following changes were made in response to user feedback:
* The fixed scroll background images for the home page were not working on mobiles.
* The chevrons on the home page needed to make it clear that they were for scrolling throught the page.
* User feedback discovered that verification emails were not sending when users tried to sign up. This was amended by adding a new EMAIL_HOST_PASS to the Heroku config variables.

#### Bugs 
A bug was discovered with the admin database that prevented me from updating products. The products were listed with the image as the 
first column. When the image was clicked, it simply displayed the image rather than the expected response of directing to the editable 
view of the product. This problem was resolved by changing the order of the products admin listing in admin.py.

It was also discovered the Apple mobile devices disable fixed scrolling of background images. This was an issue that was not identified when using the Google Devs mobile view and
only became clear when user testing was carried out on different mobile devices. This issue was resolved by creating two different layouts for the home page - one for small screens and large screens.
The large screen view kept the fixed background image and the small screen provided a full width image. If it were not for the looming deadline, a more elegant solution would have been found.