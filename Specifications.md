**Github:** https://github.com/artak10t/Examo

**Team Members**

* Spartak Gevorgyan: https://github.com/artak10t
* Matthew Chan: https://github.com/blankss
* Janelle Marcos: https://github.com/janellemarcos
* Dat Tri Tat: https://github.com/DatTriTat

**Date:** 9/16/2021

**Product Name:** Examo

**Problem Statement:** App that provides learning tools for students to study.

**Non-functional Requirements:** The website has to be in the English language.





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