# telegramBot
A couple of months ago, I had to write a telegram bot for a small business which was running in the Telegram application. By a simple search in the net, you can find many source about how to write a bot in telegram, but I could not find any that can be a template and can be customized for a simple interaction with the user.  Then, I have decided to write a simple code to include the general template and important commands to do so. Here, is a simple version of it that can be customized for your goal very easily.  I assume that the reader does not know anything about writing a bot but know basic python scripts!
To be able to use this template, please follow these steps:

    - Create your channel or groups in the Telegram app that you want to run the bot in it\\
    - Create your desired bot interface in the telegram app with "bot father". To do that, type and click on “@BotFather” in the telegram app and create newbot with the command /newbot and follow the instruction (Fig. 1). Here, I create a sample bot with this name “testBotLearning” and this username “testLearnCreateBot” and received this HTTP API token from the botFather: “1694120992:AAG4EpESMdNBihBAP0oUWUWe42gsaoMP1Nw”. DO NOT SHARE YOUR TOKEN WITH ANYBODY!!!
    - Give administrative access to the bot in the group/channel by adding the bot to them and giving enough access.
    - Now it is time to construct your bot programming engine by the written python script. Copy the written template script from here to your python interface, save it, and act according to the helps in front of each line. In the same folder create a virtual environment in command window (assuming that you are using windows!) and activate this environment
    
>python -m venv venv

>venv\Scripts\activate

And install the following libraries

pip install flask

pip install python-telegram-bot

pip install requests

Then run this command to create the requirements file:

>pip freeze > requirements.txt

In the next step, we need to tell the server, where the application starts. Just create a “Procfile” in the directory of your saved file (at your desktop and where the cmd is running) and type the following: 
web: python botScript.py
Keep in mind that the name of the Procfile must be exactly as “Procfile” without any extension. Also create a .gitignore file and write “*.md” in it and save it in the same directory as above. 


    Figure 1. How to create a bot with botFather in Telegram


To run the bot, you need a server. Either you have to upload it on your current space on some servers (the server that you have enough spaces for running this type of code continuously) or you have to buy some spaces from one of the servers. Totally, you do not need to even pay most of the time and you can use the free options is some servers, like Heroku. To sign up for an account in Heroku, go to https://signup.heroku.com/. 
Go to the dashboard in Heroku and create a new application. Here, I call the new app as “telegrambot4learning”. Go to the deploy page of the app and click setting and copy the given “Heroku git URL” and paste it in the botScript.py for the variable URL.
Now come back to your cmd terminal in windows (or shell in Mac or so on) and run the following commands consecutively;
>heroku login
>git init
>heroku git:remote -a telegrambot4learning  “here you have to use your project name instead!”
>git add .
>git commit -m "first run"
>git push heroku master


Now, it is done! Just come back to your channel or group in Telegram, and run your bot and enjoy.

