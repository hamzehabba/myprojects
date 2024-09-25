# import numpy as np
# from scipy.integrate import odeint
# import matplotlib.pyplot as plt
#
# # تعریف ماتریس A
# A = np.array([
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, -1],
#     [1, 1, 1, -2, 0],
#     [1, 1, -3, 0, 0],
#     [1, -(5-1), 0, 0, 0]
# ])
#
# # بردار اولیه
# x0 = np.array([1, 0, 0, 0, 0])
#
# # تابعی که دستگاه دیفرانسیلی را تعریف می‌کند
# def system(x, t):
#     return A.dot(x)
#
# # بازه زمانی
# t = np.linspace(0, 10, 100)
#
# # حل دستگاه
# x_t = odeint(system, x0, t)
#
# # رسم نتایج
# plt.figure(figsize=(10, 6))
# for i in range(x_t.shape[1]):
#     plt.plot(t, x_t[:, i], label=f'x{i+1}(t)')
# plt.xlabel('Time')
# plt.ylabel('x(t)')
# plt.legend()
# plt.title('Solution of the Dynamical System')
# plt.grid(True)
# plt.show()



first_list=[]
def append_if_in_range(count, sum3,first_list):
    first_list.append(count)
    if len(first_list) > 100:
        first_list.pop(0)
    if first_list[-1]== 0:
        count= first_list[-2]

        # اگر لیست خالی نیست و count بزرگتر از آخرین عنصر لیست است
        if len(sum3) > 0 and count > max(sum3):
            sum3.clear()  # اگر count بزرگ‌تر بود، لیست را خالی کن
            # اگر لیست خالی نیست و count کوچکتر از کوچکترین عنصر لیست است
        elif len(sum3) > 0 and count < min(sum3):
            sum3.clear()  # اگر count کوچکتر بود، لیست را خالی کن
        sum3.append(count)  # سپس count را به لیست اضافه کن

    # بررسی تعداد تکرارها در sum3
    if len (sum3) == 3:
        return sum3  # اگر عددی 3 بار تکرار شد، لیست را برگردان



# مثال از استفاده:
sum3_list = []
first_list=[]

print(append_if_in_range(6, sum3_list,first_list))  # عدد 6 اضافه می‌شود
print(append_if_in_range(7, sum3_list,first_list))  # عدد 7 بزرگتر از 6 است، پس 6 پاک و 7 اضافه می‌شود
print(append_if_in_range(5, sum3_list,first_list))  # عدد 5 کوچکتر از 7 است، پس 7 پاک و 5 اضافه می‌شود
print(append_if_in_range(5, sum3_list,first_list))  # دوباره 5 اضافه می‌شود
print(append_if_in_range(5, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(0, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود

print(append_if_in_range(3, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(0, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(3, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(0, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(3, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(0, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(2, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(0, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(2, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(0, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(2, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
print(append_if_in_range(0, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود

# print(append_if_in_range(3, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
# print(append_if_in_range(0, sum3_list,first_list))  # سومین بار 5 اضافه می‌شود و لیست برگردانده می‌شود
# print(append_if_in_range(5, sum3_list,first_list))  # دوباره 5 اضافه می‌شود

