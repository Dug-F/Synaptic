from channels.db import database_sync_to_async
from synaptic.models import User, UserExtension
from synaptic.constants import RoomMemberStatus as rms

class CUser():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Note: initialise needs to be called after instantiation as __init__ cannot be run async
        # The following instance variables are created by initialise
        # self.user         User model
        # self.nickname     str

    @database_sync_to_async
    def initialise(self, username):
        self.user = User.objects.get(username=username)

