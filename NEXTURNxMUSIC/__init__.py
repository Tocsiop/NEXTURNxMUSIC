from NEXTURNxMUSIC.core.bot import Anony
from NEXTURNxMUSIC.core.dir import dirr
from NEXTURNxMUSIC.core.git import git
from NEXTURNxMUSIC.core.userbot import Userbot
from NEXTURNxMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
