from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - chintupana-coll-571f541f76154643887e90d771efbc6a',debug=False,docs_url='/stoic-chandrasekhar-0080aa9ab70511ef908f0242ac12000549/docs',openapi_url='/stoic-chandrasekhar-0080aa9ab70511ef908f0242ac12000549/openapi.json')

app.include_router(router, prefix='/stoic-chandrasekhar-0080aa9ab70511ef908f0242ac12000549/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()