import cv2, pafy

url = "./cctv-stream/MerdekaAceh01.ts"
videoPafy = pafy.new(url)
best = videoPafy.getbest(preftype="webm")

video=cv2.VideoCapture(best.url)
