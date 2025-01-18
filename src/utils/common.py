import os
from box.exceptions import BoxValueError
import yaml
from src import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """reads yaml files and reaturns

    Args:
        path _to_yaml(str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        Configox: ConfigBox type

    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file :{path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e



@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """Create list of directory

    Args:
        path_to_directories(list):list of path of directories

        ignore_log(boool,optional): ignore if multiple dir is to be created
    """

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created dir at : {path}")


@ensure_annotations
def save_json(path:Path,data:dict):
    """Save json data
    Args:
        path(Path): path to json file 
        data(dict ): data to be saved in the json file

    """

    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file is saved at {path}")


@ensure_annotations
def load_json(path:Path) ->ConfigBox:
    """load the json file
    
    Args:
        path(Path): path to json file

    Returns:
        ConfigBox : data as class attribute instead of dict

    """

    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file is loaded successfully from :{path}")

@ensure_annotations
def save_bin(data:Any,path:Path):
    """save the binary fiules
    Args:
         data : data to be saved as binary
         path : path to the binary file

    """

    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file saved at :{path}")

@ensure_annotations
def load_bin(path:Path)->Any:
    """load binary data
    Args:
    path([Path]): path to the b inary file

    Returns:
        Any: object stored at the file

    """
    data  =joblib.load(path)
    logger.info(f"binary file loaded from:{path}")

    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """get sizez in kb

    Args:
        path(Path): path of the file
    
    Returns:
        str: size in kb

    """

    size_in_kb = round(os.path.getsize(path)/1024)

    return f"~ {size_in_kb}"

def decodeImage(imagestring,fileName):
    imgdata = base64.b64decode(imagestring)
    with open(fileName,"wb") as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())


