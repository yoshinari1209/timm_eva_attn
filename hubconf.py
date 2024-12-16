dependencies = ['torch']
import timm_attn
globals().update(timm_attn.models._registry._model_entrypoints)
