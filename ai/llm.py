import requests
import time

def get_dbs(message):
    prompt1 = f"""
Extract the number of dbs.
End your output with ###END###
If no items have prices in dbs or you cannot parse correctly, output Fail###END###.
Otherwise output exactly one line per item in this format:
[Item] Output: <number of dbs for that item>

[a][b]4dbs/5dbs
[a] 4
[b] 5###END###

[a]1db
[1] Output: 1###END###

[a][b]1db each
[a] 1
[b] 1###END###

[a]
Fail###END###

[a]pls give me free stuff
Fail###END###

Message: {message}
"""
    prompt = f"""
You are a strict parser for item db counts. Follow these rules exactly:

1. Only consider numeric values immediately followed by "db" or "dbs".  
2. Ignore all other numbers, words, URLs, or offers.  
3. For each item ([a], [b], [c], etc.), output exactly one line in this format:
[Item] Output: <number of dbs>
4. If an item is listed but no valid db number exists, output nothing for it.
5. If no items have valid db numbers, output exactly:
Fail###END###
6. End your output with ###END###.

Examples:

[a][b]4dbs/5dbs
[a] Output: 4
[b] Output: 5
###END###

[a]1db
[a] Output: 1
###END###

[a][b]1db each
[a] Output: 1
[b] Output: 1
###END###

[a]
Fail###END###

[a]pls give me free stuff
Fail###END###

[a]61+2 wts 2db+2full or offer
[a] Output: 2
###END###

[a][b][c]4db / 2db / 1db
[a] Output: 4
[b] Output: 2
[c] Output: 1
###END###

[a]ZIKRON ICE GET FRESH
Fail###END###

Message: {message}
"""

    start_time = time.time()

    response = requests.post(
        "http://localhost:8080/completion",
        json={
            "prompt": prompt,
            "n_predict": 64,
            "temperature": 0.0,
            "stop": ["###END###"]
        }
    )

    end_time = time.time()

    result = response.json()

    print(f"Time taken: {end_time - start_time:.3f} seconds")
    return result["content"]


if __name__ == "__main__":
    get_dbs("[RecurveBow_8001]6dbs")