"""bot.guilds RPC schema"""

# 3rd party
from pydantic import BaseModel


class BotGuildsResponse(BaseModel):
    """bot.guilds request"""

    guild_ids: set[str]
