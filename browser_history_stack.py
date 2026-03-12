# File: browser_history_stack.py
# Real-world application of Stack: Browser Back Navigation

class BrowserHistory:
    def __init__(self):
        self.history = []

    def visit_page(self, page):
        self.history.append(page)
        print(f"Visited: {page}")

    def go_back(self):
        if len(self.history) <= 1:
            print("No previous page to go back to.")
            return

        current_page = self.history.pop()
        print(f"Going back from: {current_page}")
        print(f"Now on: {self.history[-1]}")

    def show_current_page(self):
        if not self.history:
            print("No page opened yet.")
        else:
            print(f"Current page: {self.history[-1]}")

    def show_history(self):
        if not self.history:
            print("History is empty.")
            return

        print("Browser History:")
        for page in self.history:
            print(page)


def main():
    browser = BrowserHistory()

    browser.visit_page("google.com")
    browser.visit_page("youtube.com")
    browser.visit_page("github.com")
    browser.show_current_page()
    print()

    browser.go_back()
    browser.show_current_page()
    print()

    browser.go_back()
    browser.show_current_page()
    print()

    browser.show_history()


if __name__ == "__main__":
    main()
