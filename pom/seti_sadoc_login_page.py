
class SetiSadocLoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://uat.qsep.cms.gov/Events/login.aspx?event=SETISADOC&eventsubtype=SETI")

    def login(self, email):
        self.page.locator("#MainContentPlaceholder_EmailTextBox").click()
        self.page.locator("#MainContentPlaceholder_EmailTextBox").fill(email)
        self.page.get_by_role("button", name="Submit").click()
