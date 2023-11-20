
##文本分類
# 導入gradio
#import gradio as gr
# 導入transformers相關包
#from transformers import *
# 通過Interface加载pipeline並啟動文本分類服務
#gr.Interface.from_pipeline(pipeline("text-classification", model="uer/roberta-base-finetuned-dianping-chinese")).launch()


##閱讀理解
# 導入gradio
import gradio as gr
# 導入transformers相關包
from transformers import *
# 通過Interface加载pipeline並啟動閱讀理解服務
gr.Interface.from_pipeline(pipeline("question-answering", model="uer/roberta-base-chinese-extractive-qa")).launch()