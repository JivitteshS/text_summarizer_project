import setuptools


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME="End-to-end-Text_summarization"
AUTHOR_USRE_NAME="jivittesh"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="jivittesh@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USRE_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP APP",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USRE_NAME}/{REPO_NAME}",
    long_description_content_type="text/markdown",
   project_urls={
       "Bug Tracker":f"https://github.com/{AUTHOR_USRE_NAME}/{REPO_NAME}"

   },
   package_dir={"":"src"},
   packages=setuptools.find_packages(where="src"),
)