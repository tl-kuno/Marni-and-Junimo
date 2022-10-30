from enum import Enum

class VerbClass(Enum):
  move = 0
  take = 1
  Eat = 2
  read = 3
  nap = 4
  scratch = 5
  give = 6
  use = 7
  invite = 8
  talk = 9
  wear = 10
  drop = 11


verb_dict = {
  'move':VerbClass.move,
  'run': VerbClass.move,
  'go': VerbClass.move,
  'navigate': VerbClass.move,
  'take': VerbClass.take,
  'pick': VerbClass.take,
  'grab': VerbClass.take,
  'select': VerbClass.take
}