from g4f.client import AsyncClient


async def gemini_generator(question: str) -> str:
    """
    Асинхронно генерирует ответ на заданный вопрос, используя модель Google Gemini.
    
    Параметры:
    question (str): вопрос, который будет отправлен в модель Gemini для генерации ответа.

    Возврат: 
    str: ответ, сгенерированный моделью Gemini. 
    В случае ошибки в процессе генерации, он возвращает сообщение об ошибке с подробностями исключения.
    """
    client = AsyncClient()
    try:
        response = await client.chat.completions.create(
            model='gemini',
            messages=[{
                'role': 'user',
                'content': question
            }]
        )
    except Exception as e:
        print(f'Debug:\n{e}')
        return f'Произошла ошибка во время генерации запроса :(\n'
    return response.choices[0].message.content