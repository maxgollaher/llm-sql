from DB import DB
from OpenAiUtils import OpenAiUtils


def write_queries_to_file(file, questions, openai: OpenAiUtils, db: DB, section_title, response_method):
    file.write(f'## {section_title}\n')
    for i, question in enumerate(questions):
        query = response_method(question)
        db_response = db.execute(query)
        friendly_response = openai.get_friend_response(question, db_response)
        file.write(f'Question {i + 1}\n')
        file.write(f'* Prompt: {question}\n')
        file.write('* Query: \n```mysql\n' + query + '\n```\n\n')
        file.write('* DB Response: \n```text\n' + str(db_response) + '\n```\n\n')
        file.write(f'* Friendly Response: {friendly_response}\n\n')
        file.write('---\n')


def main():
    db = DB()
    openai = OpenAiUtils()
    questions = [
        "What is the total amount of all transactions?",
        "What is the average cost of all items?",
        "What is the most expensive item?",
        "Who is my most frequent customer?",
        "What is the most popular item?",
        "Which items are my least productive?",
        "Who is my most profitable customer?",
        "Who is my least profitable customer?"
    ]

    with open('queries.md', 'w') as file:
        file.write('# Queries\n')

        write_queries_to_file(file, questions, openai, db, 'Zero Shot Examples', openai.get_zero_shot__response)
        write_queries_to_file(file, questions, openai, db, 'Single Domain Examples', openai.get_single_domain_response)


if __name__ == '__main__':
    main()
