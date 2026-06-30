from poke_env import LocalhostServerConfiguration, ServerConfiguration, ShowdownServerConfiguration

from projectpokepick.common import consts
from projectpokepick.helper import showdown


def config_showdown_server(env: str, uri: str = "") -> ServerConfiguration:
    if env == consts.Env.DEV:
        if not uri:
            raise Exception("Please specify the URI for Pokemon Showdown.")

        return showdown.config_server_connect(uri)

    if env == consts.Env.LOCAL:
        return LocalhostServerConfiguration

    if env == consts.Env.PRD:
        return ShowdownServerConfiguration

    raise Exception("Please specify the correct environment.")
