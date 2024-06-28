import streamlit as st
import portal_features.upload_file as upload_file
import portal_features.load_text as load_text
import constants
import portal_features.download_sample as download_sample
import extra_streamlit_components as stx
from datetime import datetime, timedelta

cookie_manager = stx.CookieManager(key='AppKey')

def main():

    """This streamlit app contains 2 tabs, daily analysis and monthly trends. Daily Analysis tab contains 2 editable text areas which store prompts in it. These prompts can be
    changed according to the user's thinking and are saved in cookies, which get updated everytime you save the prompts. The user can then upload an excel file in a specified
    format which they can refer by downloading the sample_data_format file. 

    Once they upload this, and click on process data, they will get a processed output excel file which contains the AI_Verdict and Reason along with the corresponding input data.
    """

    expire_date = datetime.now() + timedelta(days=365)

    initial_first_text_cookie=cookie_manager.get('first_text')
    initial_first_text = initial_first_text_cookie if initial_first_text_cookie else load_text.load_text(constants.original_prompt_first_half_filepath)

    initial_second_text_cookie=cookie_manager.get('second_text')
    initial_second_text = initial_second_text_cookie if initial_second_text_cookie else load_text.load_text(constants.original_prompt_second_half_filepath)

    tab1, tab2 = st.tabs([constants.tab1_header,constants.tab2_header])
    
    with tab1:
        st.header(constants.tab1_header)

        updated_first_prompt = st.text_area(constants.ta1_header, value=initial_first_text, height=constants.ta_height)
        updated_second_prompt = st.text_area(constants.ta2_header, value=initial_second_text, height=constants.ta_height)

        col1, col2  = st.columns([12, 5])

        with col1:
            if st.button(constants.save_button_text):
                cookie_manager.set('first_text', updated_first_prompt,key='first_text',expires_at=expire_date)
                cookie_manager.set('second_text', updated_second_prompt,key='second_text',expires_at=expire_date)
                st.success(constants.prompt_save_message)
                
        with col2:
            download_sample.download_sample_data()

        uploaded_file = st.file_uploader(constants.file_uploader_message, type=['xlsx'])

        if st.button(constants.process_button_text):
            upload_file.process_data(updated_first_prompt, updated_second_prompt,uploaded_file)
 
    with tab2:
        st.header(constants.tab2_header)
        st.write(constants.tab2_subheading)

if __name__ == '__main__':
    main()
