import data_processing.createInput as createInput
import data_processing.getRandomSample as getRandomSample
import multithreading.threading_data as threading_data
import data_processing.createDF as createDF
import pandas as pd
import logging
import log.log_config

def main(uploaded_file,prompt_first_half,prompt_second_half):

    """
    input: uploaded excel file, 2 prompt halves

    This function takes in the input excel file and updated prompt halves, calls createInputData function which returns the input_df along with a list of dictionaries.
    The input_list is then sampled through getSample function. This input along with 2 prompt halves is passed to threading_data.threads which performs the prompt processing
    and returns 2 list containing outputs (verdict and reason lists). Finally, these 2 lists along with the input dataframe is passed to create_dataframe function, which returns
    the processed_output df.

    output: returns the final output dataframe, which is sent for download to the user.

    """
    
    input_list,sample_df=createInput.createInputData(uploaded_file)

    sampled_input_values,sampled_input_indices=getRandomSample.getSample(input_list,len(sample_df))

    final_verdict_list,reason_list=threading_data.threads(sampled_input_values,prompt_first_half,prompt_second_half,sample_df)

    final_df=createDF.create_dataframe(sample_df,sampled_input_indices,final_verdict_list,reason_list)

    final_df=pd.DataFrame(final_df)

    log.log_config.setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Output dataframe processed successfully")



    return final_df



