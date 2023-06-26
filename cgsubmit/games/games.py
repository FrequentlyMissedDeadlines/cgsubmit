class Games:
    def __init__(self, games):
        self.games = games
        self.pseudo = self.find_pseudo(games)
        self.number_by_id = self.find_game_by_id(games)
        self.win, self.lost = self.get_win_and_lost(games, self.pseudo)

    def find_pseudo(self, games) -> str:
        player1 = ""
        player2 = ""

        i = 0
        while i < len(games):
            if len(games[i]["players"]) <= 1:
                i = i + 1
                continue
            if player1 == "":
                player1 = games[i]["players"][0]["nickname"]
                player2 = games[i]["players"][1]["nickname"]
            else:
                if (
                    player1 == games[i]["players"][0]["nickname"]
                    and player2 != games[i]["players"][1]["nickname"]
                    or player1 == games[i]["players"][1]["nickname"]
                    and player2 != games[i]["players"][0]["nickname"]
                ):
                    return player1
                if (
                    player1 != games[i]["players"][0]["nickname"]
                    and player2 == games[i]["players"][1]["nickname"]
                    or player1 != games[i]["players"][1]["nickname"]
                    and player2 == games[i]["players"][0]["nickname"]
                ):
                    return player2
            i = i + 1

        raise Exception(
            "Not enough games played to guess who is the right player. You must play against at least 2 different opponents."
        )

    def find_game_by_id(self, games) -> dict:
        number_by_id = {}

        for i in range(len(games)):
            number_by_id[games[i]["gameId"]] = len(games) - i

        return number_by_id

    def get_win_and_lost(self, games, pseudo):
        wins = [
            a
            for a in games
            if (
                "nickname" in a["players"][0]
                and a["players"][0]["nickname"] == pseudo
                and a["players"][0]["position"] == 0
            )
            or (
                len(a["players"]) > 1
                and "nickname" in a["players"][1]
                and a["players"][1]["nickname"] == pseudo
                and a["players"][1]["position"] == 0
            )
        ]
        losts = [a["gameId"] for a in games if a not in wins]
        return (wins, losts)

    def get_timeouts(self, lost_games):
        self.timeouts = [
            a for a in lost_games if a["scores"][0] == -1 or a["scores"][1] == -1
        ]
        return self.timeouts
