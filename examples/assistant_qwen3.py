"""An agent implemented by assistant with qwen3"""
import os  # noqa
import requests

from qwen_agent.agents import Assistant
from qwen_agent.gui import WebUI
from qwen_agent.utils.output_beautify import typewriter_print


def fetch_lmstudio_models():
    """Fetch available models from LM Studio's /v1/models endpoint."""
    try:
        resp = requests.get('http://localhost:1234/v1/models', timeout=5)
        resp.raise_for_status()
        data = resp.json()
        # LM Studio returns {"object": "list", "data": [{"id": ...}, ...]}
        return [m["id"] for m in data.get("data", [])]
    except Exception as e:
        print(f"Failed to fetch models from LM Studio: {e}")
        # Fallback to a default list
        return [
            'qwen3-0.6b@q8_0',
            'qwen3-1.7b@q8_0',
            'qwen3-7b',
            'qwen3-14b',
            'qwen3-72b',
        ]


def init_agent_service(selected_model=None):
    models = fetch_lmstudio_models()
    model_to_use = selected_model or models[0]
    llm_cfg = {
        'model': model_to_use,
        'model_server': 'http://localhost:1234/v1',
        'api_key': 'EMPTY',
        'generate_cfg': {
            'extra_body': {
                'chat_template_kwargs': {'enable_thinking': False}
            },
        },
    }
    tools = [
        {
            'mcpServers': {
                'time': {
                    'command': 'uvx',
                    'args': ['mcp-server-time', '--local-timezone=America/New_York']
                },
                'fetch': {
                    'command': 'uvx',
                    'args': ['mcp-server-fetch', '--ignore-robots-txt']
                },
                "context7": {
                 "command": "npx",
                 "args": ["-y", "@upstash/context7-mcp"]
               }
            }
        },
        'code_interpreter',
    ]
    bot = Assistant(llm=llm_cfg,
                    function_list=tools,
                    name='Qwen3 Tool-calling Demo',
                    description="I'm a demo using the Qwen3 tool calling. Welcome to add and play with your own tools!")
    return bot, models


def test(query: str = 'What time is it?'):
    # Define the agent
    bot = init_agent_service()

    # Chat
    messages = [{'role': 'user', 'content': query}]
    response_plain_text = ''
    for response in bot.run(messages=messages):
        response_plain_text = typewriter_print(response, response_plain_text)


def app_tui():
    # Define the agent
    bot = init_agent_service()

    # Chat
    messages = []
    while True:
        query = input('user question: ')
        messages.append({'role': 'user', 'content': query})
        response = []
        response_plain_text = ''
        for response in bot.run(messages=messages):
            response_plain_text = typewriter_print(response, response_plain_text)
        messages.extend(response)


def app_gui():
    # On startup, fetch models and set default
    bot, models = init_agent_service()
    chatbot_config = {
        'prompt.suggestions': [
            'What time is it?',
            'https://github.com/orgs/QwenLM/repositories Extract markdown content of this page, then draw a bar chart to display the number of stars.'
        ],
        'available_models': models,
        'selected_model': models[0],
    }
    from qwen_agent.gui.web_ui import WebUI
    import gradio as gr

    class WebUIWithSettings(WebUI):
        def run(self, *args, **kwargs):
            from qwen_agent.gui.gradio_dep import gr
            models = chatbot_config['available_models']
            selected_model = chatbot_config['selected_model']
            with gr.Blocks() as demo:
                with gr.Tab("Chat"):
                    super().run(*args, **kwargs)
                with gr.Tab("Settings"):
                    with gr.Row():
                        model_dropdown = gr.Dropdown(
                            choices=models,
                            value=selected_model,
                            label="Select Model",
                            interactive=True,
                        )
                        save_btn = gr.Button("Save Model")
                        status = gr.Markdown(visible=False)

                    def save_model(selected):
                        chatbot_config['selected_model'] = selected
                        nonlocal bot
                        bot, _ = init_agent_service(selected_model=selected)
                        status_text = f"Model changed to: {selected}"
                        return status_text

                    save_btn.click(
                        fn=save_model,
                        inputs=[model_dropdown],
                        outputs=[status],
                    )
            demo.launch()

    WebUIWithSettings(
        bot,
        chatbot_config=chatbot_config,
    ).run()


if __name__ == '__main__':
    # test()
    # app_tui()
    app_gui()
