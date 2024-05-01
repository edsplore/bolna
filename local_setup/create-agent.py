import requests

url = "http://0.0.0.0:5001/agent"

payload = {
    "agent_config": {
        "agent_name": "airbnb_job",
        "agent_type": "other",
        "tasks": [
            {
                "task_type": "conversation",
                "tools_config": {
                    "llm_agent": {
                        "streaming_model": "gpt-3.5-turbo-16k",
                        "classification_model": "gpt-4",
                        "max_tokens": 123,
                        "agent_flow_type": "streaming",
                        "use_fallback": True,
                        "family": "openai",
                        "temperature": 0.1,
                        "request_json": True
                    },
                    "synthesizer": {
                        "provider": "polly",
                        "provider_config": {
                            "voice": "Kajal",
                            "engine": "neural",
                            "sampling_rate": "8000",
                            "language": "en-US"
                        },
                        "stream": True,
                        "buffer_size": 123,
                        "audio_format": "pcm"
                    },
                    "transcriber": {
                        "model": "deepgram",
                        "language": "en",
                        "stream": True,
                        "sampling_rate": 123,
                        "encoding": "linear16",
                        "endpointing": 123
                    },
                    "input": {
                        "provider": "twilio",
                        "format": "pcm"
                    },
                    "output": {
                        "provider": "twilio",
                        "format": "pcm"
                    }
                },
                "toolchain": {
                    "execution": "parallel",
                    "pipelines": [["transcriber", "llm", "synthesizer"]]
                }
            }
        ]
    },
    "agent_prompts": {"task_1": {"system_prompt": "What is the Ultimate Question of Life, the Universe, and Everything?"}}
}
headers = {
    #"Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)