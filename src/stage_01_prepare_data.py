import argparse
import os
import shutil
from tqdm import tqdm
import logging
import random
from src.utils import read_yaml,create_directories

STAGE="Prepare_Data"

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs'),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
)


def main(config_path, params_path):
    ## read config file  
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    source_data_dir=config["source_data"]["data_dir"]
    source_data_file=config["source_data"]["data_file"]
    source_data_path=os.path.join(source_data_dir, source_data_file)

    split=params["prepare"]["split"]# split ratio
    seed=params["prepare"]["seed"]
    random.seed(seed)
    artifacts=config["artifacts"]
    prepare_data_dir_path=os.path.join(artifacts["ARTIFACTS_DIR"],artifacts["PREPARED_DATA"])
    create_directories([prepare_data_dir_path])






if __name__== '__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="configs/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")
    parsed_args=args.parse_args()

    try:
        logging.info("\n*********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>> stahe {STAGE} completed <<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e