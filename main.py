import streamlit as st

# Title and description
st.title("Welcome to LearnIt!")
st.subheader("Your one-stop shop for online learning")

# Navigation bar (optional)
st.sidebar.header("Explore LearnIt!")
options = st.sidebar.radio("Select a subject:", ("All Subjects", "Math", "Science", "History", "geography"))

# Content based on user selection
if options == "All Subjects":
    st.header("All Subjects Offered")
    st.write("We offer a variety of courses across different subjects. Browse below to find what interests you!")
    # Add placeholders for course listings for all subjects
    st.write(" - Math 101")
    st.write(" - Biology for Beginners")
    st.write(" - World History Crash Course")
elif options == "Math":
    st.header("Math Courses")
    st.write("Sharpen your problem-solving skills with our engaging math courses!")
    # Add placeholders for specific math courses
    st.write(" - Algebra Fundamentals")
    st.write(" - Calculus for Beginners")
elif options == "Science":
    st.header("Science Courses")
    st.write("Explore the wonders of the universe with our exciting science courses!")
    # Add placeholders for specific science courses
    st.write(" - Introduction to Biology")
    st.write(" - Chemistry 101")
elif options == "History":
    st.header("History Courses")
    st.write("Embark on a journey through time with our captivating history courses!")
    # Add placeholders for specific history courses
    st.write(" - World History: Ancient Civilizations")
    st.write(" - American History: The Founding Fathers")
elif options == "geography":
    st.header("Geography Courses")
    st.write("Embark on a journey through time with our captivating HS courses!")
    # Add placeholders for specific history courses
    st.write(" - World History: Ancient Civilizations")
    st.write(" - American History: The Founding Fathers")

# About Us section
st.header("About LearnIt!")
st.write("We are a passionate team dedicated to making education accessible and engaging for everyone. Our courses are designed to be informative, interactive, and cater to different learning styles.")

# Call to action (optional)
st.header("Ready to Learn?")
st.button("Explore Courses Now!")

# Contact section
st.header("Contact Us")
st.write("Have questions or feedback? Reach out to us at:")
st.write("learn_it_support@email.com")

