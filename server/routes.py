from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import pandas as pd
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from zipfile import BadZipfile
from .labs.agrisolum import agrisolum2datafarm, agrisolum2inceres
from io import BytesIO
from fastapi.responses import StreamingResponse


router = APIRouter()


def read_file(file: UploadFile):
    filename = file.filename if file.filename else ""
    if filename.endswith(".csv"):
        return pd.read_csv(file.file, dtype=str)
    elif filename.endswith((".xlsx", ".xls")):
        return pd.read_excel(file.file, dtype=str, header=1)


@router.post("/agrisolum/{destLab}")
async def agrisolum(file: UploadFile = File(...), destLab = ""):
    filename = file.filename if file.filename else ""
    if not filename.endswith((".csv", ".xlsx", ".xls")):
        response = JSONResponse(status_code=HTTP_400_BAD_REQUEST,content={"error": "Extensão inválida"});
        print('"error": "Extensão inválida" ')
        return response

    try:
        print(f"agrisolum/{destLab}")
        openFile = read_file(file)
        if destLab == "inceres":
            df_formatado = agrisolum2inceres(openFile)
        elif destLab == "datafarm":
            df_formatado = agrisolum2datafarm(openFile)
        else: 
            response = JSONResponse(status_code=HTTP_403_FORBIDDEN, content={"error": "Laboratorio final nao existe"})


        output = BytesIO()
        df_formatado.to_excel(output, index=False)
        output.seek(0)

        response = StreamingResponse(
                output, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response.headers["Content-Disposition"] = f"attachment; filename=processed_{filename}"
        print("Sucesso")
        return response
    except BadZipfile:
        response = JSONResponse(status_code=HTTP_400_BAD_REQUEST,content={"error": "Erro ao ler o arquivo"});
        print('"error": "Erro ao ler o arquivo"')
        return response
    # except:
    #     response = JSONResponse(status_code=HTTP_400_BAD_REQUEST,content={"error": "Arquivo nao pertence ao lab"});
    #     print('"error": "Arquivo nao pertence ao lab"')
    #     return response
