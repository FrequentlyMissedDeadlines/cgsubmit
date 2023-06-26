import requests


class Api:
    def __init__(self, test_session_handle):
        self.test_session_handle = test_session_handle

    def get_all_battles(self):
        r = requests.post(
            "https://www.codingame.com/services/gamesPlayersRanking/findLastBattlesByTestSessionHandle",
            data="[" + self.test_session_handle + ", null]",
            headers={"Content-type": "application/json"},
        )

        if r.status_code == 200:
            return r.json()
        else:
            raise Exception("Unable to retrieve last battles: " + str(r))

    def get_lost_games(self, losts):
        return [
            requests.post(
                "https://www.codingame.com/services/gameResultRemoteService/findByGameId",
                data="[" + str(id) + ", null]",
                headers={"Content-type": "application/json"},
            ).json()
            for id in losts
        ]
