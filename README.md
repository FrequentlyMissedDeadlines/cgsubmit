[![Build](https://github.com/FrequentlyMissedDeadlines/cgsubmit/actions/workflows/python-package.yml/badge.svg)](https://github.com/FrequentlyMissedDeadlines/cgsubmit/actions/workflows/python-package.yml)
[![Publish](https://github.com/FrequentlyMissedDeadlines/cgsubmit/actions/workflows/python-publish.yml/badge.svg)](https://github.com/FrequentlyMissedDeadlines/cgsubmit/actions/workflows/python-publish.yml)
[![Version](https://img.shields.io/pypi/v/cgsubmit)](https://pypi.org/project/cgsubmit)
[![Version](https://img.shields.io/pypi/pyversions/cgsubmit)](https://pypi.org/project/cgsubmit)
[![codecov](https://codecov.io/gh/FrequentlyMissedDeadlines/cgsubmit/branch/main/graph/badge.svg)](https://codecov.io/github/FrequentlyMissedDeadlines/cgsubmit?branch=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cgsubmit)
# codingame-submit
A tool to analyze the results of your submits in codingame competitions and save a lot of time.

## Installation
```
pip install cgsubmit
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
python -m cgsubmit your-test-session-handle
```