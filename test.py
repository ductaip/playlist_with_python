import pygame
import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

	def open(self):
		webbrowser.open(self.link)

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

class TextButton:
	def __init__(self,text,position):
		self.text = text 
		self.position = position

	def is_mouse_on_text(self):
		mouse_x,mouse_y = pygame.mouse.get_pos()
		if mouse_x > self.position[0] and mouse_x < self.position[0] + self.text_box[2] and mouse_y > self.position[1] and mouse_y < self.position[1] + self.text_box[3]:
			return True
		return False

	def draw(self):
		font = pygame.font.SysFont('sans',25)
		text_render = font.render(self.text,True,(0,0,0))
		self.text_box = text_render.get_rect()
		if self.is_mouse_on_text():
			text_render = font.render(self.text,True,(0,0,255))
			pygame.draw.line(screen,(0,0,255),(self.position[0],self.position[1]+self.text_box[3]),(self.position[0]+self.text_box[2],self.position[1]+self.text_box[3]))
		else:
			text_render = font.render(self.text,True,(0,0,0))

		screen.blit(text_render,self.position)

	def draw_des(self,button,info,color):
		if	button.is_mouse_on_text():
			font = pygame.font.SysFont('sans',20)
			text_render = font.render(self.text,True,(0,0,0))
			text_box = text_render.get_rect()
			font_info = pygame.font.SysFont('sans',30)
			text_render_info = font_info.render(info,True,(0,0,0))
			text_place = text_render_info.get_rect()
			# screen.blit(text_render,(self.position[0] + 50 + text_box[3], self.position[1] + 50*i + 50 + text_box[2] ))
			pygame.draw.rect(screen,color,(mouse[0],mouse[1],text_box[2],text_box[3]))
			screen.blit(text_render,(mouse[0],mouse[1]))



def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file):
	videos = []
	total = file.readline()		
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist_from_txt(file):
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
		playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
		return playlist

def read_playlists_from_txt():
	playlists = []

	with open("data_music.txt", "r") as file:
		total = file.readline()
		for i in range(int(total)):
			playlist = read_playlist_from_txt(file)
			playlists.append(playlist)
	return playlists

pygame.init()
screen = pygame.display.set_mode((700,400))
pygame.display.set_caption('Playlist')
running = True 
BLACK = (0,0,0)
WHITE = (255,255,255)
clock = pygame.time.Clock()

playlists = read_playlists_from_txt()


playlists_button_list = []
videos_button_list = []
playlists_description = []

for i in range(len(playlists)):
	position = (50,50)
	playlist_des = TextButton(playlists[i].description.rstrip(),position)
	playlists_description.append(playlist_des)

for i in range(len(playlists)):
	playlist_btn = TextButton(playlists[i].name.rstrip(),(50,50+50*i))
	playlists_button_list.append(playlist_btn)


while running:
	clock.tick(60)
	screen.fill((255,255,255))
	mouse = pygame.mouse.get_pos()

# draw playlists
	for playlist_btn in playlists_button_list:
		playlist_btn.draw()

# draw videos
	for video_btn in videos_button_list:
		video_btn.draw()

# draw description of playlist
	for i in range(len(playlists_button_list)):
		playlists_description[i].draw_des(playlists_button_list[i],playlists[i].name,(255,0,255))

# draw link description of videos
	for i in range(len(videos_button_list)):
		video_link_button[i].draw_des(videos_button_list[i],playlists[playlist_choice].videos[i].title,(0,38,230))

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for i in range(len(playlists_button_list)):
					if playlists_button_list[i].is_mouse_on_text():
						videos_button_list = []
						playlist_choice = i
						video_link_button = []
						for y in range(len(playlists[i].videos)):
							video_button = TextButton(str(y+1) + ". " + playlists[i].videos[y].title.rstrip(),(400,50+50*y))
							videos_button_list.append(video_button)
						for a in range(len(playlists[i].videos)):
							video_link = TextButton(playlists[i].videos[y].link.rstrip(),(250,50))	
							video_link_button.append(video_link)

				for i in range(len(videos_button_list)):
					if videos_button_list[i].is_mouse_on_text():
						playlists[playlist_choice].videos[i].open()


		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()