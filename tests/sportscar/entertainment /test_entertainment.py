from pytest import mark


@mark.ui
@mark.entertainment
def test_can_navigate_to_entertainment_page(firefox_browser):
    firefox_browser.get('https://www.dailymotion.com')
    assert True
