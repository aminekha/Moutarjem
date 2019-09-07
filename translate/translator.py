"""
This file will translate any text from english to french
"""
import torch
import fairseq

def fairseq_translation(text_to_translate):
    # List available models
    torch.hub.list('pytorch/fairseq')  # [..., 'transformer.wmt16.en-de', ... ]

    # Load a transformer trained on WMT'16 En-De
    en2de = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.de-en', checkpoint_file='model1.pt:model2.pt:model3.pt:model4.pt',
                       tokenizer='moses', bpe='fastbpe')

    # The underlying model is available under the *models* attribute
    assert isinstance(en2de.models[0], fairseq.models.transformer.TransformerModel)

    # Translate a sentence
    # text_to_translate = "artificial intelligence is the new electricity."
    # text = input("> ")
    print("\nTranslating: {}".format(text_to_translate))
    output = en2de.translate(text_to_translate)
    return output
