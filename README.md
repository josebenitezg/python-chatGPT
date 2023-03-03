# python-chatGPT

This is an example how you can build a powerful chatGPT on python with OpenAI API.

## Usage :nut_and_bolt:

1. Clone this repo

```
git clone https://github.com/josebenitezg/python-chatGPT.git
```

2. Create a virtual enviroment

```
python -m venv env
```

3. Activate virtual enviroment

- for linux

```
source env/bin/activate
```

- for windows

```
env\Scripts\Activate.bat
```

4. Install requirements

```
pip install -r requirements.txt
```
You have to instal the latest version of OPENAI in case you already have one.

5. Create a .env file with the apikey from OPENAI, with the following content

```
OPENAI_API_KEY
```

5. And enjoy the app

```
streamlit run main.py
```




