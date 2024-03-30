# playdjango

## Requirement

- Python >= 3.12
- [poetry](https://python-poetry.org/docs/#installation)
  - 本專案用 poetry 管理 venv 跟套件

## Quick start

```bash
git clone https://github.com/zhshize/playdjango.git  # 把程式碼抓下來
cd playdjango

poetry init  # 初始化專案設定
poetry shell  # 進入虛擬環境，類似 venv activate
poetry install  # 安裝有用到的套件

poetry run python manage.py runserver  # 開啟測試伺服器，網址會是 http://127.0.0.1:8000
```

接著用瀏覽器打開 `http://127.0.0.1:8000/home`
