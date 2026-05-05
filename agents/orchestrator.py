from agents.planner import create_plan
from agents.coder import generate_fix
from agents.tester import execute_tests
from agents.reviewer import summarize_changes
from tools.repo_tools import get_repo_structure
from tools.file_tools import read_file, write_file
from rich import print
from rich.panel import Panel

MAX_RETRIES = 3

class PatchPilot:
    def __init__(self, repo_path, target_file):
        self.repo_path = repo_path
        self.target_file = target_file

    def run(self, task):
        structure = get_repo_structure(self.repo_path)

        print(Panel.fit("[bold cyan]PATCHPILOT INITIALIZED[/bold cyan]"))

        plan = create_plan(task, structure)
        print(plan)

        retries = 0
        latest_results = ""

        while retries < MAX_RETRIES:
            code = read_file(self.target_file)

            updated_code = generate_fix(task, code, latest_results)

            write_file(self.target_file, updated_code)

            latest_results = execute_tests(self.repo_path)

            print(latest_results)

            if "failed" not in latest_results.lower():
                print(Panel.fit("[bold green]ALL TESTS PASSING[/bold green]"))
                break

            retries += 1

        summary = summarize_changes(task, latest_results)
        print(summary)
