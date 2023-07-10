import openai
import os
from dotenv import load_dotenv

load_dotenv()


class OpenAIService:
    """ Openai Service Class
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    def summarize_and_explain(self, content: str):
        """ This method sends a request to openai api
        with provided prompt
        """
        openai.api_key = OpenAIService.OPENAI_API_KEY
        user_prompt = content
        chat_response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Read this and understand the context,\
            if the context is about an article on how to do certain thing\
            walk me through how to do it step by step, if there is a need for\
            code snippet please provide and make me understand every\
            details of it in the simplest form possible" + "\n" + user_prompt,
            temperature=0.7,
            max_tokens=800,
            top_p=1,
            frequency_penalty=0.73,
            presence_penalty=0
        )
        # Call the OpenAI API to summarize and explain the content
        # Replace the following line with the actual API call to OpenAI
        summarized_content = chat_response['choices'][0]['text'].replace(
            "?", "")

        return summarized_content
