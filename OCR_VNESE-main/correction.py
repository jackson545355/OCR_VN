import os
import re

inputDir = 'new_output'
resultDir = 'result'
path = os.listdir(inputDir)

dict = {'ơ̆': 'ố', 'ŏ': 'ồ', '_': '', 'ŭ': 'ủ', '-=': '', 'nầy': 'này', 'ĭ': 'i', 'ă': 'a','xuốất':'xuất','ẪẴ':''}


def correct(sentence):
    regex = r'[(,.\\!““]?\b\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]*\S*\b[,.\\!”;”)]?'
    return re.findall(regex, sentence)
def removeConsecutiveDuplicates(s):
    if len(s) < 2:
        return s
    if s[0] != s[1]:
        return s[0]+removeConsecutiveDuplicates(s[1:])
    return removeConsecutiveDuplicates(s[1:])


def allCharactersSame(s):
    n = len(s)
    for i in range(1, n):
        if s[i] != s[0]:
            return False

    return True
for txt in path:
    txtFile = open(inputDir + '/' + txt, encoding='utf-8', errors='ignore').read()
    for original, replace in dict.items():
        txtFile = txtFile.replace(original, replace)
    LineList = txtFile.split('\n')
    # LineList = [x for x in LineList if len(x) > 1]
    proper_noun = []
    for sentence in LineList:
        if (allCharactersSame(sentence) or len(sentence) ==0):
            continue
        correctLine = correct(sentence)
        correctLine = [removeConsecutiveDuplicates(x) for x in correctLine]
        proper_noun.append(correctLine)
    sentences = []
    for line in proper_noun:
        in_viet_dict = True
        for word in line:
            if len(word)>7:
                in_viet_dict=False
        if in_viet_dict:
            sentence = ' '.join(line)
            sentences.append(sentence)
    txtFile = '\n'.join(sentences)

    with open(resultDir + '/' + txt, 'w', encoding='utf-8') as f:
        f.write(txtFile)
