# campaign-manager
Repository for the campaign manager project.

## General
The campaign-manager is supposed to be a web application, written in *python3*.
The backend webserver is *django* until the application is deployed.

## Naming conventions
Methods in **views.py**: should end with *_view*

## Implemented functionalities

- User Login
- User Registration

## TODO
The following functionalities should be implemented:

- Error handling
- Check for login
- User Logout
- every user can create a campaign
- players have to be invited to a campaign by the creator
- a campaign can have different roles for the users:
  - GM
  - Player
- the creator will automatically be the GM of their campaign
- users can be made GMs by the campaign's creator
- files can be added to a campaign
- files can have three levels of visibility:
  - GM only
  - select player(s)
  - everyone
(- players can create character sheets for their characters)
(- markdown support and online editor for text documents)
(- awesome themes (fantasy/sci-fi))
