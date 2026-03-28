import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(temperature=0)

# prompt 1 extract information
prompt_extract = ChatPromptTemplate.from_template("Extract the tech specifications from the following text: \n\n {text_input}")

# prompt 2 transform to json
prompt_transform = ChatPromptTemplate.from_template("""
Translate the following specifications into a json
 object with 'cpu','memory' and 'storage' as keys: \n\n{specifications}
 
 """)

extraction_chain = prompt_extract | llm | StrOutputParser()

full_chain = ({"specifications":extraction_chain} | prompt_transform | llm | StrOutputParser())

input_text = """ The new laptop model features a 3.5 GHz octa-core processor,
                 16 GB of RAM and a 1 TB NVMe SSD."""

final_result = full_chain.invoke({"text_input":input_text})

print("\n--- Final JSON Output ---")

print(final_result)