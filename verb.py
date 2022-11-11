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

    'read': VerbClass.READ,

    'nap': VerbClass.NAP,

    'scratch': VerbClass.SCRATCH,

    'use': VerbClass.USE,

    'invite': VerbClass.INVITE,

    'talk': VerbClass.TALK,

    'wear': VerbClass.WEAR,

    'listen': VerbClass.LISTEN

}
