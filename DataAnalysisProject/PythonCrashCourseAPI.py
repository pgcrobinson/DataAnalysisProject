import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)

response_dict=r.json()
#print(response_dict.keys())

#print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
#print("Repositories returned:", len(repo_dicts))

#repo_dict = repo_dicts[0]


#print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)

#print("\nSelected information about each repository:")
#for repo_dict in repo_dicts:
#    print('Name:', repo_dict['name'])
#    print('Owner', repo_dict['owner']['login'])
#    print('Stars:', repo_dict['stargazers_count'])
#    print('Repository:', repo_dict['html_url'])
#    #print('Created:', repo_dict['created_at'])
#    #print('Updated:', repo_dict['updated_at'])
#    print('Description:', repo_dict['description'])
#    print('')

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style= LS('#333366',base_style=LCS)
my_style.title_font_size=24
my_style.label_font_size=14
my_style.major_label_font_size=18

my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000

chart=pygal.Bar(my_config,style=my_style)
chart.title ='Most starred Python Projects on Github'
chart.x_labels= names


chart.add('',stars)
chart.render_to_file('python_repos.svg')