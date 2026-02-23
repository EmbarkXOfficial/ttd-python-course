from first.app.FirstPython import add


# Syntax : assert <condition>, <message>


def test_add_number():
    assert add(30, 40) == 70
    assert add(20, 40) == 70, "Addition failed"


def test_add_string():
    output = add("I love", " Python")
    print(output)
    assert type(output) is str
    assert "love" in output
    assert "I love Python" == output
