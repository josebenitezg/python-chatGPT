# python-chatGPT
![Drag Racing](https://openaicom.imgix.net/8d14e8f0-e267-4b8b-a9f2-a79120808f5a/chatgpt.jpg?fm=auto&q=80&auto=compress,format&fit=min&rect=0,0,2048,2048&w=3840&h=3840)
## This is an example how you can build a powerful chatGPT on python with OpenAI API.

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
You have to install the latest version of OPENAI in case you already have one.

5. Create a .env file with the apikey from OPENAI, with the following content

```
OPENAI_API_KEY
```

5. And enjoy the app

```
streamlit run main.py
```




