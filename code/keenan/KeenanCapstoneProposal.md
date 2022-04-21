<!-- Here is My Capstone Proposal -->

# **-- Placeholder Name -- Synesthesia**


## Project Overview
This project is intended to help a spotify user visualize some of the information regarding their music listening habits in a clean visual format.  The product will end along the lines of the 'Year in Review' feature that they provide to users, but available real-time instead of once annually. The spotify app home interface for both desktop and mobile is also extremely busy, so the intent is also to reduce the visual clutter to show just what the user is interested in, and not endless rows of random recommendations. The user will be required to login in with an existing spotify account so they can view their data using the Spotify API.

Libraries/Frameworks: Python, Vue, Django Rest Framework (Serializers). Maybe a visualization library for nice to have features.


## Features


### User Stories
**As a spotify user I want to see what my listening habits were like for the past few weeks/few months/few years with regards to top songs or artists.**
**Tasks:**
-Create a Home page with login link
-Create a login page / use the Spotify API to allow user to login to the app with their own  account information
-Display the output from the spotify 'Get User's Top Items' (two options for the query and display: Song or Artist) 
<!-- Do I want users to toggle the search or do I want to display both? -->
-TBD:There may be an opportunity to show interesting info about artists based on the API response info for artists

**The user wants to look at the genre information for their listening history**
**Tasks:**
-The genre data is embedded per artist, so I'll need to loop through the data and count the number of occurrences of each genre. Whether it is the 'TopSongs' or 'TopArtists' output is dependent on the response metadata format.
-Graph or display music genre info displayed on a new page from the welcome page.

**The user wants to see related artists to their favorite.**
**Tasks:**
-Include functionality to link artist images to the Spotify API's related artists call.

**The user wants to be able to preview songs that they've listened to.**
**Tasks:**
-In the song icon / model include the functionality to play a song with a click / hover over the image or text.

**The user wants to be able to see themetic elements between the songs that they've listened to.**
**Tasks:**
-Utilize spotify API to check 'happiness', energy, and danciness

**The user wants to see the relative popularity of the songs / artists they listen to**
-Utilize spotify API to display popularity.  This could be incorporated into a little mini game to compare which artist is more popular.



## Data Model
'User'
<!-- Custom user model functionality needs to be included at the beginning! -->
'TopSongs'
'TopArtists'
'Genres'
'Song' 



## Schedule
**Week 1**
-Complete project start and Spotify Account Sign in Functionality (MVP)
-Complete login page and top 50 landing page (MVP)
-Create a custom user model just in case I want to include additional functionality (MVP)
-Create API links to pull and display a users top 50 songs (MVP)
-Start general UI feel with color theming / song model (MVP)


**Week 2**
-Complete the loop functionality to tally most popular genre data (MVP)
-Create a page to view the users top artists.  Likely need to piggy back on the loop functionality from the genres (MVP)
-Dial in clean UI feel for the pages above 

**Week 3**
-Get the site up and running on heroku or similar?
-Include functionality to link artist images to the Spotify API's related artists call (nice to have)
-Utilize spotify API to check 'happiness', energy, and danciness (nice to have)


**Week 4**
-In the song icon / model include the functionality to play a song with a click / hover over the image or text (nice to have)
-Utilize spotify API to display popularity (nice to have)