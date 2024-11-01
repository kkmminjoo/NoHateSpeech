
from django.http import HttpResponse
from django.shortcuts import render
from datasets import load_dataset
import torch
from transformers import TextClassificationPipeline, BertForSequenceClassification, AutoTokenizer

dataset = load_dataset('smilegate-ai/kor_unsmile')

model_name = 'smilegate-ai/kor_unsmile'

model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

pipe = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    device=-1,
    return_all_scores=True,
    function_to_apply='sigmoid'
)

changeimti = {
    '여성/가족': '^^',
    '남성': '>.<',
    '성소수자': '💩💩💩💩💩',
    '인종/국적': '뀨',
    '연령': '🍕🍔🍟🌭🍿',
    '지역': '3.3',
    '종교': '💐🌹🌺🌻🌼🌷',
    '기타 혐오': '(H.H)',
    '악플/욕설': '❤️🩷💛💚💙'
}

