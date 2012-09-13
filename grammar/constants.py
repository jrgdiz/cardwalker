from pyparsing import *
from basic import *

THIS = CaselessLiteral("this")
THAT = CaselessLiteral("that")

BE = or_cs(["is", "are"])
HAVE = or_cs(["has", "have"])
GET = or_cs(["get", "gets"])
CANT = or_cl(["can't"])
MUST = or_cl(["must"])
FROM = Suppress("from")
AN = or_cs(["a", "an"])
THE = CaselessLiteral("the")
OTHER = CaselessLiteral("other")
ANOTHER = CaselessLiteral("another")
ALONE = CaselessLiteral("alone")

WHEN = or_cl (["when", "whenever"])
WHERE = CaselessLiteral("where")
TARGET = CaselessLiteral("target")
MAY = CaselessLiteral("may")
TO = CaselessLiteral("to")
UPTO = CaselessLiteral("up") + TO
OF = CaselessLiteral("of")
ON = CaselessLiteral("on")
ONTO = CaselessLiteral("onto")
INTO = CaselessLiteral("into")
WITH = CaselessLiteral("with")
BY = CaselessLiteral("by")
AT = CaselessLiteral("at")
FOR = CaselessLiteral("for")
UNTIL = CaselessLiteral("until")
UNDER = CaselessLiteral("under")
NEXT = CaselessLiteral("next")
WITH = CaselessLiteral("with")
EQUAL = CaselessLiteral("equal")

DESTROY = or_cl(["destroy", "destroys", "destroyed"])
EXILE = or_cl(["exile", "exiles", "exiled"])
GAIN = or_cl(["gain", "gains", "gained"])
LIFE = CaselessLiteral("life")
LOSE = or_cl(["lose", "loses", "lost"])
TAP = or_cl(["tap", "taps"])
UNTAP = or_cl(["untap", "untaps", "untapped"])
DISCARD = or_cl(["discard", "discards", "discard"])
SACRIFICE = or_cl(["sacrifice", "sacrifices", "sacrificed"])
DRAW = or_cl(["draw", "draws", "drawn"])
DEAL = or_cl(["deal", "deals", "dealt"])
DAMAGE = CaselessLiteral("damage")
PAY = or_cl(["pay", "pays", "paid"])
PUT = or_cl(["put", "puts"])
ATTACK = or_cl(["attack", "attacks", "attacking"])
BLOCK = or_cl(["block", "blocks", "blocking"])
BECOME = or_cl(["become", "becomes"])
REDUCE = or_cl(["reduce", "reduced", "reduces"])
RETURN = or_cl(["return", "returned", "returns"])
ENTER = or_cl(["enter", "enters"])
LEAVE = or_cl(["leave", "leaves"])
DIE = or_cl(["die", "dies", "died"])
PREVENT = or_cl(["prevent", "prevents", "prevented"])
ADD = or_cl(["add", "adds", "added"])
REGENERATE = or_cl(["regenerate", "regenerates", "regenerated"])

SPELL = or_cl(["spell", "spells"])
PERMANENT = or_cl(["permanent", "permanents"])
CARD = or_cl(["card", "cards"])
ABILITY = or_cl(["ability", "abilities"])
COUNTER = or_cl(["counter"])
COUNTERSPELL = or_cl(["counter", "counters"])

CONTROL = or_cl (["control", "controls"])
IT = CaselessLiteral("it")
IN = CaselessLiteral("in")
HIS = CaselessLiteral("his or her")
ALL = CaselessLiteral("all")
EACH = CaselessLiteral("each")

CONTROLLER = or_cl(["controller", "controllers"])
OWNER = or_cl(["owner", "owners"])
YOU = CaselessLiteral("you")
PLAYER = or_cl(["player", "players"])
OPPONENT = or_cl(["opponent", "opponents"])

ITS = or_cl(["its", "their"])
YOUR = CaselessLiteral("your")
THEIR = CaselessLiteral("their")
POSS = or_cl(["' ", "'s"])

HAND = or_cl(["hand", "hands"])
GRAVEYARD = or_cl(["graveyard", "graveyards"])
LIBRARY = or_cl(["library", "libraries"])
EXILE = CaselessLiteral("exile")
BATTLEFIELD = CaselessLiteral("battlefield")

ATRANDOM = CaselessLiteral("at random")
TOTAL = CaselessLiteral("total")
SIZE = CaselessLiteral("size")
NUMBER = CaselessLiteral("number")

BEGINNING = CaselessLiteral("beginning")
END = CaselessLiteral("end")
TOP = CaselessLiteral("top")
BOTTOM = CaselessLiteral("bottom")

TURN = CaselessLiteral("turn")
UPKEEP = CaselessLiteral("upkeep")
DRAWSTEP = CaselessLiteral("draw step")
PRECOMBAT = CaselessLiteral("first main phase")
COMBAT = CaselessLiteral("combat phase")
POSCOMBAT = CaselessLiteral("second main phase")

MANA = CaselessLiteral("mana")
POOL = CaselessLiteral("pool")
SOURCE = or_cl(["source", "sources"])