from typing import Optional
from uuid import uuid4

from fastapi import (
    APIRouter,
    Header,
    HTTPException,
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
    file_upload: UploadFile,
    request: Request,
    response: Response,
    hx_request: Optional[str] = Header(None),
):
    file_name = file_upload.filename
    if not file_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No file provided."
        )
    secure_file_name = f"{uuid4().hex}_{file_name}"
    try:
        data = await file_upload.read()
        save_to = UPLOAD_DIR / secure_file_name
        with open(save_to, "wb") as file:
            file.write(data)
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"File upload failed: {str(error)}",
        )

    return JSONResponse(
        content={
            "filename": secure_file_name,
            "message": "File uploaded successfully.",
        },
        status_code=status.HTTP_200_OK,
    )
