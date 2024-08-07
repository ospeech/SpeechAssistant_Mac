import SparkApi
#以下密钥信息从控制台获取
appid = ""     #填写控制台中获取的 APPID 信息
api_secret = ""   #填写控制台中获取的 APISecret 信息
api_key =""    #填写控制台中获取的 APIKey 信息
 
domain = "general"   # v3版本
#云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v3环境的地址（"wss://spark-api.xf-yun.com/v3.1/chat）
 
 
text =[]
 
# length = 0
 
def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text
 
def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length
 
def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
    
def get_answer(Input):
    question = checklen(getText("user",Input)) 
    SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
    return SparkApi.answer
 
if __name__ == '__main__':
    Input = "今天天气不错啊"
    print(get_answer(Input))
 

