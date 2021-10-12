import requests

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import random


url = (f'https://superheroapi.com/api/6613951791952093/{str(732)}/powerstats')
r = requests.get(url)
#dictionaries from url merge with list then changed to json
characters= []

for hero in range(1,723):
    url = (f'https://superheroapi.com/api/6613951791952093/{str(hero)}/powerstats')
    r = requests.get(url)
    characters.append(r.json())

else:
    pass

    #changed to DataFrame
char = pd.DataFrame(characters)

#reorganized columns
char = char[['name', 'power' , 'strength' , 'intelligence' , 'speed' , 'combat' , 'durability']]

#replace null value to 10
char = char.replace('null', '10')

#set custom index to name
char = char.set_index('name')

#convert multiple columns to int
char = char.apply(pd.to_numeric)

#compare vaules of strongest
char.sort_values(by =['power','strength', 'intelligence', 'speed', 'combat'], ascending = False, kind = 'mergesort' ) [:10]

plt.figure(figsize=(16,9))

ax1 = plt.subplot(3,1,1)
ax1.set_title('Power')
ax1.hist(char['power'])
ax1.axvline(x=np.mean(char['power']), color = 'orange')

ax2= plt.subplot(3,1,2)
ax2.set_title('Strength')
ax2.hist(char['strength'])
ax2.axvline(x=np.mean(char['strength']), color ='orange')

ax3 = plt.subplot(3,1,3)
ax3.set_title('Intelligence')
ax3.hist(char['intelligence'])
ax3.axvline(x=np.mean(char['intelligence']) , color = 'orange');


plt.figure(figsize = (16,9))


ax1 = plt.subplot(3,1,1)
ax1.set_title('Speed')
ax1.hist(char['speed'])
ax1.axvline(x=np.mean(char['speed']), color = 'orange')

ax2= plt.subplot(3,1,2)
ax2.set_title('Combat')
ax2.hist(char['combat'])
ax2.axvline(x=np.mean(char['combat']), color ='orange')

ax3 = plt.subplot(3,1,3)
ax3.set_title('Durability')
ax3.hist(char['durability'])
ax3.axvline(x=np.mean(char['durability']) , color = 'orange');
