# -*- mode: python -*-
a = Analysis(['client.py'],
             pathex=['D:\\GitHub\\socket-HTTP-master'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='client.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
