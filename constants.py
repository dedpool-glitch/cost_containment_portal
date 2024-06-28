tab1_header="Daily Analysis"
tab2_header="Monthly Trends"
tab2_subheading="This section is for analyzing monthly trends."
prompt_save_message="Prompt Saved successfully!"
ta1_header="Prompt 1st Half"
ta2_header="Prompt 2nd Half"
ta_height=200
save_button_text="Save Prompt"
process_button_text="Process Data"
download_sample_button_text="Download Sample Data"
download_output_button_text="Download Output as Excel"
output_filename='processed_output.xlsx'
file_uploader_message="Choose a file"
original_prompt_first_half_filepath="D:\cost_containment\original_prompt_first_half.txt"
original_prompt_second_half_filepath="D:\cost_containment\original_prompt_second_half.txt"
concurrent_threads = 10
max_retries=3


sample_data_filepath="D:\cost_containment\sample_data_format.xlsx"

response_structure="""{
    
        "treatment_verification": {
            "[Treatment Name]": "necessary" or "unnecessary",
            ...
        },
        "final_verdict": "PASS" or "FAIL"
        "reason":"[up to 30 words]"
        }"""