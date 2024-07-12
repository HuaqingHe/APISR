import cv2

def get_video_frame_rate(video_path):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    
    # 获取视频的帧率
    frame_rate = video.get(cv2.CAP_PROP_FPS)
    
    # 打印帧率
    print(f"Video Frame Rate: {frame_rate} FPS")
    
    # 释放视频文件
    video.release()

# 调用函数，替换'your_video.mp4'为你的视频文件路径
get_video_frame_rate('/root/cloud/cephfs-group-hdvideo_group/Datasets/Game_training/raw_videos/xm14u_fight_5v5.MP4')
get_video_frame_rate('/root/cloud/cephfs-group-hdvideo_group/Datasets/Game_training/raw_videos/iP15pro_fight_rank.MP4')
