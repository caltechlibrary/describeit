# -*- mode: python -*-
# =============================================================================
# @file    pyinstaller-win32.spec
# @brief   Spec file for PyInstaller for Windows
# @author  Michael Hucka
# @license Please see the file named LICENSE in the project directory
# @website https://github.com/caltechlibrary/checkit
# =============================================================================

import imp
import os
import sys

# The list must contain tuples: ('file', 'destination directory').
data_files = [ ('checkit\checkit.ini', 'checkit'),
               ('checkit\data\client_secrets.json', 'checkit\data'),
               ('checkit\data\help.html', 'checkit\data') ]

configuration = Analysis([r'checkit\__main__.py'],
                         pathex = ['.'],
                         binaries = [],
                         datas = data_files,
                         hiddenimports = ['apiclient', 'keyring.backends',
                                          'wx._html', 'wx._xml',
                                          'win32timezone', 'winreg'],
                         hookspath = [],
                         runtime_hooks = [],
                         excludes = [],
                         win_no_prefer_redirects = False,
                         win_private_assemblies = False,
                         cipher = None,
                        )

application_pyz    = PYZ(configuration.pure,
                         configuration.zipped_data,
                         cipher = None,
                        )

executable         = EXE(application_pyz,
                         configuration.scripts,
                         configuration.binaries,
                         configuration.zipfiles,
                         configuration.datas,
                         name = 'CheckIt',
                         icon = r'dev\icons\generated-icons\checkit-icon-512px.ico',
                         debug = False,
                         strip = False,
                         upx = True,
                         runtime_tmpdir = None,
                         console = False,
                        )

app             = BUNDLE(executable,
                         name = 'CheckIt.exe',
                         icon = r'dev\icons\generated-icons\checkit-icon-512px.ico',
                         bundle_identifier = None,
                         info_plist = {'NSHighResolutionCapable': 'True'},
                        )
