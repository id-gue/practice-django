# Assertions in Unit tests and integration tests

assert 2 == 2   # passes
assert 2 == 3   # fails

if assert 2 != 3:
    raise Exeption('fail')

assert == "make sure"

# AssertIs means the objects are identical
# AssertEqual means Values are the same

# very generally speaking:
# F - error in code or tests are to strict
# E - error in test
