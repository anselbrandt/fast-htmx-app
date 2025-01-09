from app.constants import ROOT_PATH


def test_root_path_is_string():
    result = ROOT_PATH
    assert isinstance(
        result, str
    ), f"Expected result to be a string, but got {type(result)}"
