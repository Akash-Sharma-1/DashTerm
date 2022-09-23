## Da⚡hTerm
>A terminal based application (TUI) for enhancing your productive workstation 👨‍💻...

![DashTerm Icon](images/Dashterm.png)

---
- [Da⚡hTerm](#da-hterm)
    + [What's the app actually doing ? 🤔](#what-s-the-app-actually-doing-----)
    + [Why use a TUI for this? 🤔](#why-use-a-tui-for-this----)
    + [Want to contribute ?](#want-to-contribute--)
- [Features 📑](#features---)
- [How to use this ⚙?](#how-to-use-this---)
    + [Requirements](#requirements)
    + [Setting up Google Cloud Client](#setting-up-google-cloud-client)
      - [Login Information](#login-information)
      - [You currently have to use your own Google API token.](#you-currently-have-to-use-your-own-google-api-token)
      - [HTTP Proxy Support](#http-proxy-support)
    + [Cloning the repo](#cloning-the-repo)
    + [Installing Dependencies](#installing-dependencies)
    + [Firing up the terminal](#firing-up-the-terminal)
- [This is a **work-in-progress** project 😊](#this-is-a---work-in-progress---project---)
- [Contributing ♥](#contributing--)
- [License](#license)
---

DashTerm is an easy to use , open-source TUI dashboard which enables you to view all the essential data you need at your workplace in a single glance.

#### What's the app actually doing ? 🤔
This app helps you in marking your events throughout the day, jotting down tasks, tracking down habits, logging journals and time-boxing work with pomo sessions - all enhancing your overall productivity with lightning speed ⚡
And all this information is constantly synced with your cloud services ! 

#### Why use a TUI for this? 🤔
TUI is one of the most frictionless ways to interact with data without getting involved in UI/UX traps.
Over time, it becomes more efficient for inputting or viewing high frequency datapoints.


#### Want to contribute ?
Please refer to the [Contributing Section](#contributing-) 
Thanks in advance <3


## Features 📑

Not an exaustive list - many more dashboard views are yet to come !
Some of the currently planned **dashboard views** are : 
- 📆 Google calendar
  - View , edit and modify your daily events
- ✅ Google tasks
  - View, edit and modify your tasks from any task lists
- 🎯 Habitica - Habit Tracking
  - Manage and track your dailies and habits synced with [Habitica](https://habitica.com/)
- 📒 Google Keep
  - View and add your journalling notes to Google keep 
- ⏲ Pomodoro
  - View and start-pause-stop pomodoro sessions 

![Demo1](/images/Demo1.jpg)
![Demo2](/images/Demo2.jpg)


## How to use this ⚙?
#### Requirements
- python3
- pip or pip3

#### Setting up Google Cloud Client
- ##### Login Information
  OAuth2 is used for authenticating with your Google account. The resulting token
  is placed in the `root directory`. When you first start any google API command inside TUI dashboard, the
  authentication process will proceed. Simply follow the instructions.


- ##### You currently have to use your own Google API token.
  In order to facilitate the token process : 
    1. [Create a New Project](https://console.developers.google.com/projectcreate) within the Google developer console
      1. Activate the "Create" button.
    2. [Enable the Google Calendar API](https://console.developers.google.com/apis/api/calendar-json.googleapis.com/)
      1. Activate the "Enable" button.
    3. [Create OAuth2 consent screen](https://console.developers.google.com/apis/credentials/consent/edit;newAppInternalUser=false) for an "UI /Desktop Application".
      1. Fill out required App information section
          1. Specify App name. Example: "gcalcli"
          2. Specify User support email. Example: your@gmail.com
      2. Fill out required Developer contact information
          1. Specify Email addresses. Example: your@gmail.com
      3. Activate the "Save and continue" button.
      4. Scopes: activate the "Save and continue" button.
      5. Test users
          1. Add your@gmail.com
          2. Activate the "Save and continue" button.
    4. [Create OAuth Client ID](https://console.developers.google.com/apis/credentials/oauthclient)
      1. Specify Application type: Desktop app.
      2. Activate the "Create" button.
    5. Grab your newly created Client ID (in the form "xxxxxxxxxxxxxxx.apps.googleusercontent.com") and Client Secret from the Credentials page.
    6. Download the Credential Json file and name it is as `credentials.json` - it should look like [credentials-sample.json](credentials-sample.json)


- ##### HTTP Proxy Support
  DashTerm will automatically work with an HTTP Proxy simply by setting up some
  environment variables used by the gdata Python module:

  ```
  http_proxy
  https_proxy
  proxy-username or proxy_username
  proxy-password or proxy_password
  ```

  Note that these environment variables must be lowercase.

#### Cloning the repo
```
>> git clone https://github.com/Akash-Sharma-1/DashTerm.git
```
#### Installing Dependencies
```
>> cd DashTerm
>> pip install -r requirements.txt
```
#### Firing up the terminal
```
>> python tui.py
```
- Use Windows Terminal for the best experience


## This is a **work-in-progress** project 😊

The project currently is divided in 2 milestones : **Phase 1** and **Phase 2**
- *Phase 1* is the milestone where the plan is construct robust implementations for the currently planned basic features.
- *Phase 2* is the milestone where the plan is extend the tool to integrate more plugins and make it more user friendly

There are a few todo items left for the Phase 1 - you can view it in the [Projects](https://github.com/users/Akash-Sharma-1/projects/1/views/1) section.
All the issues are tagged with Phase 1 and Phase 2 depending upon the severity and nature.

## Contributing ♥

Currently, there are very few limited applications in the market, that could provide a single glance view of all the essential components of a work management system for a developer. 

The definition of a work management system itself varies quite differently across devs, orgs and groups.
>*DashTerm could become a personalised plug-play TUI tool for everyone to manage their work effectively and enhance their productivity with plugins they feel empowered with .* 

Achieving this humoungous task, is only a possiblity with your contributions to this project through bug reporting, proposing enhacements, documenting, code contributing and much more.

## License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details