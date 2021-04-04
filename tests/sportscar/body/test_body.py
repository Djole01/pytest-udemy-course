from pytest import mark


@mark.body
class BodyTests:
    @mark.ui
    @mark.door
    def test_body(self):
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True


# markers
# runs tests for body + engine
# pytest -m "body or engine"

# runs tests for everything not marked as entertainment
# pytest -m "not entertainment"

# lists all markers documented in pytest.ini
# pytest --markers
