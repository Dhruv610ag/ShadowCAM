import uvicorn
from fastapi import FastAPI,Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from stream_utils import Streaming
import threading

app=FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")
stream_thread=None

streaming=Streaming()

@app.get("/") #route name
def serve_ui():
    return FileResponse("static/index.html")

@app.get("/start") #route name
def start_streaming(
    source :str =Query("0"),
    fps :int =Query(15),
    blur_strength :  int=Query(21),
    background : str = Query('none') 
    ):
    streaming.update_streaming_config(in_source=source,out_source=None,fps=fps,blur_strength=blur_strength,background=background)
    
    if streaming.running:
        return JSONResponse(content={"message" : "stream already running"},status_code=400)
    global stream_thread
    stream_thread=threading.Thread(
        target=streaming.stream_video,args=()
    )
    stream_thread.start()
    return {"message" : f"Streaming Started from source : {fps} FPS and blur strength {blur_strength}"}

@app.get("/stop")
def stop_streaming():
    return streaming.update_running_status()

@app.get("/devices") #route name
def devices():
    return streaming.list_available_devices()

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)