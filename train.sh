sdf train create hehq-job0 --worker 1 --image lab/all_in_one:cl4_dreambooth_xformers_cuda11.3_cuda11.7_sdwebui --cmd 'cd /root/picasso/HuaqingHe/ && bash sleep.sh' --cpu 10 --mem 60 --gpu 1 --gputype 3090 --priority high
scp -P 30859 -r root@10.255.0.125:/opt/conda/envs/AnimeSR /opt/conda/envs

# 步骤1（网络L1损失训练）：
CUDA_VISIBLE_DEVICES=7 python train_code/train.py #--opt options/train/train_APISR_GRL_GAN.yml
# 
# 步骤2（GAN对抗训练）：