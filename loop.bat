FOR /f "delims=" %%F IN ('dir /b input') DO (
    ffmpeg -i "input\%%F" -vf scale=320:-1 "output\%%F"
)
