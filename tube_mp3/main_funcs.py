# import subprocess
# import youtube_dl
# import os
#
#
# def song_catcher(video_url, distination_folder:None):
#     video_info = youtube_dl.YoutubeDL().extract_info(
#         url=video_url, download=False)
#     video_title = video_info['title']
#     video_title = "aaa"
#
#
#     if distination_folder:
#         destination = distination_folder
#     else:
#         destination = "C:\\Users\\M\\Downloads"
#
#     filename = f"{video_info['title']}.mp3"
#     output_path = os.path.join(destination, filename)
#
#     options = {
#         # reduces the several line of output to barest minimal and therefore, time
#         'quiet': True,
#         'noplaylist': True,
#         'format': 'bestaudio/best',
#         'keepvideo': False,
#         'outtmpl': output_path,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }]
#     }
#     with youtube_dl.YoutubeDL(options) as ydl:
#         ydl.download([video_info['webpage_url']])
#
#     # returns os system eg. 'nt' for windows
#     coding_env = os.name
#
#     # Open the file once it has been downloaded
#     os.startfile(filename) if coding_env == 'nt' else subprocess.call(
#         ["open", filename])
#
#
# if __name__ == "__main__":
#     song_catcher("https://youtu.be/4GLfMTfxOwE?si=VeAW4hdYHxfh1iyy", None)
