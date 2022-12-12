import pandas as pd
import json
from itertools import chain
from underthesea import word_tokenize
import re

BOT_MEMORY = {'keywords': [], 'action': None}

def preprocessing(text):
    text = text.lower().replace('thủ tục','')
    text = re.sub(' +', ' ',text)
    text = re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_\.\,]',' ',text)
    return text


def remove_dup(result_list):
    tmp_list = list(dict.fromkeys(result_list))
    # tmp_list = sorted(tmp_list, key=len)
    return tmp_list


def bot_understand(user_question: str):
    global BOT_MEMORY
    keyword_list = []
    # load keyword dictionary
    with open('../json_data/keyword.json', 'r', encoding='utf-8') as f:
        keyword_dict = json.load(f)
    for key in keyword_dict.keys():
        for val in keyword_dict[key]:
            if val in user_question:
                keyword_list.append(key)
                user_question = user_question.replace(val, '')
    BOT_MEMORY.update({'keywords': keyword_list})
    return BOT_MEMORY

# print(bot_understand('Tối muốn đăng ký kết hôn với người nước ngoài'))


def search_token_in_database(user_token):
    df = pd.read_csv('../data/new_procedure.csv', engine='python')
    procedures = df[df.procedure_name.str.contains(user_token, na=False)]
    # flatten 2d list
    procedure_list = list(chain.from_iterable(procedures.values.tolist()))
    procedure_list = sorted(procedure_list, key=len)
    return procedure_list


def search_list_token_in_database(list_user_token: list):
    tmp_list = []
    for token in list_user_token:
        tmp_list += search_token_in_database(token)
    if len(list_user_token) == 2:
        df = pd.DataFrame({'procedure': tmp_list})

        df1 = pd.DataFrame(data=df['procedure'].value_counts())

        df1['Count'] = df1['procedure'].index

        mingg = list(df1[df1['procedure'] == 2]['Count'])

        return mingg
    elif len(list_user_token) == 3:
        df = pd.DataFrame({'procedure': tmp_list})

        df1 = pd.DataFrame(data=df['procedure'].value_counts())

        df1['Count'] = df1['procedure'].index

        mingg = list(df1[df1['procedure'] == 3]['Count'])

        return mingg


def bot_searching(user_question: str):
    user_question = preprocessing(user_question)
    BOT_MEMORY = bot_understand(user_question)
    result = []
    keywords = BOT_MEMORY['keywords']
    if keywords:
        keywords = remove_dup(keywords)

        # Trả cụm động từ : VP = V1 + V2
        VP = ' '.join(key for key in keywords)
        # print(VP)
        VP_procedure_list = search_token_in_database(VP)
        if VP_procedure_list:
            result += VP_procedure_list
        # Lấy duplicate
        if len(keywords) >= 2:
            DUP_procedure_list = search_list_token_in_database(keywords)
            if DUP_procedure_list:
                result += DUP_procedure_list
        print(keywords)
        if len(keywords) != 0:
            result += search_token_in_database(keywords[0])
        result = remove_dup(result)
        # Lấy K=5
        if result:
            return result[:5]
        else:
            return "Tôi chưa được học thủ tục này :("
    else:
        list_user_token = word_tokenize(user_question)
        tmp = []
        for token in list_user_token:
            tmp += search_token_in_database(token)
        df = pd.DataFrame({'procedure': tmp})
        df1 = pd.DataFrame(data=df['procedure'].value_counts())
        df1['Count'] = df1['procedure'].index
        result = list(df1[df1['procedure'] >= df1.procedure.max()-3]['Count'])
        if result:
            return result[:5]
        else:
            return "Tôi chưa được học thủ tục này :("
# print(bot_searching('tôi muốn đăng ký kết hôn với người nước ngoài'))
