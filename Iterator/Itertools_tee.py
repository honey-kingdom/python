
import Itertools_groupby
import itertools


person_group = itertools.groupby(
    Itertools_groupby.people, Itertools_groupby.get_state)

copy1, copy2 = itertools.tee(person_group)
# after copying, original gets exhausted
