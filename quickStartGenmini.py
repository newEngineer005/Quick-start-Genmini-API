!pip install -q -U google-generativeai

# Import the Python SDK
import google.generativeai as genai
genai.configure(api_key="あなたのAPIキーを入れてください")

# モデルの選択（お好きな方を）
# model = genai.GenerativeModel('gemini-pro')
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = """
野原に住むとある一家のお話を考えて
"""
response = model.generate_content(prompt)
print(response.text)
