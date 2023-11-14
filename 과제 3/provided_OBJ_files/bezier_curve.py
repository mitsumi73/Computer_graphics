import matplotlib.pyplot as plt
import numpy as np

P0 = [-5.0, -7.0]
P1 = [-3.0, 2.0]
P2 = [4.0, -1.0]
#P3 = [5.0, 7.0]

# Matplotlib에서 그림을 그리기 위한 초기 설정을 수행합니다.
fig, ax = plt.subplots()
ax.set_aspect('equal')

# x와 y 축의 위치 설정 및 스마트 바운드 기능 비활성화
# 이 오류는 Spine 객체에 대한 Matplotlib set_smart_bounds() 버전 때문에 발생합니다.
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
# ax.spines['bottom'].set_position('zero') 삭제
ax.spines['top'].set_color('none')
# ax.spines['left'].set_smart_bounds(True) 삭제
# ax.spines['bottom'].set_smart_bounds(True) 삭제
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

for i in range(-10, 10 + 1):
    if i != 0:
        ax.plot([-10, 10], [i, i], color='0.5')  # 수평선
        ax.plot([i, i], [-10, 10], color='0.5')  # 수직선

# 점 P0, P1, P2를 그래프에 표시합니다.
ax.scatter(P0[0], P0[1], s=50, color='g')
ax.scatter(P1[0], P1[1], s=50, color='g')
ax.scatter(P2[0], P2[1], s=50, color='g')
#ax.scatter(P3[0], P3[1], s=50, color='g') #추가

# 각 점의 좌표를 표시합니다.
ax.text(P0[0] + 0.2, P0[1], f'P0({P0[0]:.1f}, {P0[1]:.1f})')
ax.text(P1[0] + 0.2, P1[1], f'P1({P1[0]:.1f}, {P1[1]:.1f})')
ax.text(P2[0] + 0.2, P2[1], f'P2({P2[0]:.1f}, {P2[1]:.1f})')
#ax.text(P3[0] + 0.2, P3[1], f'P3({P3[0]:.1f}, {P3[1]:.1f})') #추가

ax.plot([P0[0], P1[0]], [P0[1], P1[1]], color='k')
ax.plot([P1[0], P2[0]], [P1[1], P2[1]], color='k')
#ax.plot([P2[0], P3[0]], [P2[1], P3[1]], color='k') #추가
# 곡선을 그립니다.
t = np.linspace(0, 1, 100)

#2차 베지어 곡선
x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t ** 2 * P2[0]
y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t ** 2 * P2[1]

#3차 베지어 곡선
#x = (1 - t) ** 3 * P0[0] + 3 * t * (1 - t) ** 2 * P1[0] + 3 * t ** 2 * (1 - t) * P2[0] + t ** 3 * P3[0]
#y = (1 - t) ** 3 * P0[1] + 3 * t * (1 - t) ** 2 * P1[1] + 3 * t ** 2 * (1 - t) * P2[1] + t ** 3 * P3[1]
ax.plot(x, y, color='g')

plt.show()
