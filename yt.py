import sys
import yt_dlp

# download YT
def download_youtube_video(url, output_name):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # best quality
        'outtmpl': f'{output_name}.%(ext)s',   # save
        'merge_output_format': 'mp4'           # format with mp4
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading '{url}'...")
        ydl.download([url])
        print(f"Download completed. Saved as '{output_name}.mp4'")

def main():
    # learn how to use arguments scrub
    if len(sys.argv) != 3:
        print("Usage: python script.py <YouTube_URL> <Output_Name>")
        sys.exit(1)
    
    url = sys.argv[1]
    output_name = sys.argv[2]
    
    # download
    download_youtube_video(url, output_name)

if __name__ == "__main__":
    main()

