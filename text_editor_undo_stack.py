# File: text_editor_undo_stack.py
# Real-world application of Stack: Undo in Text Editor

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []

    def write(self, word):
        self.undo_stack.append(self.text)
        self.text += word
        print(f"After writing: {self.text}")

    def delete_last(self, count):
        self.undo_stack.append(self.text)
        self.text = self.text[:-count]
        print(f"After delete: {self.text}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return

        self.text = self.undo_stack.pop()
        print(f"After undo: {self.text}")

    def show_text(self):
        print(f"Current text: {self.text}")


def main():
    editor = TextEditor()

    editor.write("Hello")
    editor.write(" World")
    editor.show_text()
    print()

    editor.delete_last(3)
    editor.show_text()
    print()

    editor.undo()
    editor.show_text()
    print()

    editor.undo()
    editor.show_text()


if __name__ == "__main__":
    main()
