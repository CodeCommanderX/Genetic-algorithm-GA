import copy
import random
import math

#khởi tạo quy mô quần thể
kichthuoc_quanthe = 8
# Danh sách cho quần thể bố mẹ
ds_bome = []
# Danh sách cho các quần thể con
ds_con = []
# hàm thích nghi của mỗi cá thể trong quần thể bố mẹ
ds_bome_fitness = []
# hàm thích nghi của mỗi cá thể trong quần thể con
ds_con_fitness = []


# Khởi tạo quần thể
def ktao_quanthe():
    # quần thể
    quanthe = []
    # mã hoá 
    for i in range(8):
        a = random.randint(0, 7)
        quanthe.append(a)
    # Tính cá thể của các con được tạo ra
    diem_thichnghi = capnhat_thichnghi(quanthe)
    # tham gia vào nhóm

    ds_bome_fitness.append(diem_thichnghi)
    ds_bome.append(quanthe)
    return


# cập nhật chức năng thích nghi
def capnhat_thichnghi(quanthe):
    value = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if quanthe[i] != quanthe[j]:
                x = j - i
                y = abs(quanthe[i] - quanthe[j])
                if x != y:
                    value += 1
    return value


#  Khởi tạo một quần thể, kích thước quần thể là kichthuoc_quanthe
def quanthe_bandau():
    for i in range(kichthuoc_quanthe):
        ktao_quanthe()
    return


# chọn cha mẹ
def chon_con():
    # Tổng thích nghi của tất cả các cá thể
    tong_diem_thichnghi = 0
    for fit in ds_bome_fitness:
        tong_diem_thichnghi += fit

    # số trong roulette
    num = random.randint(0, tong_diem_thichnghi)
    # Tổng của thích nghi trước đó
    front_score = 0
    for i in range(kichthuoc_quanthe):
        front_score += ds_bome_fitness[i]
        # Nếu tổng của lần thích nghi trước đó lớn hơn số ngẫu nhiên được tạo ra
        # Thì số đó phải rơi vào cá thể được đánh số i
        if front_score >= num:
            return i


# Đột biến
def dot_bien(thaydoi_quanthe):
    #  nếu bị đột biến gen
    gene = random.randint(0, 7)
    # giá trị đã thay đổi
    change = random.randint(0, 7)
    thaydoi_quanthe[gene] = change
    return thaydoi_quanthe


# lai tạo ra con cái
def laitao():
    # chọn hai cha mẹ
    thunhat = chon_con()
    thuhai = chon_con()
    chame_duocchon = copy.deepcopy([ds_bome[thunhat], ds_bome[thuhai]])
    # Hoán đổi gen từ gene1 sang gene2
    gene1 = random.randint(0, 6)
    gene2 = random.randint(0, 6)
    # chắc chắn gene1 <= gene2
    if gene1 > gene2:
        gene1, gene2 = gene2, gene1
    # lai chéo
    tmp = chame_duocchon[0][gene1:gene2]
    chame_duocchon[0][gene1:gene2] = chame_duocchon[1][gene1:gene2]
    chame_duocchon[1][gene1:gene2] = tmp
    # Một xác suất đột biến nhất định xảy ra, giả sử rằng xác suất đó là 0.5
    may = random.random()
    if may > 0.5:
        chame_duocchon[0] = dot_bien(chame_duocchon[0])
    may = random.random()
    if may > 0.5:
        chame_duocchon[1] = dot_bien(chame_duocchon[1])
    # cập nhật thích nghi
    thunhat_fit = capnhat_thichnghi(chame_duocchon[0])
    thuhai_fit = capnhat_thichnghi(chame_duocchon[1])

    # thêm vào con cái
    ds_con.append(chame_duocchon[0])
    ds_con.append(chame_duocchon[1])
    ds_con_fitness.append(thunhat_fit)
    ds_con_fitness.append(thuhai_fit)
    return


# Khởi tạo quần thể
quanthe_bandau()
# Tính số lần lặp lại
count = 0
# not a number
find = float('nan')
while True:
    count += 1
    if count % 1000 == 0:
        print('Số lần lặp lại : %d' % count)
    # Lai quần thể / 2 lần tạo ra con cái của quần thể
    for k in range(kichthuoc_quanthe // 2):
        laitao()
    # Nếu thích của một cá thể đạt 28, nghĩa là lúc này đã tìm ra giải pháp.
    for k in range(kichthuoc_quanthe):
        if ds_con_fitness[k] == 28:
            # ghi lại vị trí của giải pháp
            find = k
            break
    if not math.isnan(find):
        break
    # Đặt quần thể con vào quần thể bố mẹ làm cha mẹ mới và con bị xóa
    ds_bome[0:kichthuoc_quanthe] = ds_con[0:kichthuoc_quanthe]
    ds_bome_fitness[0:kichthuoc_quanthe] = ds_con_fitness[0:kichthuoc_quanthe]
    ds_con = []
    ds_con_fitness = []

# Lúc này, hãy tìm những cá thể con đáp ứng yêu cầu
cathe_dudk = ds_con[find]
print(cathe_dudk)

# Xây dựng bàn cờ
cathe_dudk_queen = [[0 for i in range(8)] for j in range(8)]
for t in range(8):
    cathe_dudk_queen[cathe_dudk[t]][t] = 1
# In bàn cờ
print("tìm kết quả ：")
for t in range(8):
    print(cathe_dudk_queen[t])


