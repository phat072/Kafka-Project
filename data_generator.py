from datetime import datetime
import random
import pandas as pd
import time

def main():
    data = {}
    free_text = []
    label_id = []

    for _ in range(1000):
        free_text.append(random.randint(10, 40))
        time.sleep(1)
        label_id.append(str(datetime.now()))

    data["free_text"] = free_text
    data["label_id"] = label_id

    df = pd.DataFrame(data)

    df.to_csv("./data/room_1/test.csv", sep=",", index=False)


if __name__ == "__main__":
    main()