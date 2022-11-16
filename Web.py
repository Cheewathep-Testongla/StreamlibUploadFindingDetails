import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="Upload Safety Audit Finding",
    page_icon="⚠️",
)

ResetRender = False

Header = [
        'No.', 'Company', 'Area', 'Sub Area', 
        'Reportor', 'Contractor', 'Type of finding', 
        'Topic', 'Details', 'Corrective Action', 
        'Issue Date', 'Due Date', 'Status'
        ]

def SubmitData(DataHeader, FindingNo, FindingCompany, 
                FindingArea, FindingSubArea, FindingReportor, 
                FindingContractor, FindingTypeOfFinding, FindingTopic, 
                FindingDetails, FindingCorrectiveAction, FindingIssueDate, 
                FindingDueDate, FindingStatus):
    global Checkheader, ResetRender
    Checkheader = True

    for value in DataHeader:
        if value not in Header:
            Checkheader = False
            break
    
    if Checkheader == True:
        url = 'https://smit3api.azurewebsites.net/UploadNewFindingDetails'
        # url = 'http://0.0.0.0:80/UploadNewFindingDetails'
        x = requests.post(url, json = {
                                        "No" : FindingNo,
                                        "Company" : FindingCompany,
                                        "Area" : FindingArea,
                                        "SubArea" : FindingSubArea,
                                        "Reportor" : FindingReportor,
                                        "Contractor" : FindingContractor,
                                        "TypeOfFinding" : FindingTypeOfFinding,
                                        "Topic" : FindingTopic,
                                        "Details" : FindingDetails,
                                        "CorrectiveAction" : FindingCorrectiveAction,
                                        "IssueDate" : FindingIssueDate,
                                        "DueDate" : FindingDueDate,
                                        "Status" : FindingStatus
                                    }
                                , auth = ('SMIT3API', 'SMIT3SafetyAudit2022'))
        st.warning(x.text)
        ResetRender = True
    else:
        st.text("Header is Invalid!!!")

def main():    
    global FindingNo, FindingCompany, FindingArea, FindingSubArea, FindingReportor, FindingContractor, FindingTypeOfFinding, FindingTopic, FindingDetails, FindingCorrectiveAction, FindingIssueDate, FindingDueDate, FindingStatus 

    global DataHeader, ResetRender, Checkheader

    Checkheader = True

    FindingNo = []
    FindingCompany = []
    FindingArea = []
    FindingSubArea = []
    FindingReportor = []
    FindingContractor = []
    FindingTypeOfFinding = []
    FindingTopic = []
    FindingDetails = []
    FindingCorrectiveAction = []
    FindingIssueDate = []
    FindingDueDate = []
    FindingStatus = [] 

    DataHeader = []

    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden; }
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    st.markdown("<div><h2 style='text-align: center; color: 62CDFF; font-family: Century Gothic'> Upload Safety Audit Finding </h2></div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a file")
    st.markdown("<div><h3 style='text-align: center; color: 62CDFF; font-family: Century Gothic'> Please used header like this!!! </h3></div>", unsafe_allow_html=True)
    st.text(Header)

    if uploaded_file is not None:
        RawFindingData = pd.read_csv(uploaded_file)
        st.dataframe(RawFindingData)

        DataHeader = list(RawFindingData.columns)

        for value in DataHeader:
            if value not in Header:
                Checkheader = False
                break

        if Checkheader == True:
            FindingNo = RawFindingData['No.'].tolist()

            FindingCompany = RawFindingData['Company'].tolist()
            FindingCompany = ["-" if pd.isnull(x) else x for x in FindingCompany]

            FindingArea = RawFindingData['Area'].tolist()
            FindingArea = ["-" if pd.isnull(x) else x for x in FindingArea]

            FindingSubArea = RawFindingData['Sub Area'].tolist()
            FindingSubArea = ["-" if pd.isnull(x) else x for x in FindingSubArea]

            FindingReportor = RawFindingData['Reportor'].tolist()
            FindingReportor = ["-" if pd.isnull(x) else x for x in FindingReportor]

            FindingContractor = RawFindingData['Contractor'].tolist()
            FindingContractor = ["-" if pd.isnull(x) else x for x in FindingContractor]

            FindingTypeOfFinding = RawFindingData['Type of finding'].tolist()
            FindingTypeOfFinding = ["-" if pd.isnull(x) else x for x in FindingTypeOfFinding]
            
            FindingTopic = RawFindingData['Topic'].tolist()
            FindingTopic = ["-" if pd.isnull(x) else x for x in FindingTopic]

            FindingDetails = RawFindingData['Details'].tolist()
            FindingDetails = ["-" if pd.isnull(x) else x for x in FindingDetails]

            FindingCorrectiveAction = RawFindingData['Corrective Action'].tolist()
            FindingCorrectiveAction = ["-" if pd.isnull(x) else x for x in FindingCorrectiveAction]

            FindingIssueDate = RawFindingData['Issue Date'].tolist()
            FindingIssueDate = ["-" if pd.isnull(x) else x for x in FindingIssueDate]

            FindingDueDate = RawFindingData['Due Date'].tolist()
            FindingDueDate = ["-" if pd.isnull(x) else x for x in FindingDueDate]

            FindingStatus = RawFindingData['Status'].tolist()
            FindingStatus = ["-" if pd.isnull(x) else x for x in FindingStatus]

        if st.button("Submit"):
            SubmitData(DataHeader, FindingNo, FindingCompany, 
                        FindingArea, FindingSubArea, FindingReportor, 
                        FindingContractor, FindingTypeOfFinding, FindingTopic, 
                        FindingDetails, FindingCorrectiveAction, FindingIssueDate, 
                        FindingDueDate, FindingStatus)

    
    # except:
        # st.markdown("There is something wrong with file!")
        
if __name__ == '__main__':    
    main()