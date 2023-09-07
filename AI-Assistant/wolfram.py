import wolframalpha as wf

question = str(input("Question : "))

client_api = wf.Client('Your API-ID')

response = client.query(question)

answer = next(response.results).text

print(answer)

"""
Wolfram Alpha Python module to I can make my assistant solve math problems.
You can implement this module in voice assistant, you can extract your voice question
'example: you said calculate 1 + 1' --> in this command not working because the assistant processing the full query,
so you delete the other words, note the 'answer variable in the next() function store the answer list of the array so you can
Extract your words, a little bit think, how you can pass the query on to the assistant.
DEMO: Understand and achieve.
"""
 if 'calculate' in query:
            client = wf.Client('VWGERK-6X5535TJHJ')   
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            response = client.query(' '.join(query))
            answer = next(response.results).text
            print(answer)
            speak(answer)
   
