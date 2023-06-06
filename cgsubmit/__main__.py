#!/usr/bin/env python

import argparse
from cgsubmit.api import *
from cgsubmit.games import *

def main():
    parser = argparse.ArgumentParser(description='Analyse your submit in codingame competitions.')
    parser.add_argument('-t', '--testsessionhandle', required=True, help='The test session handle. If you don\'t know how to get it, look at the doc: https://github.com/FrequentlyMissedDeadlines/cgsubmit')
   
    args = parser.parse_args()

    try:
        api = Api(args.testsessionhandle)
        battles = api.get_all_battles()
        games = Games(battles)
        lost_games = api.get_lost_games(games.lost)
        timeouts = games.get_timeouts(lost_games)
        print('{0} games retrieved'.format(len(battles)))
        print('Pseudo: {0}'.format(games.pseudo))
        print('Total win and draw: {0}'.format(len(games.win)))
        print('Total lose: {0}'.format(len(games.lost)))
        print()

        if len(timeouts) > 0:
            print('❌Total timeouts {0}'.format(len(timeouts)))
            for timeout in timeouts:
                print('⌛Timeout in game #{1} https://www.codingame.com/replay/{0}'.format(timeout['gameId'], games.number_by_id[timeout['gameId']]))
        else:
            print('✅ No timeouts detected')

        lost_games.sort(key=lambda a: abs(a['scores'][0] - a['scores'][1]), reverse=True)

        print()
        for game in lost_games:
            print('➤ Lost game #{2} https://www.codingame.com/replay/{0} by {1} points'.format(game['gameId'], abs(game['scores'][0] - game['scores'][1]), games.number_by_id[game['gameId']]))

        
    except Exception as exception:
        print(exception)

if __name__ == '__main__':
	main()