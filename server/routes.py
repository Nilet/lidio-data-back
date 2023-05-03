from fastapi import APIRouter, UploadFile, File
import pandas as pd
from .labs.agrisolum import agrisolum_formatter
from io import BytesIO
from fastapi.responses import StreamingResponse


router = APIRouter()


def read_file(file: UploadFile):
    filename = file.filename if file.filename else ""
    if filename.endswith(".csv"):
        return pd.read_csv(file.file, dtype=str)
    elif filename.endswith((".xlsx", ".xls")):
        return pd.read_excel(file.file, dtype=str, header=1)


@router.post("/agrisolum")
async def agrisolum(file: UploadFile = File(...)):
    filename = file.filename if file.filename else ""
    if not filename.endswith((".csv", ".xlsx", ".xls")):
        return {"Erro": "Extensão inválida"}
    df = read_file(file)

    df_formatado = agrisolum_formatter(df)

    output = BytesIO()
    df_formatado.to_excel(output, index=False)
    output.seek(0)

    response = StreamingResponse(
        output, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response.headers["Content-Disposition"] = f"attachment; filename=processed_{filename}"
    return response
