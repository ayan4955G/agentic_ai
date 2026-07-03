from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from anthropic import Anthropic
import os
from dotenv import load_dotenv
import json
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

api_key=os.getenv("API_KEY")

client = Anthropic(api_key=api_key)

embedder = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedder,
    url="http://localhost:6333",
    collection_name="vendor_2"
)

while True:

    user_query = input("Ask something : ")

    search_result = vector_db.similarity_search(query=user_query)

    # print("reference :", json.dumps(
    #     [{"page_content": doc.page_content, "metadata": doc.metadata} for doc in search_result],
    #     indent=4
    # ))

    context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
    for result in search_result])

    SYSTEM_PROMPT = """
    you are a helpfull AI Assistant who answers user query based on the available context retrived from the pdf file along with the page contents and the page number

    you should only Answer the user based on the context and navigate the user to open the right page number to know more.

    you should strictly follow the output format
    {{
        context : JSON,
        response : string,
    }}

    example:

    Userquery :  whats the Stipend ?

    OUTPUT: {{
        context : {{
                    {{
                "page_content": "SNZ CYBERINTELLECTS LLP \n2/2, F-GRD, F Kattaponnam, Chawl, S R Marg, Mukund Nagar, Dharavi, Mumbai- 400017 \nContact: 810 810 8486 | www.snzcyberintellects.com \n \n \n \n \n \n \nDate: 15th September 2025 \n \nMr. Ayan Imran Shaikh  \n                      Chawl no 40, room no 634, Bharat Nagar, \n Bandra East, Mumbai 400051, Maharashtra, India \n     \n  Subject: Internship Appointment Letter \n                     Dear Ayan Imran Shaikh, \nIn reference to your application, we would like to congratulate you on being selected for an internship with \nSNZ CYBERINTELLECTS LLP \nBelow are the details of your summer internship under the following terms and conditions:  \n1. Designation: Intern - Trainee \n2. Reporting: Sohail Shaikh \n3. Contract Period: 6 Months  \n4. Stipend \u2013 4,000/- (Four Thousand Rupee only) (Per Month) \n5. Place of Training: Hybrid (Work from Office/ Home) \n6. Benefits: Internship Certificate",
                "metadata": {{
                    "producer": "Microsoft\u00ae Word LTSC",
                    "creator": "Microsoft\u00ae Word LTSC",
                    "creationdate": "2025-09-30T13:31:00+05:30",
                    "author": "Nazish Shaikh",
                    "moddate": "2025-09-30T13:31:00+05:30",
                    "source": "E:\\gen ai\\RAG\\test.pdf",
                    "total_pages": 4,
                    "page": 0,
                    "page_label": "1",
                    "_id": "7b776245-da3f-4257-80fd-6726bb30d340",
                    "_collection_name": "leaning_RAG"
                }}
            }}
        }},
        response : "Based on the internship appointment letter from **SNZ CYBERINTELLECTS LLP**, the stipend is:

        > **₹4,000/- (Four Thousand Rupees only) per month**

        You can find this information on **Page 1** of the document under the terms and conditions of the internship."
    }}

    context:
    {context}
    """.format(context=context)

    response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[
                {"role":"user", "content":user_query}
            ],
    )

    text = response.content[0].text
    print("AI response :", text)