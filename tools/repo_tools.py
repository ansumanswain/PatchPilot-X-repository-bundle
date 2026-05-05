import os

def get_repo_structure(repo_path):
    structure = []

    for root, dirs, files in os.walk(repo_path):
        level = root.replace(repo_path, '').count(os.sep)
        indent = ' ' * 2 * level
        structure.append(f"{indent}{os.path.basename(root)}/")

        subindent = ' ' * 2 * (level + 1)

        for file in files:
            structure.append(f"{subindent}{file}")

    return "\n".join(structure)
