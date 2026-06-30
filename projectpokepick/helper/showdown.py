from poke_env import ServerConfiguration


def config_server_connect(uri: str) -> ServerConfiguration:
    return ServerConfiguration(
        f"ws://{uri}/showdown/websocket",
        f"https://{uri}/action.php?",
    )
