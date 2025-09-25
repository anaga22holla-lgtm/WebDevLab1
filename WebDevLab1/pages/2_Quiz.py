import streamlit as st



def intro():

    cookieImg = "Images/cookie.png"
    st.header("What type of cookie are you? ⋆｡‧˚ʚ🍪ɞ˚‧｡⋆ ")
    st.subheader("Answer the questions to find out what kind of cookie matches your personality")
    st.image(cookieImg, width = 250)

intro()

def questions():


    chocolateChip = 0
    snickerdoodle = 0
    oatmealRaisin = 0
    sugar = 0

    choice1 = st.radio(  # NEW
        " **How would your friends describe you?** •ᴗ• ",
        ["Loyal and a problem solver", "Warm and dependable", "Down to earth and chill", "Outgoing and energetic"])

    choice2 = st.multiselect(  # NEW
        " **What are your favorite genres of movies?** ₊⊹ ",
        ["Horror", "Psychological Thriller", "Romcom", "Documentary", "Comedy", "Action/Thriller"])

    choice3 = st.radio(
        " **What does your ideal weekend include?** ✿ ",
        ["Rewatching a comfort series/movie", "Reading and journaling", "Going out and partying", "Sleeping and hanging out with some friends"])

    choice4 = st.number_input(  # NEW
        " **Typically, how many hours do you spend on social media in a day?** ✶⋆.˚",
        min_value = 0,
        max_value = 24
        )

    choice5 = st.radio(  
        " **What is your beverage of choice?** ☕ᝰ",
        ["Soda", "Coffee", "Hot chocolate", "Tea"])


    # personality
    if choice1 == "Loyal and a problem solver":
        oatmealRaisin += 10
    elif choice1 == "Warm and dependable":
        snickerdoodle += 10
    elif choice1 == "Down to earth and chill":
        chocolateChip += 10
    else:
        sugar += 10

    # genres
    for genre in choice2:
        if genre == "Horror":
            oatmealRaisin += 1
            chocolateChip += 0.5
        elif genre == "Psychological Thriller":
            oatmealRaisin += 1
            sugar += 0.5
        elif genre == "Romcom":
            sugar += 0.5
            snickerdoodle += 1
        elif genre == "Documentary":
            oatmealRaisin += 0.5
            snickerdoodle += 1
        elif genre == "Comedy":
            snickerdoodle += 0.5
            chocolateChip += 1
        elif genre == "Action/Thriller":
            sugar += 1
            chocolateChip += 0.5

    # ideal weekend
    if choice3 == "Rewatching a comfort series/movie":
        snickerdoodle += 3
    elif choice3 == "Reading and journaling":
        oatmealRaisin += 3
    elif choice3 == "Going out and partying":
        sugar += 3
    else:
        chocolateChip += 3
        


    # hours social media
    if choice4 <= 2:
        oatmealRaisin += 1
    elif choice4 > 2 and choice4 < 6:
        chocolateChip += 1
    elif choice4 == 6 or choice4 == 7:
        snickerdoodle += 1
    else:
        sugar += 1


    # beverage
    if choice5 == "Soda":
        sugar += 3
    elif choice5 == "Tea":
        oatmealRaisin += 3
    elif choice5 == "Coffee":
        chocolateChip += 3
    else:
        snickerdoodle += 3
        
    userCookie = max(chocolateChip, snickerdoodle, sugar, oatmealRaisin)

    if userCookie == chocolateChip:
        typeCookie = "Chocolate Chip"
    elif userCookie == snickerdoodle:
        typeCookie = "Snickerdoodle"
    elif userCookie == sugar:
        typeCookie = "Sugar"
    else:
        typeCookie = "Oatmeal Raisin"
    


    if st.button("My result! 😋"):   #NEW
        st.balloons()   # NEW
        st.subheader(f"You are a {typeCookie} Cookie! °❀⋆.ೃ࿔ :･ ")
        if typeCookie == "Chocolate Chip":
            img = "Images/chocolatechip.jpeg"
            st.write(" **You are effortlessly cool and loved by all.** ≽^• ˕ • ྀི≼ ")
        elif typeCookie == "Snickerdoodle":
            img = "Images/snickerdoodle.jpeg"
            st.write(" **You are comforting and reliable.** -`♡´-")
        elif typeCookie == "Sugar":
            img = "Images/sugar.jpeg"
            st.write(" **You are sweet and socialable.**⋆ 𐙚 ̊")
        else:
            img = "Images/oatmealraisin.jpeg"
            st.write(" **You are an old soul with lots of intelligence.** 𖡼.𖤣𖥧𖡼.𖤣𖥧")

        st.image(img, width = 200)

    
    

questions()
        
    
