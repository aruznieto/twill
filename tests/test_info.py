from .util import execute_script


def test(url):
    execute_script('test_info.twill', initial_url=url)
