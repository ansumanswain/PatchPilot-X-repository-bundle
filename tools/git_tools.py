from git import Repo

def create_branch(repo_path, branch_name):
    repo = Repo(repo_path)
    repo.git.checkout('-b', branch_name)
