import requests,json
def chat(question):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    payload = {
        "model": "deepseek-ai/DeepSeek-V2-Chat",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer sk-owobgkyepmspqxgzwsygizsmziyljhaeygrueiriytnbpugd"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    data = json.loads(response.text)
    try:
        content_value = data['choices'][0]['message']['content']
    except KeyError:
        print(data)
    return content_value