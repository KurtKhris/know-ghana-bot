# Know Ghana Bot
A telegram bot to know the various regions and constituencies in Ghana.

[Demo](t.me/knowghanabot)

## Table of contents

- [Know Ghana Bot](#know-ghana-bot)
  - [Table of contents](#table-of-contents)
  - [General info](#general-info)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Setup](#setup)
        - [1. Requirements](#1-requirements)
        - [2. Setup:](#2-setup)
        - [3. Say hi to your bot:](#3-say-hi-to-your-bot)
  - [Status](#status)
  - [Inspiration](#inspiration)
  - [Contact](#contact)
  - [Contributing](#contributing)

## General info
A telegram bot with information on the number of regions, all regions, number of constituencies and all constituencies.

## Features
* Number of Regions
* All Regions
* Number of Constituencies
* All Constuencies

## Technologies 
* Python

## Setup
To run this app, you will need to follow these 3 steps:

##### 1. Requirements 
  - a Laptop

  - Text Editor [VS code]
  
  - Python 3^

  - Git installed on your Laptop. 
  
  - Telegram application [Desktop, Moblie]
  
  - A sound mind

##### 2. Setup:
Clone the repo and install the dependencies.

```bash
git clone https://github.com/barbara99/know-ghana-bot.git
cd know-ghana-bot
```

```bash
python -m pip install virtualenv
python -m venv env
source env/bin/activate
```

```bash
python -m pip install -r requirements.txt
```
##### 3. Say hi to your bot:
 - Create a new bot with [BotFather](t.me/BotFather) with _/newbot_ command
  
 - Add the telegram token to config vars when hosting on telegram or create a .env file and add the token in the file to run locally.
  
  To run the bot locally, run the following

```bash
python api.py
```

Open your bot and play around.

## Status
Project is: _in progress_

## Inspiration
This project was to improve my use and familiarity with APIs.

## Contact
Created by [Barbara Asiamah](https://www.linkedin.com/in/barbara-asiamah123/) - feel free to contact me!

## Contributing

1. Fork it (<https://github.com/barbara99/know-ghana-bot>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request