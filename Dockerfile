# If all you need is Python 3, use:
FROM cicirello/pyaction-lite:3

# If you need Python 3 and the GitHub CLI, then use:
# FROM cicirello/pyaction:4

# If Python 3 + git is sufficient, then use:
# FROM cicirello/pyaction:3

# To pull from the GitHub Container Registry instead, use one of these:
# FROM ghcr.io/cicirello/pyaction-lite:3
# FROM ghcr.io/cicirello/pyaction:4
# FROM ghcr.io/cicirello/pyaction:3
run python3 -m ensurepip --default-pip
RUN python3 -m pip install requests

COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]
