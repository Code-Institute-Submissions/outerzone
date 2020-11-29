## Testing 

### Tools 
The following tools were used to test the website code and layout throughout the development.

* Google Chrome Developer Tool - used throughout the project to test code and scalability.
* Unicorn Revealer - used throughout the project to resolve layout issues with web pages.
* Contrast Ratio - used to ensure that colours meet readability guidelines.
* W3C Markup Validation - used to validate HTML code, although this proved difficult with JINJA also included in the code.
* W3C CSS Validation - used to validate CSS code.
* JS Hint - used to validate JS code
* Pylint - to validate Python code. Some "line too long" errors were ignored as it was felt that the code was most reader friendly in its current format. Warnings of 

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
    1. Typing in 
    




#### Basket
1. Check link directs to shopping basket.
2. If no items have been put in the basket, check that message appears "basket is empty".
3. If items have been added to the basket, check that relevant items, quantity, subtotal and total appear.
4. Check that item quantity can be changed in the basket by updating the number and clicking on the edit icon.
5. If item quantity is updated, ensure that subtotal and total update appropriately.
6. Check that items can be deleted from basket by clicking on the bin icon.
7. If item is deleted, check that basket total also updates.
8. Return to shop button returns to products page.
9. Checkout button directs to checkout.



### User Feedback 
### Problem Solving