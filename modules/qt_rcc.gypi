# This file is part of Desktop App Toolkit,
# a set of libraries for developing nice desktop applications.
#
# For license and copyright information please follow this link:
# https://github.com/desktop-app/legal/blob/master/LEGAL

{
  'rules': [{
    'rule_name': 'qt_rcc',
    'extension': 'qrc',
    'inputs': [
      '<(SHARED_INTERMEDIATE_DIR)/update_dependent_qrc.timestamp',
    ],
    'outputs': [
      '<(SHARED_INTERMEDIATE_DIR)/<(_target_name)/qrc/qrc_<(RULE_INPUT_ROOT).cpp',
    ],
    'action': [
      '<(qt_loc)/bin/rcc<(exe_ext)',
      '-name', '<(RULE_INPUT_ROOT)',
      '-no-compress',
      '<(RULE_INPUT_PATH)',
      '-o', '<(SHARED_INTERMEDIATE_DIR)/<(_target_name)/qrc/qrc_<(RULE_INPUT_ROOT).cpp',
    ],
    'message': 'Rcc-ing <(RULE_INPUT_ROOT).qrc..',
    'process_outputs_as_sources': 1,
  }],
}
