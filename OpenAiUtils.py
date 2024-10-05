from openai import OpenAI
import config


class OpenAiUtils:
    COMMON_PROMPT = ("Give me a MYSQL SELECT query that answers the following question,"
                     "if there is an error, do not explain it. Answer only with valid MYSQL syntax,"
                     "do not surround the query with a code-block.")

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OpenAiUtils, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'client'):
            self.client = OpenAI(api_key=config.OPENAI_TOKEN)

    def get_completion(self, messages, max_tokens, temperature):
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return completion.choices[0].message.content

    def get_response(self, prompt, message_pairs=None, max_tokens=200, temperature=0):

        with open('sql/create-database.sql', 'r') as file:
            setup_script = file.read()

        messages = [{"role": "system", "content": setup_script}, {"role": "system", "content": self.COMMON_PROMPT}]
        if message_pairs:
            for pair in message_pairs:
                messages.append({"role": "user", "content": pair[0]})
                messages.append({"role": "assistant", "content": pair[1]})
        messages.append({"role": "user", "content": prompt})

        return self.get_completion(messages, max_tokens, temperature)

    def get_friend_response(self, question, database_results):
        prompt = f"""I asked the following question: {question}\n
        The database responded with: {database_results}\n
        Only answer the question, do not explain the answer, do not include any code, only the answer."""

        messages = [{"role": "user", "content": prompt}]
        return self.get_completion(messages, 50, 0.6)

    def get_zero_shot__response(self, message):
        return self.get_response(message)

    def get_single_domain_response(self, message):
        message_pairs = [("What is most that any user has spent in my store?",
                          "SELECT MAX(total) FROM (SELECT SUM(Amount) AS total FROM Transaction GROUP BY UserId) AS t;")]
        return self.get_response(message, message_pairs)


if __name__ == '__main__':
    openai = OpenAiUtils()
