"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
# from main import sentenceFinal
import google.generativeai as genai


gemini_api_key = "AIzaSyCiJfsrCsbstRhsZDZANLXt6NuvfZxfkoU"
genai.configure(api_key=gemini_api_key)


# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "The topic is [topic: The topic] When I tell you a sentence\n\nYour name is teacher - Grade the sentence that I give you out of a 100.  - give a sentence about why you gave that score.\n\n- Grade it on relevance on the topic\n- Grammar\n- How much info you gave\n-Run-on sentence - it shouldn't be one\n- etc",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand! I'm ready to grade your sentences. Please give me the sentence and the topic, and I'll provide a score with feedback. \n\nFor example, you could say:\n\n\"**Topic:** The history of the internet. **Sentence:**  The internet was invented in the 1960s by a group of scientists.\" \n\nI'll then give you a score and explanation based on the criteria you mentioned. 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "[Topic: Taking a test during school]\nTaking tests are very stressful due to academic stress and success that you can acheive if you succedd.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, here's a breakdown of your sentence:\n\n**Score:** 55/100\n\n**Explanation:**\n\n* **Relevance to the topic:** The sentence is relevant to the topic of taking a test during school. It touches on the stress associated with tests.\n* **Grammar:**  The sentence has some grammatical errors:\n    * \"Taking tests are\" should be \"Taking tests **is**\" (tests is plural, but the verb should agree with the subject \"taking tests\"). \n    * \"Academic stress and success that you can acheive if you succedd\" -  \"acheive\" should be \"achieve\", and \"succedd\" should be \"succeed\".  There's also some awkward phrasing. \n* **Information:** The sentence provides a minimal amount of information. It mentions stress but doesn't specify what kind of stress or how the stress affects students. It also mentions success but doesn't explain what kind of success or how it's linked to the test.\n* **Run-on sentence:**  This sentence is not a run-on sentence.\n* **Overall:** The sentence needs more clarity and precise wording. It could benefit from expanding on the ideas of stress and success.  \n\n**Suggestions for improvement:**\n\n* **Clarity:** \"Taking tests can be very stressful, especially due to the pressure of academic performance and the potential for achieving success.\"\n* **Specificity:** \"The pressure to perform well academically can lead to significant stress during tests, as students worry about achieving a good grade and its impact on their future success.\" \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "give an individual score for each thing you grade it on \n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, here is a more detailed breakdown of the score for your sentence:\n\n**Sentence:** Taking tests are very stressful due to academic stress and success that you can acheive if you succedd.\n\n**Topic:** Taking a test during school\n\n**Scores:**\n\n* **Relevance to the topic:** 8/10 - It directly addresses the theme of test stress. \n* **Grammar:** 5/10 -  Subject-verb agreement issue, two misspelled words, and awkward phrasing significantly impact clarity.\n* **Information:** 6/10 - It mentions relevant concepts like stress and success but remains superficial without further elaboration.\n* **Run-on sentence:** 10/10 -  This is not a run-on sentence, so it fulfills this criterion. \n\n**Total Score:** 29/40  (Which translates to 55/100 when using a consistent scale) \n\nDoes this more specific breakdown help you understand the scoring better? Let me know if you have any other questions! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "[Topic: Taking a test during school]\nDue to the tests providing academic stress to students, the suicidal rates across the nation rose up approximately 15%, showing its negative impact across the world, and provides a reason why we should not have tests",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here's the breakdown of your sentence for the topic \"Taking a test during school\":\n\n**Score:** 40/100\n\n**Explanation:**\n\n* **Relevance to the topic (6/10):**  The sentence attempts to connect testing stress to serious consequences (suicide rates), which is relevant but presented in an overly simplistic and inaccurate way. \n* **Grammar (7/10):**  The grammar is mostly correct but the sentence structure is awkward and unclear.  \"Rose up\" is redundant, and \"across the world\" feels tacked on. \n* **Information (3/10):**  This is where the sentence falters most. It makes a very strong claim (15% rise in suicide rates) that needs strong evidence, which isn't provided.  Correlation doesn't equal causation, so directly linking test stress to suicide without substantial support is misleading.\n* **Run-on sentence (0/10):** This is a run-on sentence. It combines multiple sentences without proper punctuation.\n\n**Suggestions for improvement:**\n\n1. **Break down the sentence:** Divide the long sentence into shorter, clearer ones.\n2. **Provide evidence:** If you're going to claim a statistic, you need to back it up with credible sources. \n3. **Nuance the argument:** Instead of saying tests *cause* a rise in suicide rates, discuss the potential for test anxiety to contribute to student stress, which is a broader societal issue. \n\n**Example of a revised sentence:**  \n\n\"While more research is needed on the complex factors influencing mental health, it's crucial to acknowledge that academic pressure, including test anxiety, can significantly impact student well-being.  Creating supportive learning environments that prioritize student mental health should be a priority.\" \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "[Topic: Taking a test during school]\ntakinggggg textss ius googgg",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here is the breakdown of your sentence:\n\n**Score:** 10/100\n\n**Explanation:**\n\n* **Relevance to the topic (5/10):** I can somewhat tell that the sentence relates to tests, but the meaning is unclear.\n* **Grammar (0/10):**  \"Takinggggg\" and \"textss\" are misspelled and grammatically incorrect. \"Ius\" and \"googgg\" are not real words. \n* **Information (0/10):** The sentence doesn't convey any clear or meaningful information.\n* **Run-on sentence (5/10):** While not grammatically sound, it's technically not a run-on sentence because it's too short to qualify. \n\n**Overall:** This sentence appears to be nonsensical due to the misspellings and grammatical errors. Please try to use correct spelling and grammar so I can understand and grade your sentence accurately. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "write the score in [Score: Score/100] \nWrite the explanation around [Explanation: \nexplanation\n]",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I understand! From now on, I'll format my responses like this:\n\n**[Score: Score/100]**\n\n**[Explanation:\nexplanation\n]**\n\nFor example, if you gave me the sentence \"The cat sat on the mat.\" with the topic \"The history of the internet,\" my response would look like this: \n\n**[Score: 10/100]**\n\n**[Explanation:\nWhile the sentence is grammatically correct, it's completely irrelevant to the topic of the history of the internet. It provides no information about the topic. \n]** \n\nPlease proceed with your next sentence; I'm ready to grade it using the new format! 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "[Prompt: apples]\napples are very tasty and sweet.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "**[Score: 65/100]**\n\n**[Explanation:\nThis sentence is relevant to the topic of apples and grammatically correct. It provides some basic information about apples, stating that they are tasty and sweet. However, it lacks depth and could be more informative. \n\nHere are some ways to improve the sentence: \n\n* **Be more specific:** What kind of taste do apples have? Are they tart, tangy, or crisp?  \n* **Add details:**  What makes apples sweet?  \n* **Expand the sentence:** You could mention different varieties of apples, their uses, or health benefits. \n\nFor example, you could say:\n\n* \"Apples are known for their sweet and slightly tart flavor, making them a refreshing and enjoyable snack.\"\n* \"From the crisp sweetness of a Fuji to the tart bite of a Granny Smith, apples offer a variety of flavors to satisfy every palate.\"\n]** \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Instead of that can you make the output a dictionary separating the score and explanation.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You got it! I will now provide the score and explanation in a dictionary format. \n\nLet's try it out with your previous sentence. \n\n**Sentence:** apples are very tasty and sweet. \n**Topic:** apples\n\n```python\n{\n  \"Score\": 65,\n  \"Explanation\": \"This sentence is relevant to the topic of apples and grammatically correct. It provides some basic information about apples, stating that they are tasty and sweet. However, it lacks depth and could be more informative. Here are some ways to improve the sentence: Be more specific: What kind of taste do apples have? Are they tart, tangy, or crisp? Add details:  What makes apples sweet? Expand the sentence: You could mention different varieties of apples, their uses, or health benefits. For example, you could say: 'Apples are known for their sweet and slightly tart flavor, making them a refreshing and enjoyable snack.' or 'From the crisp sweetness of a Fuji to the tart bite of a Granny Smith, apples offer a variety of flavors to satisfy every palate.'\" \n}\n``` \n\nI hope this format is more helpful! Let me know what other sentences you'd like me to grade.  \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "[Topic: Taking a test during school]\niii love taking tesssts becuase itssssssss fuinnnnnnZY",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\n{\n  \"Score\": 10/100,\n  \"Explanation\": \"This sentence demonstrates a lack of effort and understanding of basic grammar and spelling. While it loosely relates to the topic of taking tests in school, the excessive use of letters and made-up words ('tesssts', 'itssssssss', 'fuinnnnnnZY') render it nonsensical.  To improve, focus on: 1) Using correct spelling. 2) Expressing a clear idea. 3)  Using proper grammar and punctuation.  Remember, tests are a part of school, and it's okay to find them challenging, but expressing your thoughts clearly is important.\"\n}\n``` \n",
      ],
    },  
    {
      "role": "user",
      "parts": [
        "Stop putting enter in your output as it breaks the dictonary that you make sometimes. That just means dont space it out like this:\n see how it spaced out with that? It breaks the dictonary when you put it outside of it as i am using python using your api. I am taking your output as text so it cant work if you put a space in it.",
      ],
    },
    
  ]
)
print("e")
def sendMessage(sentenceFinal):
    response = chat_session.send_message(sentenceFinal)
    return response.text
    # print(response.text)

print("ee")