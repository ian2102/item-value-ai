import requests
import time
import json


# Convert messages to number of dbs using llms
def message_to_c_llm(message):
    prompt = f"""
What are the number of dbs for each item?

Respond in valid JSON only.
End your JSON with ###END###.
Format example:
{{"[X]": (number of dbs for X)}}###END###
Make an entry for each item in the message, where an item is in [].

If the item/items is not priced with dbs, respond with:
{{"result": "Fail"}}###END###

Message:
{message}

Answer:
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

    #print(f"Time taken: {end_time - start_time:.3f} seconds")

    json_string = result["content"].split("\n")[-1] # get last line

    try:
        data = json.loads(json_string)
        if data.get("result") == "Fail":
            return {}
        else:
            return data
    except json.JSONDecodeError:
        return {}


if __name__ == "__main__":
    m = "[Q]6dbs"
    print(m)
    print(message_to_c_llm(m))

    m = "[C]4dbs"
    print(m)
    print(message_to_c_llm(m))

    m = "[V][B]3 db each"
    print(m)
    print(message_to_c_llm(m))

    m = "[J]pls give me free loot"
    print(m)
    print(message_to_c_llm(m))

    m = "[T][M]4db / 2db / 1db"
    print(m)
    print(message_to_c_llm(m))

    m = "[T]"
    print(m)
    print(message_to_c_llm(m))
