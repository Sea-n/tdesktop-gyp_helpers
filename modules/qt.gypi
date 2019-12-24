# This file is part of Desktop App Toolkit,
# a set of libraries for developing nice desktop applications.
#
# For license and copyright information please follow this link:
# https://github.com/desktop-app/legal/blob/master/LEGAL

{
  'variables': {
    'variables': {
      'variables': {
        'variables': {
          'variables': {
            'conditions': [
              [ 'build_osx', {
                'qt_version%': '5.6.2',
              }, {
                'qt_version%': '5.12.5',
              }]
            ],
          },
          'qt_libs_5_12_5': [
            'qwebp',
            'qgif',
            'qjpeg',
            'Qt5PrintSupport',
            'Qt5AccessibilitySupport',
            'Qt5FontDatabaseSupport',
            'Qt5EventDispatcherSupport',
            'Qt5ThemeSupport',
            'Qt5Network',
            'Qt5Widgets',
            'Qt5Gui',
            'qtharfbuzz',
            'qtlibpng',
          ],
          'qt_version%': '<(qt_version)',
          'linux_path_qt%': '/usr/local/desktop-app/Qt-<(qt_version)',
        },
        'qt_version%': '<(qt_version)',
        'qt_loc_unix': '<(linux_path_qt)',
        'conditions': [
          [ 'build_win', {
            'qt_lib_prefix': '<(ld_lib_prefix)',
            'qt_lib_debug_postfix': 'd<(ld_lib_postfix)',
            'qt_lib_release_postfix': '<(ld_lib_postfix)',
            'qt_libs': [
              '<@(qt_libs_5_12_5)',
              'Qt5Core',
              'Qt5WindowsUIAutomationSupport',
              'qtmain',
              'qwindows',
              'qtfreetype',
              'qtpcre2',
            ],
          }],
          [ 'build_mac', {
            'qt_lib_prefix': '<(ld_lib_prefix)',
            'qt_lib_debug_postfix': '_debug<(ld_lib_postfix)',
            'qt_lib_release_postfix': '<(ld_lib_postfix)',
          }],
          [ 'build_mac and not build_osx', {
            'qt_libs': [
              '<@(qt_libs_5_12_5)',
              'Qt5Core',
              'Qt5GraphicsSupport',
              'Qt5ClipboardSupport',
              'qgenericbearer',
              'qtfreetype',
              'qtpcre2',
              'qcocoa',
            ],
          }],
          [ 'build_osx', {
            'qt_libs': [
              'qwebp',
              'Qt5PrintSupport',
              'Qt5PlatformSupport',
              'Qt5Network',
              'Qt5Widgets',
              'Qt5Gui',
              'Qt5Core',
              'qtharfbuzzng',
              'qgenericbearer',
              'qtfreetype',
              'qtpcre',
              'qcocoa',
            ],
          }],
          [ 'build_linux', {
            'qt_lib_prefix': 'lib',
            'qt_lib_debug_postfix': '.a',
            'qt_lib_release_postfix': '.a',
            'qt_libs': [
              'qxcb',
              'Qt5XcbQpa',
              'Qt5LinuxAccessibilitySupport',
              'Qt5ServiceSupport',
              'Qt5EdidSupport',
              'qconnmanbearer',
              'qgenericbearer',
              'qnmbearer',
              '<@(qt_libs_5_12_5)',
              'Qt5DBus',
              'Qt5Core',
              'qtpcre2',
              'SM',
              'ICE',
              'fontconfig',
              'freetype',
              'expat',
              'z',
              'xcb-shm',
              'xcb-xfixes',
              'xcb-render',
              'xcb-static',
            ],
          }],
        ],
      },
      'qt_version%': '<(qt_version)',
      'qt_loc_unix': '<(qt_loc_unix)',
      'qt_version_loc': '<!(python -c "print(\'<(qt_version)\'.replace(\'.\', \'_\'))")',
      'qt_libs_debug': [
        '<!@(python -c "for s in \'<@(qt_libs)\'.split(\' \'): print(\'<(qt_lib_prefix)\' + s + \'<(qt_lib_debug_postfix)\')")',
      ],
      'qt_libs_release': [
        '<!@(python -c "for s in \'<@(qt_libs)\'.split(\' \'): print(\'<(qt_lib_prefix)\' + s + \'<(qt_lib_release_postfix)\')")',
      ],
    },
    'qt_libs_debug': [ '<@(qt_libs_debug)' ],
    'qt_libs_release': [ '<@(qt_libs_release)' ],
    'qt_version%': '<(qt_version)',
    'conditions': [
      [ 'build_win', {
        'qt_loc': '<(libs_loc)/Qt-<(qt_version)',
      }, {
        'qt_loc': '<(qt_loc_unix)',
      }],
    ],

    # If you need moc sources include a line in your 'sources':
    # '<!@(python <(DEPTH)/list_sources.py [sources] <(qt_moc_list_sources_arg))'
    # where [sources] contains all your source files
    'qt_moc_list_sources_arg': '--moc-prefix SHARED_INTERMEDIATE_DIR/<(_target_name)/moc/moc_',

    'linux_path_xkbcommon%': '/usr/local',
    'linux_lib_ssl%': '/usr/local/desktop-app/openssl-1.1.1/lib/libssl.a',
    'linux_lib_crypto%': '/usr/local/desktop-app/openssl-1.1.1/lib/libcrypto.a',
    'linux_lib_icu%': 'libicutu.a libicui18n.a libicuuc.a libicudata.a',
  },

  'configurations': {
    'Debug': {
      'conditions' : [
        [ 'build_win', {
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalDependencies': [
                '<@(qt_libs_debug)',
                'Netapi32.lib',
                'Userenv.lib',
                'Version.lib',
                'Dwmapi.lib',
                'Wtsapi32.lib',
              ],
            },
          },
        }],
        [ 'build_mac', {
          'xcode_settings': {
            'OTHER_LDFLAGS': [
              '<@(qt_libs_debug)',
              '/usr/local/lib/libz.a',
            ],
          },
        }],
      ],
    },
    'Release': {
      'conditions' : [
        [ 'build_win', {
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalDependencies': [
                '<@(qt_libs_release)',
                'Netapi32.lib',
                'Userenv.lib',
                'Version.lib',
                'Dwmapi.lib',
                'Wtsapi32.lib',
              ],
            },
          },
        }],
        [ 'build_mac', {
          'xcode_settings': {
            'OTHER_LDFLAGS': [
              '<@(qt_libs_release)',
              '/usr/local/lib/libz.a',
            ],
          },
        }],
      ],
    },
  },

  'include_dirs': [
    '<(qt_loc)/include',
    '<(qt_loc)/include/QtCore',
    '<(qt_loc)/include/QtGui',
    '<(qt_loc)/include/QtDBus',
    '<(qt_loc)/include/QtCore/<(qt_version)',
    '<(qt_loc)/include/QtGui/<(qt_version)',
    '<(qt_loc)/include/QtCore/<(qt_version)/QtCore',
    '<(qt_loc)/include/QtGui/<(qt_version)/QtGui',
  ],
  'library_dirs': [
    '<(qt_loc)/lib',
    '<(qt_loc)/plugins',
    '<(qt_loc)/plugins/bearer',
    '<(qt_loc)/plugins/platforms',
    '<(qt_loc)/plugins/imageformats',
  ],
  'defines': [
    'QT_WIDGETS_LIB',
    'QT_NETWORK_LIB',
    'QT_GUI_LIB',
    'QT_CORE_LIB',
  ],
  'conditions': [
    [ 'build_linux', {
      'library_dirs': [
        '<(qt_loc)/plugins/platforminputcontexts',
      ],
      'dependencies': [
        '<(DEPTH)/helpers/platform/linux/linux_glibc_wraps.gyp:linux_glibc_wraps',
      ],
      'libraries': [
        '-lcomposeplatforminputcontextplugin',
        '-libusplatforminputcontextplugin',
        '-lfcitxplatforminputcontextplugin',
        '-lhimeplatforminputcontextplugin',
        '-lnimfplatforminputcontextplugin',
        '<@(qt_libs_release)',
        '<(linux_path_xkbcommon)/lib/libxkbcommon.a',
        '<(linux_path_xkbcommon)/lib/libxkbcommon-x11.a',
        '<(PRODUCT_DIR)/obj.target/helpers/platform/linux/liblinux_glibc_wraps.a',
        #'<(linux_lib_ssl)', # added in lib_ton
        #'<(linux_lib_crypto)', # added in lib_ton
        '<!@(python -c "for s in \'<(linux_lib_icu)\'.split(\' \'): print(s)")',
        '-lxcb',
        '-lX11',
        '-lX11-xcb',
        '-ldbus-1',
        '-ldl',
        '-lgthread-2.0',
        '-lglib-2.0',
        '-lpthread',
      ],
      'include_dirs': [
        '<(qt_loc)/mkspecs/linux-g++',
      ],
      'ldflags': [
        '-static-libstdc++',
        '-pthread',
        '-rdynamic',
      ],
    }],
    [ 'build_mac', {
      'xcode_settings': {
        'OTHER_LDFLAGS': [
          '-lcups',
        ],
      },
    }],
  ],
}
