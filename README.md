
# Summerhouse reservation

Summerhouse reservation is an app for my family to make reservations of our summerhouse we share on the Swedish west coast. This is a first mvp (minimum viable product) which I belive will fullfill our basic need for making plans for our holidays in the summerhouse. But of course there are features to add in the future.
Because it will only be used by my family I don't want anyone to be able to register for an account by them self. My family will have to sign in to enter. Account must be set up by Admin. 
For this demo it is open for anonymous to view posts and there is also 4 accounts in place for testing.
Users: Sam (Admin), Lisa, Kalle, Anna
Password: SummerOf69

### Small screens (iPhone 4)
![Screenshot](assets/images/screenshot_iphone4.png)

### Middle large screens (iPad Air)
![Screenshot](assets/images/screenshot_air.png)


### Large screens (Desktop)
![HomeScreenshot](assets/images/screenshot_home.png)


# Features

## Existing Features
* Home page
  * Navigation Bar
  * List of all reservations.
  * If signed in a link to reservation form.
* About page
  * Short description for my family members.
* Calendar page
  * Calendar view to see all reservations.  
* Profile link
  * If signed in a link to the profile form.
* Sign In link
  * Link to sign in form.
* Sign out link
  * If signed in a link to sign out.

### Navigation Bar
![navbarscreenshot](assets/images/screenshot_navbar1.png)

- Featured on all pages, the full responsive navigation bar includes links to the Logo, Home page, About, Calendar and Sign in page and is identical in each page to allow for easy navigation.
- When signed in there are more links in the navigation bar. New reservation, Profile and Sign Out.

![navbarscreenshot](assets/images/screenshot_navbar2.png)


### The landing page
![HomeScreenshot](assets/images/screenshot_home.png)

### The about page
![Screenshot](assets/images/screenshot_about.png)

The about page gives information about our wonderful summerplace. 

### The calendar page
![Screenshot](assets/images/screenshot_cal.png)


### The sign in page
![Screenshot](assets/images/screenshot_signin.png)

![Screenshot](assets/images/screenshot_signin_wrong.png)

### The signed out page
![Screenshot](assets/images/screenshot_signout.png)

### The reservation detail page
![HomeScreenshot](assets/images/screenshot_detail.png)

### New reservation page
![HomeScreenshot](assets/images/screenshot_new.png)

### Signed In reservation detail page
![HomeScreenshot](assets/images/screenshot_mypost.png)

### Delete reservation page
![HomeScreenshot](assets/images/screenshot_delete.png)

### Profile page
![HomeScreenshot](assets/images/screenshot_profile.png)

### Update profile page
![HomeScreenshot](assets/images/screenshot_accountupdate.png)

### Admin page
![HomeScreenshot](assets/images/screenshot_admin.png)

## Starting point

The idé was to build a booking app for my familys summerhouse. We are always having trouble to handle the planing for the summer holidays. We have tried to schedule who and when with personal calendars or shared documents, with no success so I thought a web app could help. This is small and easy mvp, but hopefully it can grow. I started with three scetches. Both Calender view and Profile was added on the way as I was building and learning new things. 

### Scetches

![Screenshot](assets/images/scetch_home.png)
![Screenshot](assets/images/scetch_home_signed_in.png)
![Screenshot](assets/images/scetch_newpost.png)


## Features left to implement
- Change password.
- Improve Calendar view on how reservations is displayed.
- Check if a room is already booked
- Integrate with Slack channel
- Todo 
- Wiki


# Testing
Test is done manual on browsers Chrome, Safari and Firefox. Responsiveness has been tested with browsers development tools. It is also tested on iPhone X and iPad Air.
Users: Sam (Admin), Lisa, Anna and Kalle. Password: SummerOf69

* Sign in with admin account Sam in Admin Page (https://samsite.herokuapp.com/admin/) to register test users and add profiles.
  * Add new user - outcome: User Anna was created with password SummerOf69.
  * Create profile for user Anna without choosing a profile image - outcome: A profile is created with a default profile image
* Connect to https://samsite.herokuapp.com/ - outcome: Landed on Sommerhouse home page.
* Click on link About - outcome: Landed on About page, https://samsite.herokuapp.com/about
* Click on link Calendar - outcome: Landed on Calendar page, https://samsite.herokuapp.com/calendar
* Click on link Home - outcome: Landed on Home page, https://samsite.herokuapp.com/ with the two newest booking shown. If more then  two reservation exist pageing buttons appear under the two bookings
* Click on link Sign In - outcome: Landed on Sign in form, https://samsite.herokuapp.com/signin

### As test user Anna: 
* Sign in with username Anna and no password - outcome: Field message pops up, "Please fill in this field"
* Sign in with username Anna and wrong password - outcome: A message in red appears, "Please enter a correct username and password. Note that both fields may be case-sensitive."
* Sign in with username Anna and right password - outcome: Landing back to home page. New reservation and Profile link appears in the navigation bar.
* Click on link New reservation - outcome: Open New reservation form
* Click on Post with empty Title and comment fields - outcome: Field message pops up in the first empty field, "Please fill in this field"
* Click on Post with a Title and comment - outcome: Reservation is saved and a view with reservation info appears with an update and delete button.
* Click on update - outcome: Reservation form is opened 
* Updated reservation with other dates and comments - outcome: Back to reservation info appears with an update and delete button.
* Click on delete button - outcome: A confirmation page is shown with two buttons, "Yes, delete" and "Cancel". If "Cancel" is clicked reservation info appears with an update and delete button. If "Yes, delete" is clicked post is deleted and home page is shown.
* Click on Profile link - outcome: Profile form appears. Here must the user add an email address and can upload a new profile image. When Update button is clicked a green message "Your account has been updated!" appears
* Click on others reservations - outcome Reservation info is shown, but without update or delete button
* Click on Calender link- outcome: Landed on Calender page with all reservations
* In Calendar page click Previous or Next month - outcome: Page updates with previous or next month dates


# Validator Testing

### HTML
No errors were returned when passing through the official W3C validator.
### CSS
No errors were found when passing through the official (Jigsaw) validator. Although there are still some css issues to handle because different browsers render css in different ways. Chrome works best for this application. 
### Accessibility
The Lighthouse test tool show good result in accesibility
![Screenshot](assets/images/screenshot_lighthouse.png)

# Bugs
 * Styling bugs still exists on how different browsers render css.
 * Home page needs to be adjusted on small screens like iPhone 4.

# Deployment
The site was deployed Heroku with a Postgres database on ElephantSQL cloud service and static files is handled by cloud service Cloudinary.
App is deployed as follows:
* Heroku is connected to GitHub repository Samssite.
* Under settings in Heroku config vars is set for connection to the Elephant and Cloudinary. Port and Django secret key is also set.
* In deploy section in Heroku choose branch main to deploy and press button "Deploy Branch". Look in the log that everything is installed correct.

The live link can be found here - [(https://samsite.herokuapp.com/)](https://samsite.herokuapp.com/)

# Credits
Example code and design is used from:
- Code Institute 
- Corey Schaffer
- Hui Wen
- Read the Docs
- Django, Bootstrap documentation

# Media
My photos.
