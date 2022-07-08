# folio-client 

This library helps to communicate with the FOLIO API and automate some manual tasks:
- creating users
- creating instances, holdings records, items
- creating loans (check out)
- etc.

# env.py

env.py file with your env details and user credentials needs to be created in the root dir:

<pre>
okapi_url = 'https://okapi-url'
origin = 'https://folio-ui-url'
tenant = 'tenant'
username = 'username'
password = 'password'
</pre>

This file is added to .gitignore, DO NOT push you credentials to GitHub