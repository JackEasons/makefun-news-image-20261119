# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/JackEasons/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/JackEasons/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026.

Lead story: Trump, Xi and Putin meet in Shenzhen in the first three-way summit, issuing a joint "Declaration toward Peace" with no mention of Ukraine or Iran. Also: the top UN court rules Myanmar committed genocide against the Rohingya; Anthropic's IPO at $83 a share, valued at about $1.5 trillion; Israeli tanks push into central Gaza; Ukraine hits the Crimea bridge again and tanker attacks mount in the Strait of Hormuz.

## Run it

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` (1024x1024 PNG, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR/entry.png`, deterministically — both runs write the same bytes. No network is used at run time.

---

<sub>Entered on [make.fun](https://make.fun/?ref=gbg9q3ye&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
