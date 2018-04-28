# ScannyMcScanFace-Python3
A simple bot that gathers sales/deals from buildapcsales subreddit.

[![GitHub release](https://img.shields.io/badge/Build-1.1-brightgreen.svg)](https://github.com/DuckBoss/RedditBAPCS/releases/latest)
[![Packagist](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/DuckBoss/RedditBAPCS/blob/master/LICENSE)


## Dependencies
- praw (can be installed with pip)

## Usage
1) Setup a praw.ini file with your reddit username, password, user_agent, client_id, and client_secret.
> You can register the app with your account for authentication here: https://www.reddit.com/prefs/apps/
2) Keep the praw.ini file in the same directory as the python script.
3) Edit the script with chosen categories/keywords in the variables provided.


## praw.ini file
You can use the template provided in this repository and fill in the required information as detailed in the usage section of the readme.

## All Optional Parameters
- allow_stream (enables real time capturing)
- search_limit (limits the number of submissions that are scanned)
