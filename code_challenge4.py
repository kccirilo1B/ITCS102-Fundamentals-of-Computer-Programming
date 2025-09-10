print("Welcome to the Manga/Anime Recommender!")
print("Let me ask you a few questions to recommend something you'll love :)")

genre = input("What genre do you like? (action, romance, comedy) ")
duration = input("What length are you looking for? (long, medium, short) ")
year = input("What year are you interested in? (2000s, 1990s, etc.) ")
media_type = input("Are you looking for a manga or anime? (manga, anime) ")

recommendations = {
    ("action", "short", "2000s", "manga"): "Sakamoto Days! (Published 2020)",
    ("action", "medium", "2000s", "manga"): "Attack on Titan! (Published 2009)",
    ("action", "long", "2000s", "manga"): "ALIVE! (Published 2006)",
    ("romance", "short", "2000s", "manga"): "Mizutama Honeyboy! (Published 2013)",
    ("romance", "medium", "2000s", "manga"): "Love Rossi! (Published 2011)",
    ("romance", "long", "2000s", "manga"): "Love is Complex! (Published 2001)",
    ("comedy", "short", "2000s", "manga"): "Finishid Twilight! (Published 2012)",
    ("comedy", "medium", "2000s", "manga"): "Grand Blue! (Published 2014)",
    ("comedy", "long", "2000s", "manga"): "Barakamon! (Published 2008)",
    ("action", "short", "1990s", "manga"): "Rurouni Kenshin (Published 1994)",
    ("action", "medium", "1990s", "manga"): "Berserk (Published 1989)",
    ("action", "long", "1990s", "manga"): "Hunter x Hunter (Published 1998)",
    ("romance", "short", "1990s", "manga"): "Marmalade Boy (Published 1992)",
    ("romance", "medium", "1990s", "manga"): "Boys Over Flowers (Published 1992)",
    ("romance", "long", "1990s", "manga"): "Fushigi Yuugi (Published 1992)",
    ("comedy", "short", "1990s", "manga"): "Ninku (Published 1993)",
    ("comedy", "medium", "1990s", "manga"): "Yu Yu Hakusho (Published 1990)",
    ("comedy", "long", "1990s", "manga"): "Oh My Goddess! (Published 1988)",
    ("action", "short", "2000s", "anime"): "Kill la Kill (Aired 2013)",
    ("action", "medium", "2000s", "anime"): "Code Geass (Aired 2006)",
    ("action", "long", "2000s", "anime"): "Fullmetal Alchemist: Brotherhood (Aired 2009)",
    ("romance", "short", "2000s", "anime"): "Tsuredure Children (Aired 2017)",
    ("romance", "medium", "2000s", "anime"): "Kaichou wa Maid-sama! (Aired 2010)",
    ("romance", "long", "2000s", "anime"): "Clannad (Aired 2007)",
    ("comedy", "short", "2000s", "anime"): "Nichijou (Aired 2011)",
    ("comedy", "medium", "2000s", "anime"): "Ouran High School Host Club (Aired 2006)",
    ("comedy", "long", "2000s", "anime"): "Gintama (Aired 2006)",
    ("action", "short", "1990s", "anime"): "Mobile Suit Gundam Wing (Aired 1995)",
    ("action", "medium", "1990s", "anime"): "Neon Genesis Evangelion (Aired 1995)",
    ("action", "long", "1990s", "anime"): "Cowboy Bebop (Aired 1998)",
    ("romance", "short", "1990s", "anime"): "Kare Kano (Aired 1998)",
    ("romance", "medium", "1990s", "anime"): "Akazukin Chacha (Aired 1994)",
    ("romance", "long", "1990s", "anime"): "Sailor Moon (Aired 1992)",
    ("comedy", "short", "1990s", "anime"): "Slayers (Aired 1995)",
    ("comedy", "medium", "1990s", "anime"): "Great Teacher Onizuka (Aired 1999)",
    ("comedy", "long", "1990s", "anime"): "Ranma ½ (Aired 1989)",
}

recommendation = recommendations.get((genre, duration, year, media_type))

if recommendation:
    print(f"I recommend: {recommendation}")
else:
    print("Sorry, I don't have a recommendation for that combination.")
