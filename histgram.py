from pathlib import Path
import math
import openpyxl
from matplotlib import pyplot

jp_font = "Yu Gothic" # 日本語フォント
pyplot.style.use("seaborn") # グラフスタイル

# エクセルファイルの読み込み
def xl_read(xl_path, cell_range, col_idx):
    lst = []
    wb = openpyxl.load_workbook(xl_path)
    ws = wb["Sheet1"]

    for r in ws[cell_range]:
        lst.append(r[col_idx].value)

    return lst


# ヒストグラム作成（売上）
def draw_hist_sales(sales_list, bin_edges):
    pyplot.hist(sales_list, bins=bin_edges, edgecolor="black", linewidth=1.0)
    pyplot.xlabel("TA発言数", fontname = jp_font)
    pyplot.ylabel("度数", fontname = jp_font)


# データ読み込み
file_path = Path("naist2021pro.xlsx")
data_list = xl_read(file_path, "D2:D84", 0)

# 最大値、最小値、個数の出力
data_max, data_min, data_n = max(data_list), min(data_list), len(data_list)
print("最大値：", data_max)
print("最小値：", data_min)
print("個数：", data_n)
print()

# 範囲、スタージェス
# print("範囲：", data_max - data_min)
print("スタージェス：", 1 + math.log2(data_n))
print()

# 階級の入力
bin_min = int(input("階級の下限値＝"))
bin_max = int(input("階級の上限値＝"))
bin_w = int(input("階級の幅＝"))

# ヒストグラム作成
edges = range(bin_min, bin_max + bin_w, bin_w)
draw_hist_sales(data_list, edges)

# ヒストグラム出力
pyplot.show()