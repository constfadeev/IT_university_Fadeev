# IT_university_task

Добрый день. 
Здесь пердставлено мое решение входного задания на курс по "Анализу данных средствами Python" пермского сетвого IT университета.

**Задание:**
Разработать программу на языке программирования Python, которая выделяет ключевые слова в заданном русскоязычном тексте. Использовать частотный анализ слов в тексте. За приведение слов к нормальной форме и исключение стоп-слов можно получить дополнительные баллы. Разрешается использования сторонних библиотек.
*Входные данные* – текстовый файл с расширением txt с заданным текстом, который вы можете выбрать самостоятельно (путь к файлу задается в консоли).
*Выходные данные* – таблица Excel с упорядоченным списком ключевых слов.

## Решение
Для выделения ключевых слов использовалась библиотека [**rutermextract**](https://pypi.org/project/rutermextract/), находящаяся в свободном доступе. Также использовалась библиотека **pandas** для удобной работы с выходными данными. 

```python
import pandas as pd
from rutermextract import TermExtractor
import codecs

term_extractor = TermExtractor()
df = pd.DataFrame(columns=['keyword', 'frequency'])
```

```python
path = input('Введите путь к файлу: ')
with codecs.open(path, 'r', 'utf_8_sig') as file:
    text = file.read().replace('\n', '')
```

```python
i = 0
for term in term_extractor(text, nested=True):
    df.loc[i] = [term.normalized, term.count]
    i += 1
```

```python
top_percent = 0.1

df_top = df.loc[df.frequency > df.loc[int(df.shape[0]*top_percent)].frequency]
df_top.to_excel(f'{path[:path.rfind(".")] + "_"}keywords.xlsx', index=False)
```
