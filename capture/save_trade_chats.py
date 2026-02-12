from google.protobuf.json_format import MessageToJson
import time
import json

from capture import PacketCapture
from protos import _PacketCommand_pb2

pc = _PacketCommand_pb2.PacketCommand

def save(message):
    data = json.loads(
        MessageToJson(
            message,
            always_print_fields_with_no_presence=True,
            ensure_ascii=False
        )
    )

    with open("output.ndjson", "a", encoding="utf-8") as file:
        file.write(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")

def show(message):
    json_str = MessageToJson(
        message,
        always_print_fields_with_no_presence=True,
        ensure_ascii=False
    )
    print(json_str)

def main():
    capture_info = {
        pc.S2C_TRADE_CHANNEL_CHAT_RES: save,
    }

    capture = PacketCapture(capture_info)

    capture.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        capture.stop()

if __name__ == "__main__":
    main()
