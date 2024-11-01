from datasets import load_dataset
from transformers import TextClassificationPipeline, BertForSequenceClassification, AutoTokenizer

# 모델 및 파이프라인 로드
dataset = load_dataset('smilegate-ai/kor_unsmile')
model_name = 'smilegate-ai/kor_unsmile'
model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

pipe = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    device=-1,
    top_k=None,
    function_to_apply='sigmoid'
)

# 혐오 표현 유형별 이모티콘 매핑
changeimti = {
    '여성/가족': '^^',
    '남성': '>.<',
    '성소수자': 'ㅇ.ㅇ',
    '인종/국적': '뀨',
    '연령': '@.@',
    '지역': '3.3',
    '종교': '뀨뀨',
    '기타 혐오': '뀨뀨뀨',
    '악플/욕설': '(ㅐ.ㅐ)'
}

def filter_hate_speech(user_input):
    # 모델 예측
    predictions = pipe(user_input)
    result = predictions[0]

    # 디버깅용: 예측 결과와 스코어 출력
    print("Predictions:", result)

    # 가장 높은 스코어를 가진 레이블과 해당 스코어 확인
    max_score_label = max(result, key=lambda x: x['score'])
    keytype = max_score_label['label']
    max_score = max_score_label['score']

    # 스코어가 0.5 이상인 경우 이모티콘으로 변환
    if max_score >= 0.5 and keytype in changeimti:
        response_value = changeimti[keytype]
    else:
        response_value = user_input  # 스코어가 낮으면 원래 입력 반환

    return response_value

# 터미널에서 사용자 입력 받기
if __name__ == "__main__":
    user_input = input("문장을 입력하세요: ")
    response = filter_hate_speech(user_input)
    print("변환 결과:", response)

