Bruno2
======

Bruno2 is a minimalist modular IRC bot written for Python 2. It is based on the `FrozenIdea <https://github.com/Bystroushaak/FrozenIdea>`_ module for IRC bots.

Usage
-----

You need to install FrozenIdea with

``pip install git+https://github.com/Bystroushaak/FrozenIdea.git``

Then you can clone this repo and run the bot like

``$ python2 bruno2.py [NICK] [SERVER] [PORT]``

Bot will connect to the given server and join channel ``#testbruno`` (see ``modules/test.py``). You can add and change modules on run.
