"""bot.guilds RPC schema"""

# 3rd party
from pydantic import BaseModel


class BotGuildsResponse(BaseModel):
    """bot.guilds response"""

    guild_ids: set[str]
