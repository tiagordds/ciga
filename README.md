# CIGA Edital Tracker

A simple script to help me keep track of the updates to a civil service exam i'm part of. 

The database has the text of the first post on the website, the crawler checks the current first post on the website and compares it to the one saved in the DB:

- If it's the same, nothing happens
- If it's different, it updates the DB and sends me an email with the new text.

The script runs twice a day using GitHub Actions.
