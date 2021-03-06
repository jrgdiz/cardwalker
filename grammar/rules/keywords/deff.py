from pyparsing import *

from ...constants.math.deff import NUM
from ...constants.prepositions.deff import FROM
from ...constants.keywords.deff import *
from ...constants.verbs.deff import ENCHANT, HAUNT, EQUIP, FORTIFY
from ...functions.deff import oneOfNamed, loadFromFile, delimitedListAnd
from ...mana.deff import color, manapayment
from ...types.deff import land_type, subtype, type_
from ...entities.articles.deff import amount
from ...entities.subjects.deff import objects

from decl import *

basic_keyword << BASICKEYWORD
number_keyword << NUMBERKEYWORD + amount
costed_keyword << COSTEDKEYWORD + manapayment

# these go apart because they are also verbs
haunt << HAUNT
equip << EQUIP + manapayment
fortify << FORTIFY + manapayment
enchant << ENCHANT + type_

# cycling goes apart because we need to extract the type
cycling << Optional(subtype) + Suppress(CYCLING) + manapayment

landwalk << land_type + WALK # legendary landwalk will fail this

protection << Suppress(PROTECTION) + delimitedListAnd(Suppress(FROM) + color)

keywords << delimitedListAnd( \
		protection
		| basic_keyword
		| number_keyword
		| costed_keyword
		| cycling
		| landwalk
		| enchant
		| haunt
		| equip
		| fortify
)