#!/usr/bin/python

from typing import List, Union, Dict, Tuple
import work_on_files_content as work_content
import header_load_settings_and_validate as initial_stage


def main() -> None:
    instances: int = 0
    value_to_load_validate_config: int = 1
    config_content: Dict = {}
    message_from_validation: str = ''

    initial_stage.printing_what_we_have()

    while value_to_load_validate_config == 1:
        path_of_config_file, instances = initial_stage.ask_for_config(instances=0)

        config_content, value_to_load_validate_config, message_from_validation = initial_stage.validate_config_file(given_file=path_of_config_file)
        if value_to_load_validate_config == 1:
            continue

        value_to_load_validate_config, message_from_validation = initial_stage.check_content_config_file(cfg_file=config_content)

    work_content.load_grades_students(given_cfg=config_content)



if __name__ == '__main__':
    main()
