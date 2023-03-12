from pytube import YouTube

def Download(link):
    SAVE_PATH = r"C:\Users\shrik\OneDrive\Desktop\YT_Videos"
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(SAVE_PATH)
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    print("You can find the downloaded video in : ", SAVE_PATH)


link = input("Enter the YouTube video URL: ")
Download(link)
