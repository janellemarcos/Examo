**Github:** https://github.com/artak10t/Examo

**Team Members**

* Spartak Gevorgyan: https://github.com/artak10t
* Matthew Chan: https://github.com/blankss
* Janelle Marcos: https://github.com/janellemarcos
* Dat Tri Tat: https://github.com/DatTriTat

**Date:** 9/16/2021

**Product Name:** Examo

**Problem Statement:** App that provides learning tools for students to study.

**Non-functional Requirements:** The website has to be in the English language, FindTextInFiles should process not slower than 2 seconds, notes should render in the form of flashcard





# Sign-up

Create a new user account

## Actors

1. User

## Preconditions

* None

## Triggers

* Click the sign-up button

## Primary Sequence

1. User opens sign-up page
2. User inputs unique username
3. User inputs password that has to be at least 6 symbols
4. User clicks sign-up

## Primary Postconditions

* Account created

## Alternative Sequences

### Alternative Trigger

* Invalid or empty password or email input
* Username is already in use

### Alternative Postconditions

* Highlight password or username input box with red and tell that input is invalid
* Highlight username input box and tell that username is already in use




# Log-in:

Logs a user into their account.

## Actors

1. User

## Preconditions

* User’s account should exist already.

## Triggers

Click Log-in button
## Primary Sequence

1. User inputs username
2. User inputs password
3. User clicks Log-in

## Primary Postconditions

* Users are logged in and can access their resources.

## Alternate Sequences
1. User inputted an invalid username or password.

2. Prompt the user to enter the username and password again.

   


# Input markdown file and output flash cards:

User import data to the app from markdown file and output flashcards.

## Actors

1. User

## Preconditions

* User’s account should be logged in.

## Triggers

* User clicks “Create flash cards” button

## Primary Sequence

1. Users click the log-out button when they are logged in.
2. User clicks“input your data” button
3. User clicks“Create” button

## Primary Postconditions

* Text editor in markdown format opens up.
* Flash cards have been created.

## Alternate Sequences
* File cannot be empty so flash cards will not be created.


  

# Delete account

Deletes the user’s account.

## Actors

* User

## Preconditions

* User’s account should be logged in.

## Triggers

* Click the delete button in the settings menu.

## Primary Sequence

1. Users navigate to the settings page.
2. Users click on the delete account button.
3. Website prompts confirmation for the account to be deleted.
4. User clicks “yes” on the confirmation pop-up.
5. Log the user out of the account and delete their credentials.

## Primary Postconditions

* Users are logged in.

## Alternate Sequences

1. User clicks “no” on the pop-up.
2. Account is not deleted and will back out of the pop-up.





# Log-out

Logs a user out of their account.

## Actors

1. User

## Preconditions

* User’s account should be logged in.

## Triggers

* Click Log-out button

## Primary Sequence

1. Users click the log-out button when they are logged in.

## Primary Postconditions

* Users are logged in and can access their resources.

## Alternate Sequences

* None.




# NotesToPDF

Convert notes into pdf and download them

## Actors

1. User
2. Notes

## Preconditions

* User has to be signed-in
* User has to have notes created

## Triggers

* Click the Download PDF button

## Primary Sequence

1. User selects one or more notes
2. User clicks Download PDF button

## Primary Postconditions

* Notes convert into PDF and start downloading

## Alternative Sequences

### Alternative Trigger

* Notes were not selected

### Alternative Postconditions

* Throw error notification that says "Notes are not selected"




# NavigateBetweenNotes:

Ability, similar to hyperlinks, to navigate between notes using this syntax [[other note]]

## Actors

1. User
2. Notes

## Preconditions

* Original note has to be created
* Other note has to be created

## Triggers

* Clicked on the hyperlink [[other note]]

## Primary Sequence

1. User opens the original note
2. User clicks on the hyperlink[[other note]]
3. Browser opens new tab with the other note

## Primary Postconditions

* Notes convert into PDF and start downloading

## Alternative Sequences

### Alternative Trigger

### Alternative Postconditions

* Throw error 404, the other note was not found

  


# FindTextInFiles

Search text and list notes that have that text in them.

## Actors

1. User
2. Notes

## Preconditions

* User has to be signed-in
* User has to have notes created

## Triggers

* Click Search button

## Primary Sequence

1. User inputs text that he wants to find in notes
2. User clicks the search button
3. Backend searches in database notes that have the user inputted text in them and lists the results

## Primary Postconditions

* Lists notes that have the user inputted text in them

## Alternative Sequences

### Alternative Trigger

* User inputted text was 3 or less symbols.
* Note was not found

### Alternative Postconditions

