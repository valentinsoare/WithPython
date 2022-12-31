#!/usr/bin/python

from typing import List, Union, Dict, Tuple
from app_components import work_on_files_content as work_content
from app_components import header_load_settings_and_validate as loading_stage


def main() -> None:
    instances: int = 0
    value_to_load_validate_config: int = 1
    config_content: Dict = {}
    #message_from_validation: str = ''
    first_config: str = ''

    loading_stage.printing_what_we_have()

    while True:
        while value_to_load_validate_config == 1:
            path_of_config_file, instances = loading_stage.ask_for_config(instances=instances, initial_config=first_config)
            first_config = path_of_config_file

            config_content, value_to_load_validate_config, message_from_validation = loading_stage.validate_config_file(
                given_file=path_of_config_file)
            if value_to_load_validate_config == 1:
                instances = 0
                continue

            value_to_load_validate_config, message_from_validation = loading_stage.check_content_config_file(cfg_file=config_content)

        input_from, settings_input, classes_settings, output_to, settings_output, logging_input, logging_output = work_content.extract_from_config_file \
            (given_cfg=config_content)

        loaded_content, value_to_load_validate_config = work_content.load_content(where_to_load_content=input_from, input_config=settings_input,
                                                                                  output_config=settings_output, classes_config=classes_settings)


if __name__ == '__main__':
    main()
