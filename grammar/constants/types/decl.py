from pyparsing import *

THISCARD = Forward()

SUPERTYPE = Forward()
TYPE_ = Forward()

BASICLANDTYPE = Forward()
OTHERLANDTYPE = Forward()
CREATURETYPE = Forward()
ARTIFACTTYPE = Forward()
PLANESWALKERTYPE = Forward()
ENCHANTMENTTYPE = Forward()
SPELLTYPE = Forward()

FREQUENCY = Forward()