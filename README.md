[![Build](https://github.com/FrequentlyMissedDeadlines/cgsubmit/actions/workflows/python-package.yml/badge.svg)](https://github.com/FrequentlyMissedDeadlines/cgsubmit/actions/workflows/python-package.yml)
[![Publish](https://github.com/FrequentlyMissedDeadlines/cgsubmit/actions/workflows/python-publish.yml/badge.svg)](https://github.com/FrequentlyMissedDeadlines/cgsubmit/actions/workflows/python-publish.yml)
[![Version](https://img.shields.io/pypi/v/cgsubmit)](https://pypi.org/project/cgsubmit)
[![Version](https://img.shields.io/pypi/pyversions/cgsubmit)](https://pypi.org/project/cgsubmit)
[![codecov](https://codecov.io/gh/FrequentlyMissedDeadlines/cgsubmit/branch/main/graph/badge.svg)](https://codecov.io/github/FrequentlyMissedDeadlines/cgsubmit?branch=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cgsubmit)
# codingame-submit
A tool to analyze the results of your submits in codingame competitions and save a lot of time.

It will automatically:
- retrieve all the games you lost by timeout (code too slow, or runtime error). Fixing these issues should always be your number 1 priority.
- sort the game you lost by biggest score difference. This way you can easily focus on the games you totally lost as there might be some cases you don't handle properly or you have bugs.

![](https://raw.githubusercontent.com/FrequentlyMissedDeadlines/cgsubmit/main/Doc/output.png)
![](https://raw.githubusercontent.com/FrequentlyMissedDeadlines/cgsubmit/main/Doc/Codingame.PNG)

## Installation
```
pip install cgsubmit
```
or to update to the latest version:
```
pip install cgsubmit -U
```

## Usage
### Getting your test session handle
This token is linked to your session and game you are playing.
To retrieve it:

1. open the IDE of the game you are playing in your browser (for example [https://www.codingame.com/ide/puzzle/spring-challenge-2023-ants](https://www.codingame.com/ide/puzzle/spring-challenge-2023-ants))
2. open the Developer Tools (F12)
3. look for this query and get the `handle` value: ![](https://raw.githubusercontent.com/FrequentlyMissedDeadlines/cgsubmit/main/Doc/handle.png)

### Run

```
python -m cgsubmit -t your-test-session-handle
```

or for a most advanced usage use `-h` option to get the description of all parameters:

```
python -m cgsubmit -h
usage: cgsubmit [-h] -t TOKEN [--noreplay] [--noelo]

Analyse your submit in codingame competitions.

options:
  -h, --help            show this help message and exit
  -t TOKEN, --testsessionhandle TOKEN
                        The test session handle. If you don't know how to get it, look at the doc: https://github.com/FrequentlyMissedDeadlines/cgsubmit
  --noreplay            Remove replay URLs.
  --noelo               Remove opponent rank.
```

### Known issues

If you are using git bash to run the command you might see this kind of error: ```'charmap' codec can't encode character '\u274c' in position 0: character maps to <undefined>```

You must go to the settings and set the encoding to UTF-8:

![](https://raw.githubusercontent.com/FrequentlyMissedDeadlines/cgsubmit/main/Doc/utf8.PNG)
