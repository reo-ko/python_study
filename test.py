#print
print("=========== 問1 ===========\n")

print('こんにちは！')

#四則演算 5,5
print("=========== 問2 ===========\n")
print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)

#if文（xが5以上だったら”5以上です”を表示5未満だったら"5未満ですを表示させる"）
print("=========== 問3 ===========\n")
x = 4

if x < 5:
    print('5以上です')
elif x < 5:
    print('5未満です')
elif x == 5:
    print('5です')

#for文（0から10を合計した数を出力）
print("=========== 問4 ===========\n")
total = 0
for i in range(10):#10まで　0-9まで
    total += i
print(total)



# for文とif文 0~30で奇数だったら”奇数”、偶数の場合は”偶数”を出力
print("=========== 問5 ===========")
for i in range(10,31):
    if i % 2 == 1:#奇数だったら
        print('奇数です')
    elif i % 2 == 0:
        print('偶数です')

#リスト for,if, 0~50で割り切れる数をリストに追加
print("=========== 問6 ===========\n")
x_list = []
y_list = []

for i in range(51):
    if i % 5 == 0:
        x_list.append(i)#x_listにiを追加する
    else:#5で割りきれない
        y_list.append(i)#x_listにiを追加する

print(x_list)
print(y_list)

#x_listの中で10で割り切れるのをz_listに追加
print("=========== 問7 ===========\n")
z_list = []

for i in x_list:
    if i % 10 == 0:
        z_list.append(i)
print(z_list)

#文字列フォーマット
x = 0
print(f'こんにちは{x}')
print('こんにちは'.format(x))


#辞書
print("=========== 問8 ===========\n")

y_dic = {'国語':80,'数学':60,'理科':90,}
#国語は80点です。
for x , y in y_dic.items():
    print(f'{x}は{y}点です。')