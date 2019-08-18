"""
This file will translate any text from english to french
"""
import torch
# import fairseq

# List available models
torch.hub.list('pytorch/fairseq')  # [..., 'transformer.wmt16.en-de', ... ]

# Load a transformer trained on WMT'16 En-De
en2de = torch.hub.load('pytorch/fairseq', 'transformer.wmt14.en-fr', tokenizer='moses', bpe='subword_nmt')

# The underlying model is available under the *models* attribute
assert isinstance(en2de.models[0], fairseq.models.transformer.TransformerModel)

# Translate a sentence
text_to_translate = "Dear Vneuron, My name is Amine Khaoui. I am incredibly passionate about all things technology, artificial intelligence, and data. Over the past 2 years, I have dedicated a considerable amount of time and effort to master machine learning algorithms, It amazed me and I have been dedicating my education to that ever since. "
output = en2de.translate("hello, world")
print(output)