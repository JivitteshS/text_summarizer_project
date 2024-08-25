import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_file: Path)-> ConfigBox:
    """Read the YAML file and returns
    
    Args:
    path_to_file (Path): Path to the YAML file

    Raises:
    ValueError: if yaml is empty
    e:empty file

    Returns:
    ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_file, 'r') as file:
            config = yaml.safe_load(file)
            logger.info(f"yaml file {path_to_file} loaded successfully")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
def create_directories(path_to_directory: list,verbose=True):
    """Create directories
    
    Args:
    path_to_directory (list): List of directory paths
    ignore_log (bool,optional): Igore if multiple directories are created/ Defaults to fale"""

    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created successfully")


@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB
    
    Args:
    path (path): path of the file

    Returns:
    str: size of the file in KB
    """

    size_in_kb =round(os.path.getsize(path)/1024)

    return f"~ {size_in_kb} KB"