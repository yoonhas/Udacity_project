import media
import fresh_tomatoes


#generate instances with name, story, image url, trailer url, director, and opening date)
old_boy = media.Movie("Old Boy", "A stroy for toy", "https://upload.wikimedia.org/wikipedia/en/6/67/Oldboykoreanposter.jpg", "https://www.youtube.com/watch?v=D89OHw0VsYM", "Park Chan-wook", "2003")
midnight = media.Movie("Midnight in Paris", "old story", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=dtiklALGz20", "Woody Allen", "2011")
spider_man = media.Movie("Spider Man", "Hero movie", "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg", "https://www.youtube.com/watch?v=Fbfe3dH4LDs", "Jon Watts", "2017")
Thor = media.Movie("Thor", "Hero movie", "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg", "https://www.youtube.com/watch?v=ue80QwXMRHg", "Taika Waititi", "2017")
iron_man = media.Movie("Iron Man", "Hero movie", "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg", "https://www.youtube.com/watch?v=2CzoSeClcw0", "Shane Black", "2013")
Captain = media.Movie("Captain America: Civil War", "Hero movie", "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg", "https://www.youtube.com/watch?v=dKrVegVI0Us", "Anthony Russo", "2016")

#put instances in a array
movies = [old_boy, midnight, spider_man, Thor, iron_man, Captain]

fresh_tomatoes.open_movies_page(movies) # pass movies array to fresh tomato
