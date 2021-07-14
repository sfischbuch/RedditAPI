rmbti - An AI application that determines your Myers-Briggs Type Indicator.
========================

Setup
========================

1. Go to `Reddit <reddit.com/prefs/apps>`_ and create an app and obtain your own ``client_id`` and ``client_secret``. Use ``http://localhost:8080`` as 
your redirect uri or your user context such as a web site.

2. To protect your credentials create a ``praw.ini`` file to place them in. Place this in the working directory. This is not the best 
way to authenticate but it will do for now. The password and username are the ones you use to sign into your reddit account. It should look like this:

[YourBot]

client_id=...

client_secret=...

password=...

username=...

3. Configure and create a Reddit intances with ``praw.Reddit('YourBot')``.

Resources 
========================

`PRAW Docs <https://praw.readthedocs.io/en/v7.3.0/>`_
