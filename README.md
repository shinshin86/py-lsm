# lsm

This is a Python implementation of the **l**ocal**S**torage **m**ock.

The behavior is not perfectly reproduced (The value returned when an unintended value is passed, for example), but the basic logic is implemented.

## Usage

```python
from lsm import LocalStorageMock

lsm = LocalStorageMock()

lsm.set_item('testkey', 'testvalue');
print(lsm.get_item('testkey'))
# => testvalue
print(lsm.key(0))
# => testkey
print(lsm.length)
# => 1

lsm.remove_item('testkey')
print(lsm.length)
# => 0
print(lsm.get_item('testkey'))
# => None

lsm.set_item('testkey', 'testvalue');
print(lsm.get_item('testkey'))
# => testvalue

lsm.clear()
print(lsm.get_item('testkey'))
# => None
print(lsm.length)
# => 0
```

## Test

```sh
python -m unittest
```

