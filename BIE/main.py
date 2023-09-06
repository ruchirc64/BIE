"""
Run Training or Inference Pipeline based on user Runtime input
"""

# Import Python modules
import sys
import numpy as np
import pandas as pd
import logging.config
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__, BlobLeaseClient

# Import master Learner & Inference modules
import learner
import inference

# Create an object for FileHandler logger
# Use logger to log DEBUG, INFO, ERROR comments in file
logging.config.fileConfig(disable_existing_loggers=False, fname='../misc/logging.conf')
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    #Download required source data files for NPS and DEMOG.
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=stvmbieeusmo001;AccountKey=pJLKvde1W2nxNTDvFfFPUbNrlupqyH/I8hHWJYRftoDbiQwPL1Exlk+tOiSY1NPfXQfdLcf8hPaGHfJTjB/t9A==;EndpointSuffix=core.windows.net")
    blob_client = blob_service_client.get_blob_client(container='mobieids', blob='ingestion/stage/ml_nps/axciom/ACXIOM_TO_EDR_201910_STEP_3B_csv.csv')
    with open('../data/demog/ACXIOM_TO_EDR_201910_STEP_3B_csv.csv',"wb") as dfile:
        dfile.write(blob_client.download_blob().readall())

    blob_client = blob_service_client.get_blob_client(container='mobieids', blob='ingestion/stage/ml_nps/nps/2020_relationship_nps_data.xlsx')
    with open('../data/nps/2020_relationship_nps_data.xlsx',"wb") as dfile:
        dfile.write(blob_client.download_blob().readall())

    blob_client = blob_service_client.get_blob_client(container='mobieids', blob='ingestion/stage/ml_nps/nps/nps_historical_2017_19.xlsx')
    with open('../data/nps/nps_historical_2017_19.xlsx',"wb") as dfile:
        dfile.write(blob_client.download_blob().readall())

    blob_client = blob_service_client.get_blob_client(container='mobieids', blob='ingestion/stage/ml_nps/axciom/inference_batch_v1.csv')
    with open('../data/inference_batch_v1.csv',"wb") as dfile:
        dfile.write(blob_client.download_blob().readall())

    # Read command line inputs

    # Pipeline type to invoke
    pipeline = sys.argv[1]
    # Generate Dashboard explaining the model
    explainer_db = sys.argv[2]

    # Based on the pipeline type, invoke method of the corresponding module
    if(pipeline=="training"):
        learner.main(explainer_db)
    elif(pipeline=="inference"):
        inference.main(explainer_db)
    else:  # If pipeline type is entered incorrectly
        logger.error("Choose pipeline type correctly")
        sys.exit(1)


#added
