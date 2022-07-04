@ECHO OFF

IF NOT "%1"=="" (
    SET CHOICE=%1
    CLS
    GOTO LBL_CHOICE
)

echo.
echo  �ᯮ�짮����: make [��������]
echo  -----------------------------
echo. 
echo    ��������          ��������
echo    --------          --------
echo    venv              ������� �।� ࠧࠡ�⪨, �ᯮ���� ����㠫쭮� ���㦥���
echo    base_deps         ��⠭����� ������ ����ᨬ��� 
rem echo    prod_deps         ��⠭����� ����ᨬ��� ��� �த��襭
rem echo    dev_deps          ��⠭����� ����ᨬ��� ��� ࠧࠡ�⪨
echo    clean             ������� ����㠫쭮� ���㦥���
echo.   
echo    freeze            ���������� development.pip �� �᭮�� ��⠭�������� ������⥪
echo.  

GOTO:EOF  

:LBL_CHOICE
IF "%CHOICE%"=="venv" (CALL:FUNC_VENV)
IF "%CHOICE%"=="base_deps" (CALL:FUNC_BASE_DEPS)
IF "%CHOICE%"=="prod_deps" (CALL:FUNC_PROD_DEPS)
IF "%CHOICE%"=="dev_deps" (CALL:FUNC_DEV_DEPS)
IF "%CHOICE%"=="clean" (CALL:FUNC_CLEAN)
IF "%CHOICE%"=="freeze" (CALL:FUNC_FREEZE)
IF "%CHOICE%"=="docker_push" (CALL:FUNC_DOCKER_PUSH)
GOTO:EOF  

:FUNC_VENV
  python.exe -m venv --copies --without-pip venv 
  CALL .\venv\Scripts\activate.bat
  curl https://bootstrap.pypa.io/get-pip.py --ssl-no-revoke | python.exe
  CALL .\venv\Scripts\deactivate.bat
GOTO:EOF  

:FUNC_BASE_DEPS
  CALL .\venv\Scripts\activate.bat
  pip.exe install --requirement=".\requirements\base.pip"
  CALL .\venv\Scripts\deactivate.bat
GOTO:EOF  

:FUNC_PROD_DEPS
  CALL .\venv\Scripts\activate.bat
  pip.exe install --requirement=".\requirements\production.pip"
  CALL .\venv\Scripts\deactivate.bat
GOTO:EOF  cd

:FUNC_DEV_DEPS
  CALL .\venv\Scripts\activate.bat
  pip.exe install --requirement=".\requirements\development.pip"
  CALL .\venv\Scripts\deactivate.bat
GOTO:EOF  

:FUNC_CLEAN
  @RMDIR /s /q ".\venv"
GOTO:EOF  

:FUNC_FREEZE
  CALL .\venv\Scripts\activate.bat
  pip.exe freeze > .\requirements\base.pip
  CALL .\venv\Scripts\deactivate.bat
GOTO:EOF
