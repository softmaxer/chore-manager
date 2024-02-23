# chore-manager
A small, simple (and extremely ugly coded) streamlit application to manage chores and turns for a few roommates living in an appartment.

currently the app is hosted with streamlit cloud, with a persistent json file.
Even though, this was a fun 30 minute project, here are some ways you can improve this app:
- Avoid reading/writing to the same file over and over again
(Maybe use an actual database with time log?)
- Don't use streamlit. Make an API (preferably in Go, cuz it's my favorite) and a separate frontend (I hate CSS), and deploy them with a CI/CD.
