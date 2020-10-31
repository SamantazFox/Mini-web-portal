Apps portal generator
=====================

Generates a very simple website with icons that redirects to any url you want.

No javasript, no PHP, only static HTML.

The generator requires python, though.


How to use
----------

When using this tool for the first time, you'll have to:

1. rename (or copy) `config_example.json` to `config.json`
2. Get normalize.css from here: https://necolas.github.io/normalize.css

Then, whenever you want to change the site's contents:

1. Edit `config.json` to meet your needs
2. Place your icons (svg, png, ...) in icons/
3. run `python3 generator.py` (or `./generator.py` directly on linux)


Licensing
---------

This repo's content is released under the public domain.

Feel free to copy, modify and redistribute the code.

Read the UNLICENSE file for more infos.