* Highlight search bar red and tell that that key search word has to be 3 or more symbols
* Show empty list of notes that say note was not found




# CreateTimeBlock

Create time block for note when to study them

## Actors

1. User
2. Note

## Preconditions

* User has to be signed-in
* Note has to be created

## Triggers

* Edit note and set time block dates

## Primary Sequence

1. User clicks Edit Note
2. User inputs time block start and end dates/times using date/time picker
3. User clicks Save button

## Primary Postconditions

* Time block has been set

## Alternative Sequences

### Alternative Trigger

### Alternative Postconditions




# Use pomodoro timer

User creates pomodoro timer .

## Actors

1. User

## Preconditions

* User’s account should be logged in.

## Triggers

* User click “Pomodoro Timer” button

## Primary Sequence

1. User input minutes for Pomodoro length, short break length, long break length.
2. User clicks “Set” button
3. User clicks “Start” button to use
4. User clicks "Stop" button to stop using

## Primary Postconditions

* Pomodoro Timer has started.
* Pomodoro Timer has stopped.

## Alternate Sequences

* Error message displayed: “Need to set time”.





# Add note to to-do list

User adds note to to-do list.

## Actors

1. User

## Preconditions

* User is logged in and has created notes.

## Triggers

* User clicks “add to to-do list” button.

## Primary Sequence

1. User selects notes to add to-do list.
2. User clicks “Save” button

## Primary Postconditions

* Notes have been added to to-do list.

## Alternate Sequences

* Notes were not selected.




# Check off to-do item

User marks an item on to-do list to show that it has been dealt with..

## Actors

1. User

## Preconditions

* User is logged in and have items on to-do list.

## Triggers

* User clicks “to-do list” button

## Primary Sequence

1. The user marks each note or item as completed.
2. User clicks “Save” button

## Primary Postconditions

* To-do list is updated.

## Alternate Sequences

* None.




# TrackWorkHoursPerDay

Tracks how many hours user was studying

## Actors

1. User

## Preconditions

* User has to be signed-in

## Triggers

* User signs-in

## Primary Sequence

1. User signs-in
2. WorkHours starts counting
3. User signs-out WorkHours stops counting

## Primary Postconditions

* WorkHours count
* After one day WorkHours reset

## Alternative Sequences

### Alternative Trigger

### Alternative Postconditions




# RenderWorkHoursPerDay

Render work hours per day

## Actors

1. User

## Preconditions

* User has to be signed-in

## Triggers

* User signs-in

## Primary Sequence

1. User signs-in

## Primary Postconditions

* Render work hours per day

## Alternative Sequences

### Alternative Trigger

### Alternative Postconditions




# Render markdown notes
## Summary
 
The user converts markdown notes into text with features (title bold, italics, etc).
 
## Actors
User
Markdown notes
 
## Preconditions
* User is logged in and has created notes in markdown format
 
## Triggers
User selects “render markdown notes” button
 
## Primary Sequence
User selects notes to render
User clicks “render markdown notes” button

## Primary Postconditions
* Markdown notes are rendered
 
## Alternate Sequences
* Notes were not selected so render doesn’t start
 
 
 

# Share notes with other people
## Summary
The user shares notes with other users.
 
## Actors
User that shares notes
User that receives notes
Markdown notes
 
## Preconditions
* User is logged in and has created notes in markdown format
 
## Triggers
User selects “share notes” button
 
## Primary Sequence
User selects notes to share
User clicks “share notes” button
User inputs username of other users that they want to share the notes with
User clicks “share” button

## Primary Postconditions
* Notes are being shared
 
## Alternate Sequences
* Notes were not selected and aren’t shared
*No username was inputted
*Error message displayed: “information missing”
 



# Add new note
## Summary
User creates a note.
 
## Actors
User
 
## Preconditions
* User is logged in
 
## Triggers
User selects “create note” button
 
## Primary Sequence
User selects “create note” button

## Primary Postconditions
* Text editor in markdown format opens up




# Edit note
## Summary
User edits a note.
 
## Actors
User
 
## Preconditions
* User is logged in
*At least 1 note exists
 
## Triggers
User selects “edit note” button
 
## Primary Sequence
User opens up the desired note
User selects “edit note” button

## Primary Postconditions
* Text editor in markdown format opens up
 



# Delete note
## Summary
User deletes a note.
 
## Actors
User
 
## Preconditions
* User is logged in
* At least 1 note exists
 
## Triggers
User selects “delete note” button
 
## Primary Sequence
User opens up the desired note
User selects “delete note” button

## Primary Postconditions
* Deleted file no longer appears in list

