# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['biosafety_checklist.py'],
    pathex=[],
    binaries=[('C:\\Users\\agkap\\anaconda3\\Library\\bin\\tcl86t.dll', '.'), ('C:\\Users\\agkap\\anaconda3\\Library\\bin\\tk86t.dll', '.'), ('C:\\Users\\agkap\\anaconda3\\Library\\bin\\libexpat.dll', '.')],
    datas=[('ΥΠΑΑΤ_ICON_Exe.ico', '.'), ('Screenshot 2026-06-25 130650.png', '.')],
    hiddenimports=['openpyxl', 'openpyxl.styles', 'openpyxl.cell._writer', 'et_xmlfile', 'xml.parsers.expat'],
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
    name='Checklist_Bioasfaleias_2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ΥΠΑΑΤ_ICON_Exe.ico'],
)
