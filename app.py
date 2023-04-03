from fastapi import FastAPI
from pydantic import BaseModel
import tiktoken

app = FastAPI()


@app.get("/")
async def index():
  return {"service": "tiktoken service", "status": 200}


class TiktokenPayload(BaseModel):
  content: str
  model: str = 'gpt-3.5-turbo'


class TiktokenResponse(BaseModel):
  token_len: int


@app.post("/num-of-token")
async def num_of_token(options: TiktokenPayload) -> TiktokenResponse:
  encoding = tiktoken.encoding_for_model(options.model)
  return TiktokenResponse(token_len=len(encoding.encode(options.content)))
