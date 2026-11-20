#!/usr/bin/env python3
"""THE WORLD TODAY - Thursday 19 November 2026. One 1024x1024 front page,
33 verified stories, drawn from scratch with PIL. No network at run time."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
INK = (24, 24, 28)
PAPER = (250, 247, 238)
RED = (178, 34, 34)
BLUE = (30, 70, 140)
TEAL = (14, 110, 110)
GOLD = (176, 128, 28)
GREY = (105, 105, 105)
LIGHT = (232, 228, 218)
RULE = (180, 172, 158)

FD = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FD + name, size)

f_title = F("DejaVuSerif-Bold.ttf", 56)
f_date = F("DejaVuSans-Bold.ttf", 17)
f_big = F("DejaVuSans-Bold.ttf", 19)
f_big2 = F("DejaVuSans-Bold.ttf", 16)
f_body = F("DejaVuSans.ttf", 13)
f_bodyb = F("DejaVuSans-Bold.ttf", 13)
f_small = F("DejaVuSans-Bold.ttf", 14)
f_smbody = F("DejaVuSans.ttf", 12)
f_brief = F("DejaVuSans.ttf", 12)
f_briefb = F("DejaVuSans-Bold.ttf", 12)
f_num = F("DejaVuSans-Bold.ttf", 21)
f_numlab = F("DejaVuSans-Bold.ttf", 9)
f_src = F("DejaVuSans.ttf", 10)
f_check = F("DejaVuSans.ttf", 11)
f_checkb = F("DejaVuSans-Bold.ttf", 11)
f_map = F("DejaVuSans-Bold.ttf", 10)
f_foot = F("DejaVuSans.ttf", 10)


def wrap(text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if font.getlength(trial) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, lines, font, fill=INK, leading=17):
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += leading
    return y


def hline(d, x0, x1, y, fill=RULE, w=2):
    d.line([(x0, y), (x1, y)], fill=fill, width=w)


# ------------------------- small drawn emblems -------------------------

def icon_summit(d, x, y, s):
    # three leaders at a table: three heads, three flags
    d.rectangle([x, y + s * 0.62, x + s, y + s * 0.72], fill=(120, 84, 52))
    for i, col in enumerate([(178, 34, 34), (30, 70, 140), (24, 24, 28)]):
        cx = x + s * (0.2 + 0.3 * i)
        d.ellipse([cx - s * 0.11, y + s * 0.28, cx + s * 0.11, y + s * 0.5], fill=(232, 190, 150))
        d.arc([cx - s * 0.11, y + s * 0.28, cx + s * 0.11, y + s * 0.42], 180, 360, fill=(90, 60, 40), width=2)
        d.rectangle([cx - s * 0.13, y + s * 0.52, cx + s * 0.13, y + s * 0.62], fill=col)
    # three small flags above
    for i, col in enumerate([(178, 34, 34), (200, 200, 200), (30, 70, 140)]):
        fx = x + s * (0.12 + 0.36 * i)
        d.line([(fx, y + s * 0.05), (fx, y + s * 0.28)], fill=INK, width=2)
        d.polygon([(fx, y + s * 0.05), (fx + s * 0.22, y + s * 0.10), (fx, y + s * 0.15)], fill=col)


def icon_cyclone(d, x, y, s):
    cx, cy = x + s / 2, y + s * 0.45
    for r, w in [(s * 0.42, 4), (s * 0.30, 4), (s * 0.18, 4)]:
        d.arc([cx - r, cy - r, cx + r, cy + r], 20, 300, fill=TEAL, width=w)
    d.ellipse([cx - s * 0.07, cy - s * 0.07, cx + s * 0.07, cy + s * 0.07], fill=TEAL)
    for i in range(5):
        rx = x + s * (0.08 + 0.2 * i)
        d.line([(rx, y + s * 0.78), (rx - s * 0.05, y + s * 0.95)], fill=BLUE, width=3)


def icon_scales(d, x, y, s):
    d.line([(x + s / 2, y + s * 0.12), (x + s / 2, y + s * 0.85)], fill=INK, width=4)
    d.line([(x + s * 0.12, y + s * 0.22), (x + s * 0.88, y + s * 0.22)], fill=INK, width=4)
    for cx in (x + s * 0.16, x + s * 0.84):
        d.line([(cx, y + s * 0.22), (cx, y + s * 0.45)], fill=INK, width=2)
        d.polygon([(cx - s * 0.14, y + s * 0.45), (cx + s * 0.14, y + s * 0.45),
                   (cx, y + s * 0.62)], fill=GOLD)
    d.rectangle([x + s * 0.32, y + s * 0.85, x + s * 0.68, y + s * 0.92], fill=INK)


def icon_rocket(d, x, y, s):
    d.polygon([(x + s * 0.5, y + s * 0.05), (x + s * 0.68, y + s * 0.45),
               (x + s * 0.5, y + s * 0.38), (x + s * 0.32, y + s * 0.45)], fill=RED)
    d.polygon([(x + s * 0.32, y + s * 0.45), (x + s * 0.2, y + s * 0.62),
               (x + s * 0.38, y + s * 0.52)], fill=RED)
    d.polygon([(x + s * 0.68, y + s * 0.45), (x + s * 0.8, y + s * 0.62),
               (x + s * 0.62, y + s * 0.52)], fill=RED)
    d.polygon([(x + s * 0.44, y + s * 0.55), (x + s * 0.56, y + s * 0.55),
               (x + s * 0.5, y + s * 0.78)], fill=GOLD)
    d.line([(x + s * 0.08, y + s * 0.88), (x + s * 0.92, y + s * 0.88)], fill=INK, width=3)


def icon_chart_down(d, x, y, s):
    pts = [(x + s * 0.08, y + s * 0.25), (x + s * 0.3, y + s * 0.4),
           (x + s * 0.5, y + s * 0.32), (x + s * 0.7, y + s * 0.62),
           (x + s * 0.92, y + s * 0.8)]
    d.line(pts, fill=RED, width=4, joint="curve")
    d.polygon([(x + s * 0.92, y + s * 0.8), (x + s * 0.78, y + s * 0.78),
               (x + s * 0.9, y + s * 0.64)], fill=RED)
    for i, h in enumerate((0.5, 0.35, 0.55, 0.3)):
        bx = x + s * (0.1 + 0.22 * i)
        d.rectangle([bx, y + s * (0.9 - h), bx + s * 0.12, y + s * 0.9], fill=LIGHT, outline=GREY)


def icon_tank(d, x, y, s):
    d.rectangle([x + s * 0.1, y + s * 0.55, x + s * 0.9, y + s * 0.78], fill=(90, 90, 80))
    d.rectangle([x + s * 0.3, y + s * 0.38, x + s * 0.62, y + s * 0.58], fill=(70, 70, 60))
    d.line([(x + s * 0.6, y + s * 0.45), (x + s * 0.95, y + s * 0.4)], fill=(70, 70, 60), width=5)
    for i in range(4):
        cx = x + s * (0.2 + 0.2 * i)
        d.ellipse([cx - s * 0.06, y + s * 0.78, cx + s * 0.06, y + s * 0.9], fill=INK)


def icon_bridge(d, x, y, s):
    d.line([(x + s * 0.05, y + s * 0.75), (x + s * 0.95, y + s * 0.75)], fill=INK, width=4)
    d.arc([x + s * 0.08, y + s * 0.3, x + s * 0.48, y + s * 0.78], 180, 360, fill=INK, width=4)
    d.arc([x + s * 0.52, y + s * 0.3, x + s * 0.92, y + s * 0.78], 180, 360, fill=INK, width=4)
    cx, cy = x + s * 0.5, y + s * 0.18
    for ang in range(0, 360, 45):
        import math
        dx = math.cos(math.radians(ang)) * s * 0.12
        dy = math.sin(math.radians(ang)) * s * 0.12
        d.line([(cx, cy), (cx + dx, cy + dy)], fill=GOLD, width=3)
    d.ellipse([cx - s * 0.05, cy - s * 0.05, cx + s * 0.05, cy + s * 0.05], fill=GOLD)


def icon_tanker(d, x, y, s):
    d.polygon([(x + s * 0.08, y + s * 0.55), (x + s * 0.92, y + s * 0.55),
               (x + s * 0.8, y + s * 0.8), (x + s * 0.2, y + s * 0.8)], fill=(60, 60, 90))
    d.rectangle([x + s * 0.6, y + s * 0.35, x + s * 0.78, y + s * 0.55], fill=(60, 60, 90))
    for i, fx in enumerate((0.25, 0.45, 0.65)):
        d.polygon([(x + s * fx, y + s * 0.5), (x + s * (fx + 0.06), y + s * 0.28),
                   (x + s * (fx + 0.12), y + s * 0.5)], fill=(220, 120, 20))
    d.line([(x + s * 0.05, y + s * 0.88), (x + s * 0.95, y + s * 0.88)], fill=BLUE, width=3)


def icon_drone(d, x, y, s):
    d.line([(x + s * 0.2, y + s * 0.2), (x + s * 0.8, y + s * 0.8)], fill=INK, width=4)
    d.line([(x + s * 0.8, y + s * 0.2), (x + s * 0.2, y + s * 0.8)], fill=INK, width=4)
    for cx, cy in ((0.2, 0.2), (0.8, 0.2), (0.2, 0.8), (0.8, 0.8)):
        d.ellipse([x + s * (cx - 0.09), y + s * (cy - 0.09),
                   x + s * (cx + 0.09), y + s * (cy + 0.09)], outline=INK, width=3)
    d.ellipse([x + s * 0.42, y + s * 0.42, x + s * 0.58, y + s * 0.58], fill=RED)


def icon_neon(d, x, y, s):
    d.ellipse([x + s * 0.15, y + s * 0.1, x + s * 0.85, y + s * 0.8], fill=(255, 120, 160))
    d.ellipse([x + s * 0.3, y + s * 0.25, x + s * 0.7, y + s * 0.65], fill=(255, 200, 60))
    d.polygon([(x + s * 0.12, y + s * 0.85), (x + s * 0.2, y + s * 0.45),
               (x + s * 0.28, y + s * 0.85)], fill=(20, 120, 80))
    d.polygon([(x + s * 0.72, y + s * 0.85), (x + s * 0.8, y + s * 0.45),
               (x + s * 0.88, y + s * 0.85)], fill=(20, 120, 80))
    d.text((x + s * 0.32, y + s * 0.82), "VI", font=F("DejaVuSans-Bold.ttf", int(s * 0.22)), fill=INK)


def icon_dish(d, x, y, s):
    for i in range(14):
        import random
        random.seed(7 + i)
        sx = x + random.random() * s
        sy = y + random.random() * s * 0.7
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=INK)
    d.arc([x + s * 0.15, y + s * 0.2, x + s * 0.85, y + s * 0.85], 200, 340, fill=GREY, width=5)
    d.line([(x + s * 0.5, y + s * 0.55), (x + s * 0.78, y + s * 0.9)], fill=INK, width=4)
    d.line([(x + s * 0.5, y + s * 0.55), (x + s * 0.28, y + s * 0.78)], fill=INK, width=3)


def icon_dome(d, x, y, s):
    d.polygon([(x + s * 0.5, y + s * 0.1), (x + s * 0.78, y + s * 0.42),
               (x + s * 0.22, y + s * 0.42)], fill=(200, 200, 200), outline=INK)
    d.rectangle([x + s * 0.2, y + s * 0.42, x + s * 0.8, y + s * 0.52], fill=(200, 200, 200), outline=INK)
    for i in range(4):
        cx = x + s * (0.28 + 0.15 * i)
        d.rectangle([cx - s * 0.04, y + s * 0.52, cx + s * 0.04, y + s * 0.82], fill=INK)
    d.rectangle([x + s * 0.15, y + s * 0.82, x + s * 0.85, y + s * 0.9], fill=INK)


def icon_tower(d, x, y, s):
    d.rectangle([x + s * 0.35, y + s * 0.15, x + s * 0.65, y + s * 0.9], fill=(120, 120, 130))
    for i in range(4):
        wy = y + s * (0.25 + 0.16 * i)
        d.rectangle([x + s * 0.4, wy, x + s * 0.6, wy + s * 0.07], fill=(255, 220, 120))
    d.line([(x + s * 0.05, y + s * 0.12), (x + s * 0.4, y + s * 0.3)], fill=RED, width=4)
    d.polygon([(x + s * 0.05, y + s * 0.12), (x + s * 0.14, y + s * 0.1),
               (x + s * 0.12, y + s * 0.2)], fill=RED)


# ------------------------- the news (all verified 19 Nov 2026) -------------------------
# regions: ASIA EUROPE MIDDLE EAST AFRICA AMERICAS GLOBAL

BIG = [
    ("SHENZHEN SUMMIT", "Trump, Xi and Putin meet in first three-way summit",
     "Three nuclear powers meet for 80 minutes at Kylin Villa and issue a joint "
     "\"Declaration toward Peace\": UN reform, more fuel, officials' immunity, "
     "\"a nuclear war cannot be won and must never be fought\". No Ukraine or "
     "Iran mention.",
     "CNA / Al Jazeera", "ASIA", icon_summit),
    ("CYCLONE AKVAN", "100,000+ evacuated as storm bears down on Odisha",
     "Odisha moves 100,000+ people to shelters as Severe Cyclonic Storm Akvan "
     "closes on Gopalpur, due to cross by noon Friday, winds 90-100 km/h "
     "gusting to 110. Schools shut in 11 districts; third cyclone in 24 days.",
     "The Hindu / Indian Express", "ASIA", icon_cyclone),
    ("WORLD COURT", "Myanmar guilty of genocide against the Rohingya, 9-6",
     "The International Court of Justice finds Myanmar committed genocide in "
     "Rakhine state - the first time it has held a state responsible for the "
     "crime. Myanmar and China reject the ruling; survivors call it historic.",
     "AP / ARN News", "EUROPE", icon_scales),
]

SMALL = [
    ("ANTHROPIC'S $83 DEBUT", "IPO opens $111.50, closes $97.17, up 17% - largest listing on record at $81bn. (Reuters)", "AMERICAS", icon_rocket),
    ("MARKETS ROUT", "S&P 500 -2.02%, sixth straight loss; Dow -1,101, first close below 50,000. (AP)", "AMERICAS", icon_chart_down),
    ("GAZA GROUND PUSH", "Israeli tanks push into central Gaza in a new ground operation. (ARN News)", "MIDDLE EAST", icon_tank),
    ("CRIMEA BRIDGE HIT AGAIN", "Ukraine strikes the Crimea bridge a third time this week. (Al Jazeera)", "EUROPE", icon_bridge),
    ("MINES IN THE GULF", "Three oil tankers catch fire after hitting mines east of Hormuz. (NDTV)", "ASIA", icon_tanker),
    ("1,000 DRONES FOR KYIV", "UK unveils a GBP 260m package of 1,000+ long-range strike drones. (gov.uk)", "EUROPE", icon_drone),
    ("GTA VI IS OUT", "The most awaited game in history launches on PS5 and Xbox; PSN outage first. (Rockstar)", "GLOBAL", icon_neon),
    ("VOYAGER, ONE LIGHT-DAY", "NASA confirms Voyager 1 is one light-day out - a first for any craft. (NASA)", "GLOBAL", icon_dish),
    ("SENATE SAYS NO", "US Senate rejects the Iran war-powers resolution 51-48. (AppiSToS)", "AMERICAS", icon_dome),
    ("STRIKE ON RIYADH", "Houthi attack hits a Riyadh tower; damage, no injuries. (ARN News)", "MIDDLE EAST", icon_tower),
]

BRIEFS = [
    ("UK + Norway fund two Ukrainian naval craft", "GBP 100m+ joint programme", "EUROPE"),
    ("Jeffries nominated for Speaker, 251-11", "vote was Wednesday", "AMERICAS"),
    ("Trump pardons baseball star Pete Rose", "posthumous, announced Thursday evening", "AMERICAS"),
    ("Denmark ratifies Trump deal over Greenland", "parliament vote Thursday", "EUROPE"),
    ("US and Venezuela restore military ties", "deal signed, Hegseth says", "AMERICAS"),
    ("Iraqi forces enter Hezbollah stronghold", "Jurf al-Sakhar, under a deal", "MIDDLE EAST"),
    ("Bangladesh deploys paramilitary amid unrest", "over Hasina's return", "ASIA"),
    ("US-Saudi nuclear deal 'satisfactory'", "IAEA verdict", "MIDDLE EAST"),
    ("Egypt unearths Ptolemaic necropolis", "hundreds of coffins found", "AFRICA"),
    ("Qatar Amir in talks with Swiss president", "first state visit", "ASIA"),
    ("Takaichi, Putin hold first talks since 2019", "Japan-Russia leaders meet", "ASIA"),
    ("US sanctions Hezbollah charity network", "gold and cash channels hit", "AMERICAS"),
    ("Nvidia halts Hopper chip shipments to China", "licensed AI chips stopped", "AMERICAS"),
    ("UK-EU draft ends most food border checks", "from March 2028", "EUROPE"),
    ("Barcelona 6-0 Servette in Women's UCL", "Pina hat-trick; Lyon 2-0 Arsenal", "EUROPE"),
    ("Gas blast kills six in Georgia flats", "apartment block explosion", "EUROPE"),
    ("Bus-fuel truck crash kills 10 in Pakistan", "southwest Pakistan", "ASIA"),
    ("Pakistan army: 22 militants killed", "northwest raids", "ASIA"),
    ("France jails 3 women who joined ISIS", "sentenced over Syria travel", "EUROPE"),
    ("US renews warnings for Bahrain, Saudi", "security alerts reissued", "MIDDLE EAST"),
]

NUMBERS = [
    ("100,000+", "EVACUATED IN ODISHA"),
    ("9-6", "ICJ GENOCIDE VOTE"),
    ("$83 to $97", "ANTHROPIC, +17% DAY ONE"),
    ("-2.02%", "S&P 500, 6TH LOSS IN A ROW"),
    ("1,000+", "UK DRONES FOR UKRAINE"),
    ("3", "TANKERS ABLAZE, HORMUZ"),
]

# coarse continent outlines (lon, lat) for the stylised map
CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 71), (-110, 68), (-95, 69), (-85, 66), (-80, 62),
     (-75, 58), (-65, 60), (-60, 55), (-55, 47), (-65, 45), (-70, 42), (-75, 35),
     (-80, 32), (-84, 30), (-90, 29), (-97, 26), (-105, 23), (-110, 24), (-115, 29),
     (-120, 34), (-125, 40), (-125, 49), (-132, 54), (-145, 60), (-158, 58), (-168, 66)],
    [(-80, 10), (-77, 7), (-80, 0), (-81, -5), (-78, -12), (-72, -18), (-70, -23),
     (-70, -30), (-65, -38), (-68, -45), (-66, -52), (-60, -50), (-55, -38),
     (-48, -30), (-40, -22), (-35, -8), (-42, -3), (-50, 0), (-55, 5), (-60, 8),
     (-68, 11), (-75, 11), (-80, 10)],
    [(-18, 35), (-10, 37), (-9, 43), (-2, 44), (-2, 48), (0, 46), (-4, 48),
     (2, 51), (5, 53), (8, 57), (10, 59), (12, 56), (18, 56), (21, 55),
     (24, 58), (28, 60), (30, 62), (30, 70), (40, 68), (45, 68), (50, 69),
     (55, 68), (60, 69), (68, 66), (70, 72), (75, 72), (80, 73), (85, 75),
     (95, 76), (105, 77), (110, 74), (120, 73), (130, 72), (140, 72), (150, 70),
     (160, 69), (170, 67), (178, 65), (178, 62), (170, 60), (162, 58), (158, 52),
     (150, 59), (142, 55), (140, 45), (135, 43), (130, 42), (127, 40), (122, 38),
     (120, 32), (118, 25), (110, 20), (108, 12), (105, 9), (100, 7), (98, 12),
     (95, 16), (92, 21), (88, 22), (85, 19), (80, 15), (77, 8), (73, 16),
     (70, 20), (66, 25), (62, 25), (58, 26), (54, 27), (50, 29), (48, 30),
     (44, 29), (40, 31), (36, 36), (33, 36), (30, 36), (27, 37), (23, 36),
     (20, 40), (19, 42), (15, 44), (12, 44), (8, 44), (3, 43), (0, 40),
     (-2, 37), (-6, 36), (-9, 37), (-9, 43), (-18, 35)],
    [(-6, 35), (-10, 31), (-15, 27), (-17, 21), (-17, 15), (-12, 8), (-8, 5),
     (0, 5), (6, 4), (9, 4), (12, -2), (13, -8), (12, -15), (13, -22),
     (16, -28), (19, -33), (25, -34), (28, -32), (32, -28), (35, -22),
     (38, -18), (40, -12), (42, -6), (45, -2), (48, 2), (51, 10), (44, 12),
     (40, 15), (38, 18), (37, 22), (35, 28), (33, 31), (30, 32), (25, 32),
     (20, 32), (15, 32), (10, 34), (5, 37), (-2, 35), (-6, 35)],
    [(113, -22), (114, -30), (115, -34), (120, -34), (125, -33), (130, -32),
     (132, -32), (135, -35), (138, -35), (140, -38), (145, -38), (147, -39),
     (150, -37), (153, -32), (153, -27), (150, -23), (146, -19), (142, -15),
     (142, -11), (137, -12), (135, -15), (132, -12), (130, -13), (126, -14),
     (122, -17), (118, -20), (113, -22)],
]

MAP_DOTS = [  # (lon, lat, number, label)
    (114, 22, "1", "SHENZHEN"), (85, 20, "2", "ODISHA"), (34, 31, "3", "GAZA"),
    (56, 26, "4", "HORMUZ"), (47, 25, "5", "RIYADH"), (4, 52, "6", "THE HAGUE"),
    (34, 45, "7", "CRIMEA"), (13, 52, "8", "BERLIN"), (-77, 39, "9", "WASHINGTON"),
    (0, 51, "10", "LONDON"),
]


def draw_map(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 235, 240), outline=RULE)
    for poly in CONTINENTS:
        pts = []
        for lon, lat in poly:
            px = x + (lon + 180) / 360.0 * w
            py = y + (90 - lat) / 180.0 * h
            pts.append((px, py))
        d.polygon(pts, fill=(190, 205, 180), outline=(140, 155, 135))
    for lon, lat, num, label in MAP_DOTS:
        px = x + (lon + 180) / 360.0 * w
        py = y + (90 - lat) / 180.0 * h
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=(255, 255, 255), width=2)
        d.text((px - 3, py - 6), num, font=F("DejaVuSans-Bold.ttf", 9), fill=(255, 255, 255))
    d.text((x + 6, y + 4), "WHERE THE NEWS HAPPENED", font=f_map, fill=INK)


def region_counts():
    counts = {}
    for it in BIG:
        counts[it[4]] = counts.get(it[4], 0) + 1
    for it in SMALL:
        counts[it[2]] = counts.get(it[2], 0) + 1
    for _, _, r in BRIEFS:
        counts[r] = counts.get(r, 0) + 1
    order = ["ASIA", "EUROPE", "MIDDLE EAST", "AFRICA", "AMERICAS", "GLOBAL"]
    return "  .  ".join("%s %d" % (r, counts.get(r, 0)) for r in order), sum(counts.values())


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    MX = 24
    CW = W - 2 * MX

    # masthead
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, 12), title, font=f_title, fill=INK)
    d.text((MX, 78), "THURSDAY 19 NOVEMBER 2026", font=f_date, fill=RED)
    regions, total = region_counts()
    f_reg = F("DejaVuSans-Bold.ttf", 12)
    rw = d.textlength(regions, font=f_reg)
    d.text((W - MX - rw, 81), regions, font=f_reg, fill=INK)
    hline(d, MX, W - MX, 102, fill=INK, w=3)

    # big-number strip
    y0 = 110
    bw = (CW - 5 * 6) / 6
    for i, (num, lab) in enumerate(NUMBERS):
        x = MX + i * (bw + 6)
        d.rectangle([x, y0, x + bw, y0 + 46], fill=(255, 255, 255), outline=RULE)
        nw = d.textlength(num, font=f_num)
        d.text((x + (bw - nw) / 2, y0 + 3), num, font=f_num, fill=RED)
        lw = d.textlength(lab, font=f_numlab)
        d.text((x + (bw - lw) / 2, y0 + 29), lab, font=f_numlab, fill=INK)

    # three big features
    y0 = 166
    colw = (CW - 2 * 11) / 3
    for i, (kick, head, body, src, _reg, icon) in enumerate(BIG):
        x = MX + i * (colw + 11)
        d.rectangle([x, y0, x + colw, y0 + 84], fill=LIGHT, outline=RULE)
        icon(d, x + colw / 2 - 42, y0 + 2, 84)
        yy = y0 + 92
        d.text((x, yy), kick, font=f_big2, fill=RED)
        yy += 20
        for ln in wrap(head, f_big, colw):
            d.text((x, yy), ln, font=f_big, fill=INK)
            yy += 22
        yy += 2
        yy = text_block(d, x, yy, wrap(body, f_body, colw), f_body, leading=15)
        d.text((x, yy + 3), "Source: " + src, font=f_src, fill=GREY)
    hline(d, MX, W - MX, 418, fill=RULE, w=1)

    # ten small illustrated stories, 2 columns x 5 rows
    y0 = 428
    cellw = (CW - 11) / 2
    rowh = 48
    for i, (head, body, _reg, icon) in enumerate(SMALL):
        r, c = divmod(i, 2)
        x = MX + c * (cellw + 11)
        y = y0 + r * rowh
        d.rectangle([x, y, x + 46, y + 44], fill=LIGHT, outline=RULE)
        icon(d, x + 2, y + 2, 42)
        tx = x + 54
        d.text((tx, y), head, font=f_small, fill=INK)
        bl = wrap(body, f_smbody, cellw - 54)
        text_block(d, tx, y + 18, bl[:2], f_smbody, leading=14)
    hline(d, MX, W - MX, 674, fill=RULE, w=1)

    # map (left) + briefs (right)
    y0 = 678
    mapw = 300
    draw_map(d, MX, y0, mapw, 200)
    f_leg = F("DejaVuSans.ttf", 10)
    d.text((MX, y0 + 204), "1 Shenzhen  2 Odisha  3 Gaza  4 Hormuz  5 Riyadh", font=f_leg, fill=INK)
    d.text((MX, y0 + 217), "6 The Hague  7 Crimea  8 Berlin  9 Washington  10 London", font=f_leg, fill=INK)
    bx = MX + mapw + 12
    bwid = (W - MX - bx)
    colw2 = (bwid - 10) / 2
    f_brief = F("DejaVuSans.ttf", 11)
    f_briefb = F("DejaVuSans-Bold.ttf", 11)
    for i, (head, sub, _reg) in enumerate(BRIEFS):
        r, c = divmod(i, 2)
        x = bx + c * (colw2 + 10)
        y = y0 + r * 24
        d.text((x, y), "- " + head, font=f_briefb, fill=INK)
        d.text((x, y + 11), "  " + sub, font=f_brief, fill=GREY)

    # date check
    y0 = 920
    d.rectangle([MX, y0, W - MX, y0 + 54], fill=(255, 255, 255), outline=RED, width=2)
    check = ("DATE CHECK: Thursday's news - summit, ICJ ruling, Akvan evacuations, Anthropic "
             "debut, Gaza, Crimea, Hormuz, UK drones, GTA VI, Senate vote, Riyadh strike. "
             "Announced Wednesday, in Thursday's papers - Jeffries nominated 251-11; Voyager "
             "crossed one light-day Wed, confirmed Thu. Left out: North Korea's flag change "
             "was reported 13 Nov, not Thursday; no credible 19 Nov source for a North "
             "Korean missile launch.")
    yy = y0 + 5
    for ln in wrap(check, f_check, CW - 16):
        d.text((MX + 8, yy), ln, font=f_check, fill=INK)
        yy += 14

    # footer
    foot = ("Sources: CNA, Al Jazeera, The Hindu, Indian Express, AP, Reuters, Bloomberg, ARN News, "
            "NDTV, gov.uk, Kyiv Post, Rockstar Games, NASA, AppiSToS. 33 stories, every one checked "
            "against reporting of 19 November 2026.")
    yy = 980
    for ln in wrap(foot, f_foot, CW):
        d.text((MX, yy), ln, font=f_foot, fill=GREY)
        yy += 13

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    render()
