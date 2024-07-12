# GRL
CUDA_VISIBLE_DEVICES=7 python test_code/inference.py --input_dir /simple_ssd/HuaqingHe/AnimeSR/inputs/test0704  --weight_path /simple_ssd/HuaqingHe/APISR/pretrained/4x_APISR_GRL_GAN_generator.pth --store_dir /simple_ssd/HuaqingHe/APISR/results
# DAT
CUDA_VISIBLE_DEVICES=7 python test_code/inference.py --input_dir /simple_ssd/HuaqingHe/AnimeSR/inputs/test0704 --model DAT --weight_path /simple_ssd/HuaqingHe/APISR/pretrained/4x_APISR_DAT_GAN_generator.pth --store_dir /simple_ssd/HuaqingHe/APISR/results
# RRDB
CUDA_VISIBLE_DEVICES=7 python test_code/inference.py --input_dir /simple_ssd/HuaqingHe/AnimeSR/inputs/test0704 --model RRDB --weight_path /simple_ssd/HuaqingHe/APISR/pretrained/4x_APISR_RRDB_GAN_generator.pth --store_dir /simple_ssd/HuaqingHe/APISR/results
