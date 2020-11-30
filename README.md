# Inventory-Bot
Used to automatically scrape sites to check inventory on specific items and send updates via XMPP or email

Forked an updated to deal with the primer/powder/ammo shortage of 2020, this script was tested against a few firearm ammunition reloading component suppliers. It should work with any site that has some sort of "out of stock" message that appears on a product page when scraped.

## Features
- Send messages via email, XMPP, both, and/or with libnotify (Ubuntu) when desired items are in stock

## Requirements
- python3
- xmpppy

## Use
- install xmpppy via pip
- fill in config.py
- set a cron job to trigger the script, or maybe a keybpard shortcut
- pass the option `-d` to the script to enable desktop notifications using libnotify (Ubuntu)
- Have fun

To add or use a website that is not in the list below, check the "out of stock" message on the product page and make sure that it is in the `cfg.keywords` list found on line 12 of `main_script.py`, being mindful that the script is case sensative. If it is not found in the list, add it to the `keywords` list in `config.py` for local use. If this should be added to the script, open a pull request adding in the new keyword to `main_script.py` and adding the site to the list below.

## Sites known to be working:
- [Mid South Shooters](https://www.midsouthshooterssupply.com/)
- [Midway USA](https://www.midwayusa.com)
- [Natchcz](https://www.natchezss.com/)
- [Poweder Valley Inc](https://www.powdervalleyinc.com)
- [Reloading Unlimited](https://reloadingunlimited.com)

## Sties known to be not working:
