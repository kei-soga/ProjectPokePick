# __pycache__ファイルの一括削除

## bash

`find . -name '__pycache__' -type d -exec rm -r {} +`

※ docker環境で生成された場合、sudo必須

## PowerShell

`Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force`
