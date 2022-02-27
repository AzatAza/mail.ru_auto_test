[![Test site https://mail.ru/](https://github.com/AzatAza/mail.ru_auto_test/actions/workflows/task's_CICD.yml/badge.svg)](https://github.com/AzatAza/mail.ru_auto_test/actions/workflows/task's_CICD.yml)
# Test task "Лаборатория качества
Selenium/Python

```
The Task
1. Login on mail.ru
2. Go to "Compose a letter"
3. Fill in a random text
4. Send it
```

Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

pre-commit https://pre-commit.com
```
pre-commit run --all-files
```

Test site
```
https://mail.ru/
```

Allure report
```
pytest --alluredir=allure-results/
allure serve allure-results/
```
