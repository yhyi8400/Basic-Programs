# youtubeDownload
from pytube import YouTube
download_folder = 'G:\\멧돼지영상'
#url = 'https://www.youtube.com/watch?v=M4aPML93B9Q'
#url = 'https://www.youtube.com/watch?v=M-NAkwSRB74'
#url = 'https://www.youtube.com/watch?v=BbOvX_JmEzQ'
#url = 'https://www.youtube.com/watch?v=TPGyzzcmhcE'
#url = 'https://www.youtube.com/watch?v=CPW7raxp4Fo'
#url ='https://www.youtube.com/watch?v=ruzG1PIKYfE'
url = 'https://www.youtube.com/watch?v=T158jICxRgQ'
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(download_folder)
