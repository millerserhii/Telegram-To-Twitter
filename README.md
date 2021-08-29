**Telegram to Twitter tool**


Simple tool that fetch messages from specified Telegram channel and push them to the Twitter


Uses Telethon and Tweepy libraries

_Need to have Telegram API and and twitter developer account._

_Don't forget to change permissions on the Twitter app_

**Ready for deploy on Heroku:**
_(can use free dyno hours without sleeping)_

**Steps:**

_1 - $heroku login_

_2 - $heroku create_

_3 - $cd <my-project>_
  
_4 - $git init_
  
_5 - $heroku git:remote -a <your-heroku-app-name>_
  
_6 - $git add ._
  
_7 - $git commit -am "first commit"_
  
_8 - $git push heroku master_
  
_9 - $heroku ps:scale worker=1_
  
  
**Done!**
  
Now this app fetches every telegram post and immediately push it to your Twitter 

