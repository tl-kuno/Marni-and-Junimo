from enum import Enum


class VerbClass(Enum):
    MOVE = 0
    TAKE = 1
    DROP = 2
    EAT = 3
    READ = 4
    NAP = 5
    SCRATCH = 6
    USE = 7
    INVITE = 8
    TALK = 9
    WEAR = 10
    LISTEN = 11
    MOVE_PRIME = 12
    LOOK = 13
    LOOK_AT = 14
    SAVE = 15
    LOAD = 16


verb_dict = {
    'move': VerbClass.MOVE,
    'run': VerbClass.MOVE,
    'go': VerbClass.MOVE,
    'navigate': VerbClass.MOVE,

    'take': VerbClass.TAKE,
    'pick': VerbClass.TAKE,
    'grab': VerbClass.TAKE,
    'select': VerbClass.TAKE,

    'drop': VerbClass.DROP,
    'delete': VerbClass.DROP,
    'discard': VerbClass.DROP,

    'eat': VerbClass.EAT,
    'consume': VerbClass.EAT,
    'devour': VerbClass.EAT,
    'gobble': VerbClass.EAT,

    'read': VerbClass.READ,
    'scan': VerbClass.READ,
    'skim': VerbClass.READ,

    'nap': VerbClass.NAP,
    'sleep': VerbClass.NAP,
    'rest': VerbClass.NAP,
    'chill': VerbClass.NAP,

    'scratch': VerbClass.SCRATCH,
    'itch': VerbClass.SCRATCH,
    'scrape': VerbClass.SCRATCH,

    'use': VerbClass.USE,

    'invite': VerbClass.INVITE,

    'talk': VerbClass.TALK,
    'chat': VerbClass.TALK,
    'whisper': VerbClass.TALK,
    'speak': VerbClass.TALK,
    'yell': VerbClass.TALK,

    'wear': VerbClass.WEAR,

    'listen': VerbClass.LISTEN,
    'hear': VerbClass.LISTEN,

    'look': VerbClass.LOOK,

    'look at': VerbClass.LOOK_AT,

    'savegame': VerbClass.SAVE,

    'loadgame': VerbClass.LOAD

}
