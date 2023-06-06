import unittest

class TestGames(unittest.TestCase):
    mocked_games = [
        {
            "players": [
                {
                    "position": 0,
                    "nickname": "Player 1"
                },
                {
                    "position": 1,
                    "nickname": "Player 2"
                }
            ],
            "gameId": 100
        },
        {
            "players": [
                {
                    "position": 0,
                    "nickname": "Player 3"
                },
                {
                    "position": 1,
                    "nickname": "Player 1",
                }
            ],
            "gameId": 200
        }
    ]
    
    def test_games(self):
        from cgsubmit.games import Games
        games = Games(self.mocked_games)

        self.assertEqual(games.pseudo, 'Player 1')
        self.assertEqual(games.number_by_id[100], 2)
        self.assertEqual(games.number_by_id[200], 1)
        self.assertEqual(len(games.win), 1)
        self.assertEqual(games.win[0]['gameId'], 100)
        self.assertEqual(len(games.lost), 1)
        self.assertEqual(games.lost[0], 200)

        games = Games(self.mocked_games[::-1])
        self.assertEqual(games.pseudo, 'Player 1')

    def test_games_raise_exception(self):
        from cgsubmit.games import Games
        try:
            Games([])
        except Exception as exception:
            self.assertEqual(str(exception), 'Not enough games played to guess who is the right player. You must play against at least 2 different opponents.')
            pass
        else:
            self.fail('Exception not raised')
        
        try:
            Games([
                {
                    "players": [
                        {
                            "position": 0,
                            "nickname": "Player 1"
                        },
                        {
                            "position": 1,
                            "nickname": "Player 2"
                        }
                    ],
                    "gameId": 100
                }
            ])
        except Exception as exception:
            self.assertEqual(str(exception), 'Not enough games played to guess who is the right player. You must play against at least 2 different opponents.')
            pass
        else:
            self.fail('Exception not raised')

    def test_games_timeouts(self):
        from cgsubmit.games import Games
        games = Games(self.mocked_games)
        timeouts = games.get_timeouts([
            {
                "scores": [90, 86]
            },
            {
                "scores": [-1, 0]
            }
        ])
        self.assertEqual(len(timeouts), 1)

        games = Games(self.mocked_games)
        timeouts = games.get_timeouts([
            {
                "scores": [90, 86]
            },
            {
                "scores": [1, 0]
            }
        ])
        self.assertEqual(len(timeouts), 0)

