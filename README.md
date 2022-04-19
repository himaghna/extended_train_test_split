# extended_train_test_split

<h1 align="center">extended_train_test_split</h1> 
<h3 align="center">Algorithmic train:test splitting for molecules, images, and arbitrary arrays.</h3>

<p align="center">  
  <img alt="extended_train_test_splitlogo" src="https://github.com/JacksonBurns/extended_train_test_split/blob/main/extended_train_test_split_logo.png">
</p> 
<p align="center">
  <img alt="GitHub Repo Stars" src="https://img.shields.io/github/stars/JacksonBurns/extended_train_test_split?style=social">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/extended_train_test_split">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/extended_train_test_split">
  <img alt="PyPI - License" src="https://img.shields.io/github/license/JacksonBurns/extended_train_test_split">
</p>

## Online Documentation
[Click here to read the docuemtntation](https://JacksonBurns.github.io/extended_train_test_split/)

## Extending Functionality
Adding a new splitting method should take on this format:

```python
def random(
    X,
    y=None,
    test_size=None,
    train_size=None,
    random_state=None,
    shuffle=True,
    stratify=None,
):
    return train_test_split(
        X,
        y,
        test_size=test_size,
        train_size=train_size,
        random_state=random_state,
        shuffle=shuffle,
        stratify=stratify,
    )
```

It can be as simple as a passthrough to a another `train_test_split`, or it can be an original implementation that results in X and y being split into two lists.


Adding a new interface should take on this format:

```python
from extended_train_test_split import train_test_split

def train_test_split_INTERFACE(
    INTERFACE_input,
    INTERFACE_ARGS,
    y: np.array = None,
    test_size: float = 0.25,
    train_size: float = 0.75,
    splitter: str = 'random',
    hopts: dict = {},
    INTERFACE_hopts: dict = {},
):
    # turn the INTERFACE_input into an input X
    # based on INTERFACE ARGS where INTERFACE_hopts
    # specifies additional behavior
    X = []
    
    # call train test split with this input
    return train_test_split(
        X,
        y=y,
        test_size=test_size,
        train_size=train_size,
        splitter=splitter,
        hopts=hopts,
    )
```