# folio-client 

This library helps to communicate with the FOLIO API and automate some manual tasks:
- creating users
- creating instances, holdings records, items
- creating loans (check out)
- etc.

Python 3 is required. `requests` module needs to be installed too: `pip3 install requests`

# env.py

env.py file with your env details and user credentials needs to be created in the root dir:

<pre>
okapi_url = 'https://okapi-url'
origin = 'https://folio-ui-url'
tenant = 'tenant'
username = 'username'
password = 'password'
consortia_enabled = False
</pre>

This file is added to .gitignore, DO NOT push you credentials to GitHub

# FOLIO API integration

API integration is implemented in module-specific files:

- inventory.py
- circulation
- users
- etc.

You can add such files or extend the existing ones if you want to improve folio-client's integration with FOLIO API. There shouldn't be anything specific to you immediate tasks/scenarios in these files because they will be used by other devs for other scenarios.

# scenarios.py

Specific scenarios should be implemented in scenarios.py as functions. This is you "sandbox". 

# main.py

main.py should only call scenarios from scenarios.py.