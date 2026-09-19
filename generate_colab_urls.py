import os
from urllib.parse import quote


def generate_colab_urls(file_path):
    """
    Generate Google Colab URLs for all Jupyter Notebook files in the specified directory.
    Toggle off Google AI assistant to avoid generating solutions.
    Set metadata to prevent the AI from generating solutions.

    Args:
        file_path (str): The path to the directory containing Jupyter Notebook files.

    Returns:
        list: A list of Google Colab URLs for each Jupyter Notebook file.
    """
    colab_base_url = "https://colab.research.google.com/github/"
    colab_urls = []

    # Get the GitHub repository URL from the environment variable
    github_repo_name = "csc-8000"
    github_username = "mgruppi"
    notebook_path = "Lectures"
    if not github_repo_name:
        raise ValueError("GITHUB_REPO_NAME environment variable is not set.")

    # Iterate through all files in the specified directory
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.endswith(".ipynb"):
                # Construct the relative path to the notebook file
                relative_path = os.path.relpath(os.path.join(root, notebook_path, file), start=file_path)
                relative_path = relative_path.replace(os.sep, "/")
                encoded_relative_path = quote(relative_path, safe="/")
                # Create the full Colab URL
                colab_url = f"{colab_base_url}{github_username}/{github_repo_name}/blob/main/{encoded_relative_path}"
                colab_urls.append(colab_url)

    return colab_urls

if __name__ == "__main__":
    # Example usage
    directory_path = "Lectures/" 
    urls = generate_colab_urls(directory_path)
    for url in urls:
        print(url)