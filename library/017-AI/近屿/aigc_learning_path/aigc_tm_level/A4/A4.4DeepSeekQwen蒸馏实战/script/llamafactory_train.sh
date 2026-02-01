CUDA=0
MODEL_NAME_OR_PATH="Qwen2.5-1.5B-Instruct"
DATASET_DIR="lf_data"
DATASET="dis_sft"
OUTPUT_DIR="${DATASET}"


SAVE_STEPS=2000  #200|1500
LEARNING_RATE=1e-05



export CUDA_VISIBLE_DEVICES=${CUDA}

nohup llamafactory-cli train \
    --stage sft \
    --do_train True \
    --model_name_or_path ${MODEL_NAME_OR_PATH} \
    --preprocessing_num_workers 16 \
    --finetuning_type lora \
    --template qwen \
    --flash_attn auto \
    --dataset_dir ${DATASET_DIR} \
    --dataset ${DATASET} \
    --cutoff_len 2048 \
    --learning_rate ${LEARNING_RATE} \
    --num_train_epochs 1 \
    --max_samples 100000 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 1 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 10 \
    --save_strategy epoch \
    --warmup_steps 0 \
    --optim adamw_torch \
    --packing False \
    --report_to none \
    --output_dir ${OUTPUT_DIR} \
    --bf16 True \
    --plot_loss True \
    --ddp_timeout 180000000 \
    --include_num_input_tokens_seen True \
    --lora_rank 8 \
    --lora_alpha 16 \
    --lora_dropout 0 \
    --lora_target all \
&


#/new_disk/models_for_all/Qwen2.5-7B-Instruct

# template qwen

    # --save_steps ${SAVE_STEPS} \
