
import uuid

def auto_create_brand_info():##生成品牌信息的函数，返回一个字典

    timestamp = str(uuid.uuid4()).replace('-','')[:8]
    auto_name = f'auto_name_{timestamp}'
    auto_firstLetter = auto_name[0]

    auto_info = {
    "name": auto_name,
    "firstLetter": auto_firstLetter,
    "sort": 0,
    "factoryStatus": 0,
    "showStatus": 0,
    "logo": "string",
    "bigPic": "string",
    "brandStory": "string"
    }
    return auto_info