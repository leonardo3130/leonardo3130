import requests
import re

FACT_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random"
README_PATH = "README.md"

def fetch_fact():
    try:
        response = requests.get(FACT_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("text", "No fact available today.")
    except Exception as e:
        print("Error fetching fact:", e)
        return "Could not fetch a fact today. :("

def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    new_readme = re.sub(
        r"(<!--COOL_FACT-->)([\s\S]*?)(<!--COOL_FACT-->)",
        rf"\1{fetch_fact()}\3",
        readme,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)

if __name__ == "__main__":
    update_readme()
