from django.shortcuts import render, redirect
from openai import OpenAI
# Create your views here.
import os
from dotenv import load_dotenv

load_dotenv()

def gpt_process(strVal):

    client = OpenAI(
        api_key=os.getenv('OPEN_API_KEY'))

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant, you have to give answer correctly and give your answer in a single line minimum."},
            {"role": "user", "content": strVal}
        ]
    )
    return str(completion.choices[0].message.content)

def chatgpt(request):
    result = None
    gptProcessed =None
    if request.method == "POST":
        myinput = str(request.POST['text'])
        gptProcessed = gpt_process(myinput)
        result = gptProcessed
    return render(request, 'chatgpt.html',{'result': result})