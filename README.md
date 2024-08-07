fork from:
https://github.com/csensor/GPT_Voice_Assistant
几点改进：
1. 修复recorder的bug（CHUNK=512）
2. 用星火大模型lite（永久免费）代替ChatGPT
# SpeechAssistant_Mac
基于星火大模型的智能交互语音助手,产品主要涉及四个任务：语音唤醒，语音识别，GPT对话，文本转语音

# 实现的功能
通过唤醒词唤醒后，进行语音对话

# 可玩性
可在mac笔记本上实现语音助手功能

# 安装方法
1. `pip install -r requirements.txt`

# 配置
按需修改配置
```
{
    "porcupine": {
        "access_key": "",                // porcupine的ak
        "keywords": [],                  // 可使用 porcupine 内置的唤醒词，否则使用keyword_paths
        "keyword_paths": ["ppn/hello-orange_en_mac_v3_0_0.ppn"], // 项目下自带了唤醒词模型，在resource/ppn 目录下可供选择
        "sensitivities": [0.5]           // 唤醒词阈值，值越高precision越高，反之recall越高
    },
    "nlp_service": {
        "paddlepaddle": {               
            "asr_url": "http://x.x.x.x:8090/paddlespeech/asr",  // 自己搭建的paddlespeech的asr服务, x 换成ip地址
            "tts_url": "http://x.x.x.x:8090/paddlespeech/tts"   // 自己搭建的paddlespeech的tts服务, x 换成ip地址
        }
    },
}
```

# 运行方法
1. `python3 gva_main.py`

# 常见问题
> 如何生成自己的唤醒词？

见 https://console.picovoice.ai/

> 如何搭建paddlespeech 服务

见 https://github.com/PaddlePaddle/PaddleSpeech
