import rpa as r

# use init() to start TagUI, it auto downloads TagUI on first run
# default init(visual_automation = False, chrome_browser = True)
r.init()

# use url('your_url') to go to web page, url() returns current URL
r.url('https://ca.yahoo.com')

# use type() to enter text into an UI element or x, y location
# '[enter]' = enter key, '[clear]' = clear field
r.type('search-box', 'github')

# use read() to fetch and return text from UI element
search_text = r.read('search-box')
print(search_text)

# use click() to click on an UI element or x, y location
# rclick() = right-click, dclick() = double-click
r.click('search-button')

r.wait(6.6)

# use snap() to save screenshot of page or UI element
# page = web page, page.png = computer screen
r.snap('page', 'results.png')
r.snap('logo', 'logo.png')
r.wait(4.4)

r.click('GitHub')
r.wait(10)

r.close()