import asyncio
import os

from poke_env.player import RandomPlayer

from projectpokepick.config import showdown


async def main():
    custom_config = showdown.config_showdown_server(env=os.environ["ENV"], uri=os.environ["SHOWDOWN_SERVER_URI"])
    player_1 = RandomPlayer(max_concurrent_battles=1, server_configuration=custom_config)
    player_2 = RandomPlayer(max_concurrent_battles=1, server_configuration=custom_config)

    await player_1.battle_against(player_2, n_battles=1)

    print(f"Finished battles: {player_1.n_finished_battles}")
    print(f"Player 1 wins: {player_1.n_won_battles}")

    print("###player1")
    for b in player_1.battles.values():
        for p in b.team.values():
            print(p.name)

    print("###player2")
    for b in player_2.battles.values():
        for p in b.team.values():
            print(p.name)


if __name__ == "__main__":
    asyncio.run(main())
