#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install nba_api


# In[30]:


from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
import matplotlib.pyplot as plt


# In[31]:


nba_teams = teams.get_teams()
nba_teams[:5]


# In[32]:


def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key,value in dict_.items():
            out_dict[key].append(value)
    return out_dict
dict_nba_team = one_dict(nba_teams)


# In[33]:


df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()


# In[34]:


df_warriors=df_teams[df_teams["nickname"]=="Warriors"]
df_warriors


# In[35]:


id_warriors = df_warriors[['id']].values[0][0]
id_warriors


# In[68]:


gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
games=gamefinder.get_data_frames()[0]
games.head()


# In[71]:


games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']


# In[78]:


fig, ax =plt.subplots()
plt.ylabel('PLUS_MINUS')
games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away","home"])
plt.show()


# In[ ]:





# In[ ]:




