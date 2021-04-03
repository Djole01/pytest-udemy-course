from pytest import mark


@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(firefox_browser):
    firefox_browser.get('https://www.engine.com')
    assert True
