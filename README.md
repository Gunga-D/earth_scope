# GEOSCOPE
![build status](https://badgen.net/badge/build/latest/green?icon=github)
![code style](https://badgen.net/static/code%20style/standard/f2a)

Geoscope - это геофизический инструмент для получения геофизических данных с различных служб.

На данный момент поддерживает 5 геофизических служб, где 5 - FDSN является оберткой/протоколом для синхронизации работы других.

Для начала работы необходимо запустить следующие две команды:
```bin
python bin/cli.py run-server 
```
и
```bin
python bin/cli.py run-worker 
```

## Функциональность 
Сервис позволяет как скачивать в реальном времени с выбранных станций данные в формате mseed, так и по указанному промежутку времени получать необходимые волновые формы и соответственно данные

## Поддерживаемые геофизические службы
- IRIS - Американская службы геофизических сетей
- GEOFON - Немецкая глобальная сеть сейсмических широкополосных станций
- FDSN - Мировая сеть 
- IPGP - Франзуская сейсмологическая сеть
- NORSAR - Группа NORSAR