Squirrel-Tracker
=============

### Background Description

A web application project created with Django framework which could track sightings of squirrels in New York City Central Park.Users are allowed to add and update squirrel data. The statistics of data and map visualization of data are also available.


### Contributors
Project Group Allison & Yanqiu Section 1

UNIs: [yx2627, jx2430]

Note: Since Allison used multiple devices to  write the project, authors' name Allison, Allison1212, and Allison Xu all represent the contributor Jiaxue(Allison) Xu.

Prerequisites
------------
Python 3 and Django web framework are required for this application.



Main Functions
------------
The application allows users to create, update the squirrels' sighting data, and browse the general data statistics. The application also provides a map visualization of the sightings' locations in New York City Central Park

### Homepage
The homepage provides users choices to enter sightings page or map page by clicking "Squirrels Sightings" and "Squirrels Map Visualization". Users could go back to homepage by clicking "Homepage" on navigation bar from all sightings pages.


### Sightings

#### View All Sightings
All the sightings' IDs and dates can be viewed on the main sightings page and users can get access to the detailed information and update them. Users could view this page by clicking "Squirrel Sightings" on homepage or click "All Sightings"on navigation bar from all sightings pages.

    located at: /sightings/

#### Create a New Sighting
A new sighting can be created by users by clicking the "New Sighting" on navigation bar from all sightings pages and submit their information on a new page.

    located at: /sightings/add/


#### View Sightings Statistics
The general sightings data statistics can be browsed by clicking "Stats Summary" on navigation bar from all sightings pages.

    located at: /sightings/stats/


#### Update a Sighting Data
Users can update sighting information by click "update" on the main sightings page.

    located at: /sightings/<unique-squirrel-id>


### Map Visualization
A map visualizing all the locations of squirrels' sightings in the New York City Central Park. Users can view at most 100 locations on the map. The map page could be redirected from homepage by clicking "Squirrels Map Visualization" button on homepage.

        located at: /map/
