export CUDA_VISIBLE_DEVICES=0
python -m vllm.entrypoints.openai.api_server\
  --model /HOME/airecruitas_qding/airecruitas_qding_2/HDD_POOL/dino/ds_dis/Qwen2.5-1.5B-Instruct \
  --dtype bfloat16 \
  --api-key token-abc123\
  --port 6666 \
  --trust-remote-code \
  --gpu-memory-utilization 0.95 \
  --served-model-name Qwen2.5-1.5B\
  --max_model_len 2048 \
  --enable-lora \
  --lora-modules '{"name": "lora", "path": "/HOME/airecruitas_qding/airecruitas_qding_2/HDD_POOL/dino/ds_dis/base_sft/checkpoint-8576"}'
  # --chat-template "{{ (messages|selectattr('role', 'equalto', 'system')|list|last).content|trim if (messages|selectattr('role', 'equalto', 'system')|list) else '' }}\n{%- for message in messages -%}\n    {%- if message['role'] == 'user' -%}\n        {{- '<reserved_106>' + message['content'] -}}\n    {%- elif message['role'] == 'assistant' -%}\n        {{- '<reserved_107>' + message['content'] -}}\n    {%- endif -%}\n{%- endfor -%}\n\n{%- if add_generation_prompt and messages[-1]['role'] != 'assistant' -%}\n    {{- '<reserved_107>' -}}\n{% endif %}"
