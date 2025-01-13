from typing import Optional
from uuid import uuid4

from fastapi import (
    APIRouter,
    Header,
    Request,
    Response,
    status,
    UploadFile,
)
from fastapi.responses import JSONResponse

from app.constants import UPLOAD_DIR

router = APIRouter(prefix="/files")


@router.post("/upload")
async def create_upload(
    file_uploads: list[UploadFile],
    request: Request,
    response: Response,
    hx_request: Optional[str] = Header(None),
):
    for file_upload in file_uploads:
        file_name = file_upload.filename
        secure_file_name = f"{uuid4().hex}_{file_name}"
        data = await file_upload.read()
        save_to = UPLOAD_DIR / secure_file_name
        with open(save_to, "wb") as file:
            file.write(data)
    return JSONResponse(
        content={"filenames": [file.filename for file in file_uploads]},
        status_code=status.HTTP_200_OK,
    )
