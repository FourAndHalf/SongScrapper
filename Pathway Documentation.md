## Documentation

( 2023 )

1. Created Django - Python Project for LinkSaver Project
2. Created Django - Python Project for SpotifyDownloader
3. Created Django - Python Project for YoutubeLinkSaver

( 2025 )

19/01/2025

1. Cleaned up the project
2. Conditioned it to only one project
3. Added the SongSaver Project to get the data
4. Added the spotify_auth file and spotify_service file to get link with my spotify application

25/01/2025

1. Added data in models.py to make way to multi-select dropdown in link.html
2. Added the forms.py file to select the data from the html page to the model
3. Detailed the form submission code in views.py file
4. Added code and files to get data from a config.yaml file
5. Added authentication account in Neon.Tech account
6. Selected Neon.Tech postgres database as database for the project

01/02/2025

1. Added Schema for tables in Neon.Tech Database and inserted some values for the multi-select dropdown
2. Added Logging library for the project

02/02/2025

1. Added the database connection to the project
2. Configured logger to a centralized folder
3. Created serializers.py for REST api framework
4. Created repository.py for getting data from database
5. Created SpotifyService project for interacting with spotify api

03/02/2025

1. Added the services folder in songsaver to write all the logic in
2. Added the youtube library to download the mp3 file of the music
3. Removed the separate services folder to write logic and wrote all the logic in src folder as per industry standards
4. Have to add celery for background downloading
5. Make this all come together and test the application before further proceedings

04/02/2025

1. Wrote the code in main.py to work this all together
2. Added necessary logging of data along the way
3. Wrote some unit tests to test the working of the application

07/02/2025

1. Tested the application and the song download works
2. Created a beautiful loader and chose to create a colorful and fun website for the song scrapper.
3. Chose to create pages to enter the link and song details, an admin page to create songs and genres / codes
4. An user login page / registration page if the user wants to download playlists
5. A listing page of the songs / playlists created by the user, when clicking on one of them shows the songs in that list
6. Another listing of the popular songs / playlists as inputted by the user
7. Added logo for the website
8. Thought of idea of creating a course for powerful web designs

08/02/2025

1. Created the function in serializers.py to serialize the json and push data
2. Added a preloader page for the website and selected some animations for them
3. Have to set some ease-ness in going to the page

11/02/2025

1. Created dashboard page

12/02/2025

1. Trying to get the data from the database to populate the dropdown

13/02/2025

1. Created the post method for saving the playlist

15/02/2025

1. Changed the logo of the project

17/02/2025

1. Best way to move forward is to recreate the website with minimal controls and needs.
2. Create only a single dashboard and download page and maybe a listing page to show the top tracks in spotify
