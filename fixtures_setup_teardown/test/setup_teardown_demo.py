# module level setup and tear down
def setup_module():
    print("Open db connection")


def teardown_module():
    print("Close db connection")


# function level setup and tear down
def setup_function():
    print("function : Open db connection")


def teardown_function():
    print("function : Close db connection")


def test_multiply():
    print("Multiply executed")


def test_divide():
    print("Divide executed")


def test_mod():
    print("Mod executed")
