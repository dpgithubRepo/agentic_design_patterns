import os
import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# -------------------------
# Setup
# -------------------------
load_dotenv()

llm = ChatOpenAI(temperature=0)
parser = StrOutputParser()

# -------------------------
# File Reader
# -------------------------
def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

resume_text = read_txt("resume.txt")
jd_text = read_txt("jd.txt")

# -------------------------
# Prompts (FIXED with {{ }})
# -------------------------

prompt_extract_job_requirement = ChatPromptTemplate.from_template(
    "Extract the following from the job description:\n\n"
    "1. Technical Skills\n"
    "2. Soft Skills\n"
    "3. Tools / Technologies\n\n"
    "Return in JSON format:\n"
    "{{\n"
    '  "technical": [],\n'
    '  "soft": [],\n'
    '  "tools": []\n'
    "}}\n\n"
    "Job Description:\n"
    "{text_input_jd}"
)

prompt_extract_resume = ChatPromptTemplate.from_template(
    "Extract the following from the resume:\n\n"
    "1. Technical Skills\n"
    "2. Soft Skills\n\n"
    "Return in JSON format:\n"
    "{{\n"
    '  "technical": [],\n'
    '  "soft": []\n'
    "}}\n\n"
    "Resume:\n"
    "{text_input_resume}"
)

prompt_normalize = ChatPromptTemplate.from_template(
    "Normalize the following skills:\n"
    "- Convert to lowercase\n"
    "- Remove duplicates\n"
    '- Standardize names (e.g., "py" → "python", "aws cloud" → "aws")\n\n'
    "Return as a clean list.\n\n"
    "Skills:\n"
    "{text_input}"
)

prompt_compare = ChatPromptTemplate.from_template(
    "Compare candidate skills with job requirements.\n\n"
    "Return JSON with:\n"
    "{{\n"
    '  "matched_skills": [],\n'
    '  "missing_skills": [],\n'
    '  "extra_skills": [],\n'
    '  "match_percentage": number\n'
    "}}\n\n"
    "Candidate Skills:\n"
    "{normalized_resume}\n\n"
    "Job Requirements:\n"
    "{normalized_jd}"
)

# -------------------------
# Chains
# -------------------------
jd_extract_chain = prompt_extract_job_requirement | llm | parser
resume_extract_chain = prompt_extract_resume | llm | parser

normalize_chain = prompt_normalize | llm | parser
compare_chain = prompt_compare | llm | parser

# -------------------------
# Execution (STEP-BY-STEP)
# -------------------------

# Step 1: Extract
jd_extracted = jd_extract_chain.invoke({"text_input_jd": jd_text})
resume_extracted = resume_extract_chain.invoke({"text_input_resume": resume_text})

#print("\n--- Extracted JD ---\n")
#print(jd_extracted)

#print("\n--- Extracted Resume ---\n")
#print(resume_extracted)

# Step 2: Normalize
jd_normalized = normalize_chain.invoke({"text_input": jd_extracted})
resume_normalized = normalize_chain.invoke({"text_input": resume_extracted})

#print("\n--- Normalized JD ---\n")
#print(jd_normalized)

#print("\n--- Normalized Resume ---\n")
#print(resume_normalized)

# Step 3: Compare
final_result = compare_chain.invoke({
    "normalized_resume": resume_normalized,
    "normalized_jd": jd_normalized
})

#print("\n--- Final Output ---\n")
#print(final_result);




# -------------------------
# Optional: Parse JSON safely
# -------------------------
try:
    data = json.loads(final_result)
    print("\nMatch %:", data.get("match_percentage"))
except Exception:
    print("\n⚠️ Could not parse JSON cleanly")



data = json.loads(final_result)
missing_skillset = data["missing_skills"]



missing_skillset_input = ",".join(missing_skillset)

upscale_plan = ChatPromptTemplate.from_template(
     "Create plan for upscaling in the missing skills with online resources with links & references and required timeline.\n\n"
    "Return JSON with:\n"
    "{{\n"
    '  "missing_skills": [],\n'
    '  "plan": [],\n'
    '  "resources": []]\n'
    '   "timeline in months":number\n'
    "}}\n\n"
    "Missing Skills:\n"
    "{missing_skillset_input}\n\n"
)

upscale_plan_chain = upscale_plan | llm | StrOutputParser()
upscaling_plan_result = upscale_plan_chain.invoke({"missing_skillset_input":missing_skillset_input})




prompt_humanize = ChatPromptTemplate.from_template(
    "Convert the following structured data into clear, professional paragraphs:\n\n"
    "Missing Skills:\n{missing_skills}\n\n"
    "Plan:\n{plan}\n\n"
    "Timeline:\n{timeline}\n\n"
    "Resources:\n{resources}\n\n"
    "Write in a natural, human-friendly tone."
)


data = json.loads(upscaling_plan_result)
print("MISSING SKILLS ==> ", missing_skillset)
print("\n")
#print("Plan : ", data['plan'])
#print("Timeline in months : ", data['timeline in months'])
#print("Recommended resources",data['resources'])

humanize_chain = prompt_humanize | llm | StrOutputParser()

human_text = humanize_chain.invoke({"missing_skills": missing_skillset_input,
    "plan": "\n".join( data['plan']),
    "timeline":  data['timeline in months'],
    "resources": str(data['resources'])})


print("***** plan to upscale ***********************\n")


print(human_text)

