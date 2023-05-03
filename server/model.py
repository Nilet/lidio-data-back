from pydantic import BaseModel, Field


class FileSchema(BaseModel):
    filename: str
    extension: str = Field(..., regex=r'^(xls|xlsx|csv)$')
    content: bytes

    class Config:
        schema_extra = {
            "example": {
                "filename": "example_file",
                "extension": "txt",
                "content": b"Example file content"
            }
        }
