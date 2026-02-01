export CUDA_VISIBLE_DEVICES=0
python -m vllm.entrypoints.openai.api_server\
  --model /HOME/airecruitas_qding/airecruitas_qding_2/HDD_POOL/dino/ds_dis/Qwen2.5-1.5B-Instruct-dis_sft \
  --dtype bfloat16 \
  --api-key token-abc123\
  --port 6666 \
  --trust-remote-code \
  --gpu-memory-utilization 0.9 \
  --served-model-name Qwen2.5-1.5B-dis_sft\
  --max_model_len 2048
