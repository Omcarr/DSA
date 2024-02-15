
file_path='D:\Omkar\Downloads\SPJIMR\\birlsoft.txt'
with open(file_path, 'r') as file:
        file_content = file.read()
text = file_content

from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax
import torch

def get_semantic_analysis_bert(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
    inputs = tokenizer(text, return_tensors='pt', truncation=True)
    logits = model(**inputs).logits
    probabilities = softmax(logits, dim=1)
    activity, optimism, certainty, commonality, realism = probabilities[0]

    return activity.item(), optimism.item(), certainty.item(), commonality.item(), realism.item()


activity, optimism, certainty, commonality, realism = get_semantic_analysis_bert(text)

print(f"ACTIVITY: {activity}, OPTIMISM: {optimism}, CERTAINTY: {certainty}, COMMONALITY: {commonality}, REALISM: {realism}")
