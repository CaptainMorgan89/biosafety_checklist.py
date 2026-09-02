# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['biosafety_checklist.py'],
    pathex=[],
    binaries=[('C:\\Users\\agkap\\anaconda3\\Library\\bin\\tcl86t.dll', '.'), ('C:\\Users\\agkap\\anaconda3\\Library\\bin\\tk86t.dll', '.')],
    datas=[],
    hiddenimports=['openpyxl', 'openpyxl.styles', 'openpyxl.cell._writer', 'et_xmlfile'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Checklist_Debug',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
