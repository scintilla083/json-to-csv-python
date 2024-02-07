from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from utils.convert import Converter
from utils.checker import TypeChecker

app = FastAPI()


@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):

    with open(f'./downloads/{file.filename}', "wb") as f:
        f.write(await file.read())

    checker = TypeChecker(file_path=f'./downloads/{file.filename}')
    result = checker.check()

    output_file = f"converted/converted_{file.filename}.csv"
    converter = Converter(result=result, output=output_file)
    converter.convert()

    return {"filename": output_file}


@app.get("/download-file/")
async def download_file(filename: str):
    file_path = f"./downloads/{filename}"
    return FileResponse(file_path, filename=filename)
