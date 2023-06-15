import openai

openai.api_key = "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"

celebrity = input("Enter the celebrity name: ")
name = input("Enter your child's name: ")



    gpt_prompt = 'What would' +str(celebrity) +'advice' + str(name) + ' 15 lines as a personal letter'
    def get_response (gpt_prompt):

        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=gpt_prompt,
          temperature=0.5,
          max_tokens=256,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        return (response['choices'][0]['text'])



    answer = get_response (gpt_prompt)
    get_response (gpt_prompt)
        
    print(answer)