from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")
def add(a, b):
   
	return float(a) + float(b)

@app.get("/subtract")
def subtract(a, b):
	
	return float(a) - float(b)

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=9321)
			 
