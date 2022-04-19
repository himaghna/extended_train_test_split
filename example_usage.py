import numpy as np

from extended_train_test_split.interfaces import (
    train_test_split_molecules,
    train_test_split_images,
)

from extended_train_test_split import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    np.array([10, 11, 12]),
    test_size=0.2,
    train_size=0.8,
    splitter='random',
    hopts={
        "shuffle": True,
        "random_state": 42,
    }

)

print(X_train, X_test, y_train, y_test)

X_train, X_test, y_train, y_test = train_test_split_molecules(
    ['C', 'CC', 'CCC', 'CCCC', 'CCCCC'],
    np.array([10, 11, 12, 13, 14]),
    test_size=0.2,
    train_size=0.8,
    return_as='fprint',
    splitter='random',
    hopts={'random_state': 42},
    fprints_hopts={'radius': 2},
)

print(X_train, X_test, y_train, y_test)


X_train, X_test, y_train, y_test = train_test_split_molecules(
    ['C', 'CC', 'CCC', 'CCCC', 'CCCCC'],
    np.array([10, 11, 12, 13, 14]),
    test_size=0.2,
    train_size=0.8,
    return_as='fprint',
    splitter='kennard_stone',
    fprints_hopts={'radius': 2},
)

print(X_train, X_test, y_train, y_test)
'''
Each of these specialized interfaces needs to take additional keyword args
specific to their use case. For example, molecules needs to take a
fingerprint (and maybe another **fprint_hopts)

All other special hyperparamters for the splitters need to be taken
by the interfaces and then just passed onto train_test_split.
'''
