from pytest import mark


'''
@mark.parametrize('tv_brand', [
    ('Samsung'),
    ('Sony'),
    ('Vizio')
    ]
)
 #parameters moved to an external json file
'''

def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")   # print statemenet example, normally 
                                                # there would be some test logic 
                                                # testing against different parameter
                                                
@mark.skip                                                 
def test_browser_can_navigate_to_xwebpage(browser):
    browser.get('http://qwant.com')
    
