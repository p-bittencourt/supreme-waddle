from fastapi import HTTPException


class BadRequest(HTTPException):
    def __init__(self, resource: str = "Resource", id=None, detail: str = None):
        message = detail or (
            f"{resource} is invalid or the request was malformed"
            if id is None
            else f"{resource} #{id} is invalid or the request was malformed"
        )
        super().__init__(status_code=400, detail=message)


class NotFound(HTTPException):
    def __init__(self, resource: str = "Resource", id=None, detail: str = None):
        message = detail or (
            f"{resource} not found" if id is None else f"{resource} #{id} not found"
        )
        super().__init__(status_code=404, detail=message)
