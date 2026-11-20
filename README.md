# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/JackEasons/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/JackEasons/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026.

Lead story: Trump, Xi and Putin hold the first three-way summit in Shenzhen, issuing a joint "Declaration toward Peace" with no mention of Ukraine or Iran. Also: Cyclone Akvan forces 100,000+ evacuations in Odisha ahead of Friday landfall; the World Court rules 9-6 that Myanmar committed genocide against the Rohingya; Anthropic's $83 IPO opens at $111.50 and closes $97.17, up 17%, while US markets slide for a sixth straight session; Israeli tanks push into central Gaza; Ukraine hits the Crimea bridge a third time this week; three tankers catch fire on mines east of Hormuz; the UK pledges 1,000+ long-range drones for Ukraine; GTA VI launches worldwide; NASA confirms Voyager 1 is one light-day from Earth; and the US Senate rejects the Iran war-powers resolution 51-48. 33 stories in all, each verified against reporting of the day — see STORIES.md for every item and its source.

## Run it

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` (1024x1024 PNG, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR/entry.png`, deterministically — both runs write the same bytes. No network is used at run time.

---

<sub>Entered on [make.fun](https://make.fun/?ref=gbg9q3ye&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
