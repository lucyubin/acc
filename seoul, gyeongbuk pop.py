import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

file_path = '.'

# Population of Daily Night Time in Seoul, Gyeongbuk

card_sum = pd.read_csv(file_path + 'card_sum.csv')
card_sl = card_sum[card_sum['sgg_cd'].astype(str).str.startswith('11')]
card_sl = card_sl.groupby('date')['pop'].mean()
card_sl = card_sl.reset_index()

card_gb = card_sum[card_sum['sgg_cd'].astype(str).str.startswith('47')]
card_gb = card_gb.groupby('date')['pop'].mean()
card_gb = card_gb.reset_index()

pop_sum = pd.read_csv(file_path + 'pop_sum.csv')
pop_sl = pop_sum[pop_sum['sgg_cd'].astype(str).str.startswith('11')]
pop_sl = pop_sl.groupby('date')['pop'].mean()
pop_sl = pop_sl.reset_index()

pop_gb = pop_sum[pop_sum['sgg_cd'].astype(str).str.startswith('47')]
pop_gb = pop_gb.groupby('date')['pop'].mean()
pop_gb = pop_gb.reset_index()


# Seoul
dates = pop_sum['date']
fig, ax1 = plt.subplots(figsize=(12, 6))
x = range(1, 32)

ax1.plot(x, card_sl['pop'], color='#a3cd5e', linewidth=3)
ax1.tick_params(axis='y', labelcolor='#a3cd5e')

ax2 = ax1.twinx()
ax2.plot(x, pop_sl['pop'], color='#2c619c', linewidth=3)
ax2.tick_params(axis='y', labelcolor='#2c619c')

plt.xticks(x, fontsize=14)

plt.tight_layout()
plt.savefig('./seoul.png', format='jpeg', dpi=300)
plt.show()


# Gyeongbuk
dates = pop_sum['date']
fig, ax1 = plt.subplots(figsize=(12, 6))
x = range(1, 32)

ax1.plot(x, card_gb['pop'], color='#a3cd5e', linewidth=3)
ax1.tick_params(axis='y', labelcolor='#a3cd5e')

ax2 = ax1.twinx()
ax2.plot(x, pop_gb['pop'], color='#2c619c', linewidth=3)
ax2.tick_params(axis='y', labelcolor='#2c619c')

plt.xticks(x, fontsize=14)

plt.tight_layout()
plt.savefig('./gb.png', format='jpeg', dpi=300)
plt.show()