import  re


def parse(text):
    text = re.sub(r'[^\w ]', '', text)
    # 将所有的大写变为小写
    text = text.lower()
    # 生成单词列表
    word_list = text.split(' ')
    # 去除空白的单词
    word_list = filter(None, word_list)
    # 合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；

    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1

    word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return  word_dict

with open('in.txt','r') as fin:
    text=fin.read()

word_dict=parse(text)

with open('out.txt','w') as out:
    for word,frenquce in word_dict:
        out.write('{}:{}\n'.format(word,frenquce))


import json
params = {
'symbol': '123456',
'type': 'limit',
'price': 123.4,
'amount': 23
}
params_str = json.dumps(params)

print(type(params_str))

original_params = json.loads(params_str)
print(type(original_params))