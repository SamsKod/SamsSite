
# Summerhouse reservation

Summerhouse reservation is an app for my family to make reservations of our summerhouse we share on the Swedish west coast. This is a first mvp (minimum viable product) which I belive will fullfill our basic need for making plans for our holidays in the summerhouse. But of course there are features to add in the future. Because it will only be used by my family I don't want anyone make an account by them self and they must sign in to enter. Account must be set up by Admin. For this demo it is open for anonymous and there is also 3 accounts in place for testing.


![Screenshot](assets/images/RideaBikeScreenshot.png)

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

![MenuScreenshot](assets/images/MenuScreenshot.png)

- Featured on all pages, the full responsive navigation bar includes links to the Logo, Home page, About and Sign up page and is identical in each page to allow for easy navigation.
- This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button.

### The landing page

![HomeScreenshot](assets/images/IndexScreenshot.png)

The landing includes a photograph with text overlay to allow the user to see exactly which location this site would be applicable to.

### The about page

![Screenshot](assets/images/AboutScreenshot.png)

The about page gives information about ability to bicycle train in a group and where and when the training starts. 

### The calendar page

![Screenshot](assets/images/FormScreenshot.png)

Here you can add name and email address to join a group training session and information on what level you are and which distances you prefer.

### The sign in page

![Screenshot](assets/images/FormScreenshot.png)

Here you can add name and email address to join a group training session and information on what level you are and which distances you prefer.

### The sign in page

![Screenshot](assets/images/FormScreenshot.png)

Here you can add name and email address to join a group training session and information on what level you are and which distances you prefer.

### The sign in page

![Screenshot](assets/images/FormScreenshot.png)

A form to sign in with username and password.


## Features left to implement
- Change password.
- Improve Calendar view on how reservations is displayed.
- Check if a room is already booked
- Integrate with Slack channel


# Testing
Test is done manual on browsers Chrome, Safari and Firefox. Responsiveness has been tested with browsers development tools. It is also tested on iPhone X and iPad Air.
Users: Sam (Admin), Lisa and Kalle. Password: SummerOf69

* Signed in with admin account Sam in Admin Page to register more test users and add profiles.
* Tested navigation bar to see that all links worked correct.
* Sign in as test user Lisa and made i new reservation.
* As test user Lisa updated reservation with other dates and comments.
* As test user Lisa deleted reservation.
* As test user Lisa viewed profile and added a profile image.
* As test user Lisa viewed others reservations and made sure update or delete button was not available.
* 

More automated test should be added.

# Validator Testing

### HTML
No errors were returned when passing through the official W3C validator.
### CSS
No errors were found when passing through the official (Jigsaw) validator. Although there are still some css issues to handle because different browsers render css in different ways. Chrome works best for this application. 
### Accessibility
The Lighthouse test tool show good result in accesibility
![Screenshot](assets/images/LighthouseTest_img.png)

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
Is my own photos.
