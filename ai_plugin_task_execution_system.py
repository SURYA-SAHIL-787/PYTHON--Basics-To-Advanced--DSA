from abc import ABC, abstractmethod


class UnsupportedTaskError(Exception):
    pass


class Task:
    def __init__(self, task_type, data):
        self.task_type = task_type
        self.data = data

    def __str__(self):
        return f"Task(type={self.task_type}, data={self.data})"


class Plugin(ABC):
    def __init__(self, name):
        self._name = name
        self._execution_count = 0

    @abstractmethod
    def can_handle(self, task):
        pass

    @abstractmethod
    def execute(self, task):
        pass

    def get_stats(self):
        return f"{self._name} executed {self._execution_count} time(s)"

    def _increase_count(self):
        self._execution_count += 1

    def __add__(self, other):
        return Workflow([self, other])


class TranslationPlugin(Plugin):
    def can_handle(self, task):
        return task.task_type == "translate"

    def execute(self, task):
        if not self.can_handle(task):
            raise UnsupportedTaskError(f"{self._name} cannot handle {task.task_type}")
        self._increase_count()
        text = task.data
        return f"{self._name} translated text: {text[::-1]}"


class SummarizationPlugin(Plugin):
    def can_handle(self, task):
        return task.task_type == "summarize"

    def execute(self, task):
        if not self.can_handle(task):
            raise UnsupportedTaskError(f"{self._name} cannot handle {task.task_type}")
        self._increase_count()
        words = task.data.split()
        short_summary = " ".join(words[:5]) + ("..." if len(words) > 5 else "")
        return f"{self._name} summary: {short_summary}"


class CodeReviewPlugin(Plugin):
    def can_handle(self, task):
        return task.task_type == "code_review"

    def execute(self, task):
        if not self.can_handle(task):
            raise UnsupportedTaskError(f"{self._name} cannot handle {task.task_type}")
        self._increase_count()
        code = task.data
        issues = []
        if "print(" in code:
            issues.append("Debug print found")
        if "global " in code:
            issues.append("Global keyword used")
        if not issues:
            issues.append("No major issues found")
        return f"{self._name} review: {', '.join(issues)}"


class Workflow:
    def __init__(self, plugins):
        self.plugins = plugins

    def __add__(self, other):
        if isinstance(other, Plugin):
            return Workflow(self.plugins + [other])
        elif isinstance(other, Workflow):
            return Workflow(self.plugins + other.plugins)
        else:
            raise TypeError("Can only add Plugin or Workflow")

    def run(self, task):
        for plugin in self.plugins:
            if plugin.can_handle(task):
                return plugin.execute(task)
        raise UnsupportedTaskError(f"No plugin available for task type: {task.task_type}")

    def show_stats(self):
        for plugin in self.plugins:
            print(plugin.get_stats())


# Driver Code
translator = TranslationPlugin("TranslateAI")
summarizer = SummarizationPlugin("SummaryAI")
reviewer = CodeReviewPlugin("CodeInspector")

workflow = translator + summarizer + reviewer

task1 = Task("translate", "hello world")
task2 = Task("summarize", "Python OOP helps in building reusable and scalable software systems")
task3 = Task("code_review", "global x\nprint(x)")
task4 = Task("image_generation", "create a cat image")

print(workflow.run(task1))
print(workflow.run(task2))
print(workflow.run(task3))

try:
    print(workflow.run(task4))
except UnsupportedTaskError as e:
    print("Error:", e)

workflow.show_stats()
