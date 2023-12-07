from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage

chat = ChatOpenAI(model="gpt-3.5-turbo")

propmt = PromptTemplate(
    template="{product}はどこの会社が開発した製品ですか?",
    input_variables=[
        "product",
    ],
)

result = chat(
    [HumanMessage(content=propmt.format(product="iPhone"))],
)

print(result.content)
