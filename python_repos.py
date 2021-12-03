import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Haz una llamada de API y guarda la respuesta.
URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(URL)
print("Status code:", r.status_code)

# Guarda una respuesta API en una variable.
response_dict = r.json()
print("Repositorios totales:", response_dict['total_count'])

# Explora informacion acerca de los repositorios.
repo_dicts = response_dict['items']
print('Numero de objetos:', len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

# Haz una visualizacion.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Proyectos en Python mas vistos en GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

print("\nSelecciona informacion acerca de cada repositorio:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])

# Examina el primer repositorio.
#repo_dict = repo_dicts[0]
# print("\nSelecciona info. acerca del primer repositorio:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])
# print("\nKeys:", len(repo_dict))

#for key in sorted(repo_dict.keys()):
    #print(key)

# Procesa los resultados.
#print(response_dict.keys())
