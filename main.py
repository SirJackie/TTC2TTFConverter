from fontTools.ttLib import TTCollection, TTFont


def ttc_to_ttf(ttc_file, ttf_file):
    # 打开TTC文件
    ttc = TTCollection(ttc_file)

    # 获取TTC中的第一个字体
    ttf = ttc.fonts[10]  # Source Han Sans Normal

    # 保存为TTF文件
    ttf.save(ttf_file)

    print("Conversion completed successfully!")


if __name__ == "__main__":
    ttc_file = "SourceHanSans.ttc"  # 输入的TTC文件名
    ttf_file = "SourceHanSans_Normal.ttf"  # 输出的TTF文件名
    ttc_to_ttf(ttc_file, ttf_file)
