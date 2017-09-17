# -*- coding: utf-8 *-
"""
Created on Sat 08/26/2017

@Author: Junichi Suetsugu (末次 淳一)
"""

def selection_request(message={"Enter": "Next"}, prompt=">>> "):
    """選択メッセージを表示します
    """
    selection_request_message = []
    message = message.items()
    for i in message:
        selection_request_message.append(i[0])
        selection_request_message.append(":")
        selection_request_message.append(i[1])
        selection_request_message.append(" ")
    selection_request_message.pop()
    print("".join(selection_request_message))
    select = input(prompt)
    return select
