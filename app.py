from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import streamlit as st
import pandas as pd
#to load API key
#from dotenv import load_dotenv

#load csv file
def create_df(csv_):
    csv_.seek(0)
    df = pd.read_csv(csv_)
    print(df.head())
    return df

#generation of response
def generate_response(csv_file,input_query,key):
    df = create_df(csv_file)
    llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', openai_api_key=key)
    agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)
    response = agent.run(input_query)
    return st.success(response)

def main():
    #load_dotenv()
    st.title("ChatCSV")
    st.write("Please Upload Your CSV File")
    csv = st.file_uploader("Upload Your CSV",type='csv')
    if csv is not None:
        df=create_df(csv)
        with st.expander('See DataFrame'):
            st.write(df)
        
        question_list = [
        'How many rows are there?',
        'What is the range of values for MolWt with logS greater than 0?',
        'How many rows have MolLogP value greater than 0.',
        'Other']
        key = st.text_area('Enter Your Open AI API Key:')
        query = st.selectbox('Select your Query: ', question_list, disabled=not csv)
        if query is 'Other':
            query = st.text_input('Enter your query:', placeholder = 'Enter query here ...', disabled=not csv)
        if key.startswith('sk-'):
            generate_response(csv,query,key)

if __name__ == '__main__':
    main()