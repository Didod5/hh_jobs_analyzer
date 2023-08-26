# hh_jobs_analyzer
Скрипт для визуализации основных ключевых навыков из вакансий на hh.

Для сбора данных используются библиотеки Selenuim (используется драйвер для Chrome) и BeautifulSoup4, информация записывается в файл result.txt, далее с помощью matplotlib она визуализируется в виде диаграммы.


![изображение](https://github.com/Didod5/hh_jobs_analyzer/assets/123077884/bbe43931-d7ad-4039-8645-e3682ff6acb4)


 **Настройки в config.py:**
- driver_path - путь к установленному веб-драйверу
- url - ссылка на поиск вакансий с хэдхантера с выбранными фильтрами
- min_num_of_repeat - минимальное кол-во повторений навыка для отображения в итоговой диаграмме
