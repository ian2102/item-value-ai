import requests
import time

def get_dbs(message):
    prompt = f"""
    Extract the number of dbs in the last message. 
    If none is listed, output 0.
    Output exactly one line per item in this format:
    [Item] Output: <number>
    End your output with ###END###

    Message: [a][b]4dbs/5dbs
    [a] Output: 4
    [b] Output: 5###END###

    Message: [a]1db
    [b] Output: 1###END###

    Message: [a][b]1db each
    [a] Output: 1
    [b] Output: 1###END###

    Message: [a]pls give me free stuff
    [a] Output: 0###END###

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