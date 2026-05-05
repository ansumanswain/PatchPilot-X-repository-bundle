import subprocess

def run_command(command, cwd=None):
    result = subprocess.run(
        command,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True,
    )

    return result.stdout + result.stderr
