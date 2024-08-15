import sys
import yt_dlp

# Function to download YouTube video using yt-dlp
def download_youtube_video(url, output_name):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio available
        'outtmpl': f'{output_name}.%(ext)s',   # Save the video with the given output name and proper extension
        'merge_output_format': 'mp4'           # Ensure the output is in MP4 format
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading '{url}'...")
        ydl.download([url])
        print(f"Download completed. Saved as '{output_name}.mp4'")

# Main function to download video
def main():
    # Check if arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <YouTube_URL> <Output_Name>")
        sys.exit(1)
    
    url = sys.argv[1]
    output_name = sys.argv[2]
    
    # Download the video
    download_youtube_video(url, output_name)

if __name__ == "__main__":
    main()

