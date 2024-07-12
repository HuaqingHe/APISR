import os, cv2, shutil, argparse
import math

if __name__ == "__main__":

    # Parse variables available
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', type = str)
    parser.add_argument('-o', '--store_dir', type = str)
    args  = parser.parse_args()

    input_dir = args.input_dir
    store_dir = args.store_dir

    print("We are doing the 720p Resize check!")

    # File Check
    if os.path.exists(store_dir):
        shutil.rmtree(store_dir)
    os.makedirs(store_dir)

    scale = 4
    num = 0
    for file_name in sorted(os.listdir(input_dir)):
        source_path = os.path.join(input_dir, file_name)
        destination_path = os.path.join(store_dir, file_name)
        img = cv2.imread(source_path)
        h,w,c = img.shape

        if h == 720:
            # It is already 720P so we directly move them
            shutil.copy(source_path, destination_path)
            continue
        elif h < 720:
            print("It is weird that there is an image with height less than 720 ", file_name)
            continue
        
        # # Else, here we need to resize them (All resize to 720P)
        # both resize and crop
        new_w = int(w*(720/h))
        img_bicubic = cv2.resize(img, (new_w, 720), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(store_dir, file_name), img_bicubic, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        
        # I don't want to resize the image, but crop the image to 720P
        # calculate the number of crops blocks
        num_blocks_w = math.ceil(w / 720)
        num_blocks_h = math.ceil(h / 720)
        block_count = 0
        for i in range(num_blocks_h):
            for j in range(num_blocks_w):
                # 计算每个图块的坐标
                x_start = j * 720
                y_start = i * 720
                if x_start + 720 > w:
                    x_start = w - 720
                    x_end = w
                else:
                    x_end = x_start + 720
                if y_start + 720 > h:
                    y_start = h - 720
                    y_end = h
                else:
                    y_end = y_start + 720
                
                # 分割图片
                img_block = img[y_start:y_end, x_start:x_end]
                
                # 保存图块
                block_file_name = file_name.split('.')[0] + f"_{block_count}.png"
                cv2.imwrite(os.path.join(store_dir, block_file_name), img_block)
                block_count += 1
                num += 1

    print("The total resize num is ", num)