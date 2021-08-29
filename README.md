**Telegram to Twitter tool**

Simple tool that fetch messages from specified Telegram channel and push them to the Twitter

Uses Telethon and Tweepy libraries
_Need to have Telegram API and and twitter developer account._
_Don't forget to change permissions on the Twitter app_

Ready for deploy on Heroku:
(can use free dyno hours without sleeping)

Steps:
1 - $heroku login
2 - $heroku create
3 - $cd <my-project>
4 - $git init
5 - $heroku git:remote -a <your-heroku-app-name>
6 - $git add .
7 - $git commit -am "first commit"
8 - $git push heroku master
9 - $heroku ps:scale worker=1     
  
**Done!**
Now this app fetches every telegram post and immediately push it to your Twitter 

